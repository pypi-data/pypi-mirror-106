from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Ping library that will check if server is up or down'
LONG_DESCRIPTION = 'A package that allows you to check on a servers status. Can get GMAIL notifications if server is down.'

# Setting up
setup(
    name="Pyinger",
    version=VERSION,
    author="Sean Pelser",
    author_email="<sean.pelser97@gmail.com>",
    description=DESCRIPTION,
    url='https://github.com/seanp97/PyServerChecker',
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['ping3', 'colorama'],
    keywords=['python', 'ping', 'pinger', 'server', 'server checker', 'pyinger'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)