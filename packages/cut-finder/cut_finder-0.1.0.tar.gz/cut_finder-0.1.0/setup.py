"""setup"""
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="cut_finder",
    version="0.1.0",
    description="Plan lumber cutting schemes with minimal waste",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Cluff1112/cut_finder",
    author="Cory Cluff",
    author_email="cluff.cory@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("test",)),
    include_package_data=False,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "cutfinder=cut_finder.__main__:main",
        ]
    },
)
