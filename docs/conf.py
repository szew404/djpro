# This file is part of djpro.
#
# Copyright (c) 2024, Franco Gidaszewski <gidaszewskifranco@gmail.com>
#
# For the full copyright and license information, please view
# the LICENSE.txt file that was distributed with this source code.

#
# -- Utils ---------------------------------------------------------
#

import codecs
import os
import re
import sys
from datetime import date

PROJECT_DIR = os.path.abspath("..")
sys.path.insert(0, PROJECT_DIR)


def read_file(filepath):
    """Read content from a UTF-8 encoded text file."""
    with codecs.open(filepath, "rb", "utf-8") as file_handle:
        return file_handle.read()


def find_version(meta_file):
    """Extract ``__version__`` from meta_file."""
    contents = read_file(os.path.join(PROJECT_DIR, meta_file))
    meta_match = re.search(r"^__version__\s+=\s+['\"]([^'\"]*)['\"]", contents, re.M)

    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __version__ string in package meta file")


#
# -- Project information -----------------------------------------------------
#

# General information about the project.
project = "djpro"
copyright = f"2024-{date.today().year}, Franco Gidaszewski"
author = "Franco Gidaszewski"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# Allow non-local URIs, so we can have images in CHANGELOG etc.
suppress_warnings = [
    "image.nonlocal_uri",
]

# The master toctree document.
master_doc = "index"
# The version info
# The short X.Y version.
release = find_version(os.path.join("djpro", "__init__.py"))
version = release.rsplit(".", 1)[0]
# The full version, including alpha/beta/rc tags.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_favicon = None
html_theme = "furo"
html_title = project
html_static_path = ["_static"]

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
