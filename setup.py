import os
from setuptools import setup, find_packages

with open(
    os.path.join(os.path.dirname(__file__), "requirements.txt"), "r"
) as fh:
    requirements = fh.readlines()

NAME = "b2u-conector-python"
DESCRIPTION = (
    "This is a lightweight library that works as a conector to b2u bank public API."
)
AUTHOR = "jeff0102"
URL = "https://github.com/jeff0102/b2u-conector-python"
VERSION = None

about = {}

root = os.path.abspath(os.path.dirname(__file__))

if not VERSION:
    with open(os.path.join(root, "b2u", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    license="MIT",
    description=DESCRIPTION,
    AUTHOR=AUTHOR,
    url=URL,
    keywords=["b2u", "Public API"],
    install_requires=[req for req in requirements],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
