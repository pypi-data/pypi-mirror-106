from setuptools import setup, find_packages

setup(
    name = 'time-cross-validation',
    version = '0.0.2',
    description = 'Time series cross validation tool, supplementing or replacing relevant existing sklearn libraries.',
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    url = '',
    author = 'Riccardo Doyle',
    #py_modules = ["time_cross_validation"],
    author_email = 'riccardo.doyle.14@ucl.ac.uk',
    keywords = 'cross validation',
    packages = find_packages()
)
