from setuptools import setup, find_packages

setup(
    name="ontology_sql",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["networkx", "sqlite3"],
)

# Built the package
#python -m build

# Publish it
#pip install twine
#twine upload dist/*

# Users can install it via
#pip install ontology_sql
