# Accelerator for pip, the Python package manager.
#
# Author: Peter Odding <peter.odding@paylogic.com>
# Last Change: May 26, 2016
# URL: https://github.com/paylogic/pip-accel

"""Sphinx documentation configuration for the `pip-accel` project."""

import os
import sys

# Add the pip_accel source distribution's root directory to the module path.
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'humanfriendly.sphinx',
]

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pip-accel'
copyright = u'2016, Peter Odding and Paylogic International'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from pip_accel import __version__ as pip_accel_version  # NOQA

# The short X.Y version.
version = '.'.join(pip_accel_version.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = pip_accel_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# http://sphinx-doc.org/ext/autodoc.html#confval-autodoc_member_order
autodoc_member_order = 'bysource'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = dict(
    boto=('http://boto.readthedocs.org/en/latest/', None),
    coloredlogs=('http://coloredlogs.readthedocs.org/en/latest/', None),
    humanfriendly=('http://humanfriendly.readthedocs.org/en/latest/', None),
    packaging=('http://packaging.readthedocs.org/en/latest/', None),
    python=('http://docs.python.org', None),
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Output file base name for HTML help builder.
htmlhelp_basename = 'pip-acceldoc'
