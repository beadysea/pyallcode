"""Sphinx configuration for the pyallcode project.

This config enables API docs from the source code using autodoc and autosummary,
supports Google/NumPy-style docstrings via napoleon, and allows Markdown with MyST.
"""
from __future__ import annotations

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------

# Add the project root so Sphinx can import the package for autodoc
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# -- Project information -----------------------------------------------------

project = "pyallcode"
author = "pyallcode contributors"
copyright = f"{datetime.now().year}, {author}"

# If your package exposes a version string, you can import it here.
# We avoid importing the package to keep docs builds robust.
release = ""


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "myst_parser",
]

# Generate autosummary pages automatically
autosummary_generate = True

# Napoleon settings for Google/NumPy docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False

# Mock external dependencies that may not be installed in the docs environment
# (e.g., pyserial used by the transport layer)
autodoc_mock_imports = [
    "serial",
]

# If typehints exist, show them in descriptions instead of signatures (nicer)
autodoc_typehints = "description"

templates_path = ["_templates"]
exclude_patterns: list[str] = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# Support Markdown via MyST
myst_enable_extensions = [
    "deflist",
    "linkify",
]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Intersphinx -------------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
