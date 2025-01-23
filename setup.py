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
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    description="A simple preprocessor for Python files",
    url="https://github.com/gizmore/pypp",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
