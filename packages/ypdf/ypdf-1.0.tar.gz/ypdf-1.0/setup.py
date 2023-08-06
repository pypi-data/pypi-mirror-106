import setuptools
from pathlib import Path
setuptools.setup(
    name="ypdf",
    version=1.0,
    long_description=Path("tests/README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
