#!/usr/bin/env python3
"""
Safe-LLM: Toolkit for LLM prompt injection testing and output security evaluation.
"""

from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Read requirements
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="safe-llm",
    version="0.1.0",
    description="Toolkit for LLM prompt injection testing and output security evaluation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/venkatasaiv/safe-llm",
    author="Venkata Saiv",
    author_email="venkatasaiv@example.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Security",
        "Topic :: Software Development :: Testing",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "safe-llm=safe_llm.cli:main",
        ],
    },
    keywords="llm security testing prompt-injection ai safety",
    project_urls={
        "Bug Reports": "https://github.com/venkatasaiv/safe-llm/issues",
        "Source": "https://github.com/venkatasaiv/safe-llm",
        "Documentation": "https://github.com/venkatasaiv/safe-llm/wiki",
    },
)
