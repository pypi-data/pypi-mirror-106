from setuptools import setup
import os

VERSION = "0.3.12"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="gekitchensdk",
    description="gekitchensdk is now gehomesdk",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    install_requires=["gehomesdk"],
    classifiers=["Development Status :: 7 - Inactive"],
)
