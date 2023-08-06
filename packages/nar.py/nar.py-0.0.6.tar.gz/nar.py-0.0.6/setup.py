from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'A Wrapper for browser game Nations at Risk\'s API'

# Setting up
setup(
    name="nar.py",
    version=VERSION,
    author="Blitz#6652",
    author_email="<blitz2k4.dev@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'nar', 'nations at risk'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)