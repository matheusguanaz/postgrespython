from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="postgrespython",
    version="0.0.2",
    author="Matheus Guanaz",
    author_email="",
    description="This package is a simple package for execute query in postgres databases using psycopg2 package, this package was used to learn how to post a package on pypi",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheusguanaz/postgrespython",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)