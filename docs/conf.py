"""Sphinx configuration."""

from datetime import datetime

project = "nbnpy"
author = "Yass"
copyright = f"{datetime.now().year}, {author}"
language = "en"
html_theme = "furo"
autodoc_typehints = "description"


extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
