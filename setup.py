from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("requirements/production.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="opulence.facts",
    version="0.0.4",
    description="Facts are used to represent intelligence",
    long_description=readme,
    author="Opulence",
    author_email="contact@opulence.fr",
    url="https://github.com/opullence/facts",
    license=license,
    packages=find_namespace_packages(include=["opulence.*"]),
    install_requires=requirements,
    python_requires=">=3.5.*, <4",
)
