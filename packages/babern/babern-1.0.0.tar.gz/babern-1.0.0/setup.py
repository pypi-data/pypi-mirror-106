import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="babern",
    version="1.0.0",
    description="babern engine",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ardustri/babern",
    author="Ardustri",
    author_email="admin@ardustri.co",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["babern"],
    include_package_data=True,
    install_requires=["playsound", "validator"],
    entry_points={
        "console_scripts": [
            "babern=reader.__main__:main",
        ]
    },
)
