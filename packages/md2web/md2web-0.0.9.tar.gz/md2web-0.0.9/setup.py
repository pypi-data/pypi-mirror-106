from os.path import join, isfile
from os import walk
import io
import os
import sys
from shutil import rmtree
from setuptools import find_packages, setup, Command


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

NAME = 'md2web'
FOLDER = 'md2web'
DESCRIPTION = 'An awesome and also useful sqlite high level api tools for python developer, enjoy~'
URL = 'https://github.com/szj2ys/md2web'
EMAIL = 'szj2ys@qq.com'
AUTHOR = 'szj'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

REQUIRED = read_requirements('requirements.txt')

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    with open(os.path.join(here, FOLDER, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


def package_files(directories):
    paths = []
    for item in directories:
        if isfile(item):
            paths.append(join('..', item))
            continue
        for (path, directories, filenames) in walk(item):
            for filename in filenames:
                paths.append(join('..', path, filename))
    return paths


class UploadCommand(Command):
    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Removing build files...')
        os.system('rm -rf *.egg-info')
        os.system('rm -rf build')
        os.system('rm -rf dist')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


class InstallCommand(Command):
    description = 'Build and install the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and install to local…')
        os.system('{0} setup.py install'.format(sys.executable))

        self.status('Removing build files...')
        os.system('rm -rf *.egg-info')
        os.system('rm -rf build')
        os.system('rm -rf dist')

        sys.exit()

setup(
    name=NAME,
    version=about['__version__'],
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=['examples','datasets', '*.db', '*.sqlite']),
    install_requires=REQUIRED,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'md2web = md2web.__main__:run',
        ],
    },
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

    cmdclass={
        # $ python setup.py pypi    # upload repository to pypi
        'pypi': UploadCommand,
        'get': InstallCommand,   # install package to local
    },
    zip_safe=False,
)
