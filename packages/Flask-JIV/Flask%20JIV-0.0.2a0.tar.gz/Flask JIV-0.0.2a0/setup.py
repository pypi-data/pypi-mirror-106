import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="Flask JIV",
    version="0.0.2-alpha",
    description="Validates JSON request body for flask endpoints",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rez4mt/flask-jiv",
    author="Reza Motlagh",
    author_email="rmoti49@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["flask_json_validator"],
    include_package_data=True,
    install_requires=["Flask>=1.1.2", "flask-inputs>=0.3.0", 'jsonschema>=3.2.0', 'future>=0.18.2'],
)
