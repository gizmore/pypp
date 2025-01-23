from setuptools import setup, find_packages

setup(
    name="pypp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["pypp=pypp.py:main"]
    },
    author="gizmore",
    description="A simple preprocessor for Python files",
    url="https://github.com/gizmore/pypp",
)
