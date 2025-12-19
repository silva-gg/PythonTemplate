"""
Setup script for your-package.
Uses pyproject.toml for configuration.
This file is mainly for compatibility with older tools.
"""

from setuptools import setup, find_packages

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
