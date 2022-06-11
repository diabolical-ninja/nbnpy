"""Sphinx configuration."""

from datetime import datetime

project = "nbnpy"
author = "Yass"
copyright = f"{datetime.now().year}, {author}"
language = "en"
html_theme = "furo"
html_favicon = "images/favicon.png"
html_logo = "images/logo.png"

autodoc_typehints = "description"
pygments_style = "sphinx"
pygments_dark_style = "monokai"


extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]
