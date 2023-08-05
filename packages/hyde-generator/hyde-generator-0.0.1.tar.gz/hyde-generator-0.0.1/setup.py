from setuptools import setup
from pathlib import Path

codeDirectory = Path(__file__).parent

readme = (codeDirectory / "README.markdown").read_text()
requirements = (codeDirectory / "requirements.txt")

with open(requirements) as requirements:
    requirements = requirements.readlines()
    requirements = [requirement.replace("\n", "") for requirement in requirements]

setup(
    name = "hyde-generator",
    version = "v0.0.1",
    description = "a simple static site generator",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/0x44RU5H/hyde",
    author = "Aarush Gupta",
    author_email = "aarush@theaarushgupta.com",
    license = "AGPLv3+",
    classifiers = [
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    packages = ["hyde"],
    package_data = {},
    install_requires = requirements,
    entry_points = {
        "console_scripts": ["hyde = hyde.hyde:main"]
    }
)