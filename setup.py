import io
import os

from setuptools import setup

# Package meta-data.
NAME = 'shadegpx'
DESCRIPTION = 'Compute "shade factor" on a runner during a race using GPX data and solar positions.'
URL = 'https://github.com/benmayersohn'
EMAIL = 'contact@benmayersohn.com'
AUTHOR = 'Ben Mayersohn'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = ['matplotlib>=3.0', 'pandas>=0.24', 'scipy>=1.2', 'seaborn>=0.9', 'numpy>=1.16', 'pysolar==0.8',
            'pytz>=2018', 'gpxpy>=1.3', 'requests>=2.21']

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=['shadegpx'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='Freely Distributable',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: Freely Distributable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ]
)
