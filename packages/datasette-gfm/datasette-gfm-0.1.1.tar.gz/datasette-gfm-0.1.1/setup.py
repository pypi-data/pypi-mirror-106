from setuptools import setup
import os

VERSION = "0.1.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-gfm",
    description="Export Datasette records as GitHub flavoured markdown",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Mike Ralphson",
    url="https://github.com/postman-open-technologies/datasette-gfm",
    project_urls={
        "Issues": "https://github.com/postman-open-technologies/datasette-gfm/issues",
        "CI": "https://github.com/postman-open-technologies/datasette-gfm/actions",
        "Changelog": "https://github.com/postman-open-technologies/datasette-gfm/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_gfm"],
    entry_points={"datasette": ["gfm = datasette_gfm"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio", "httpx", "sqlite-utils"]},
    tests_require=["datasette-gfm[test]"],
)
