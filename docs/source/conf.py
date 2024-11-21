# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'seshat.settings.base'


import seshat


# -- Project information -----------------------------------------------------

project = 'Seshat'
copyright = '2024, Seshat: Global History Databank'
author = 'Ed Chalstrey, Kalle Westerling, Majid Benam'

release = seshat.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "myst_parser",
    "autoapi.extension",
    "sphinx_copybutton",
    "nbsphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx_togglebutton",
    "sphinx_tabs.tabs",
    "sphinx_rtd_theme"
]

templates_path = ["_templates"]
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- autoapi configuration -----

autoapi_dirs = [
    "../../seshat/",
    "../../pulumi/",
]
autoapi_type = "python"
autoapi_root = "api"

autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    # "imported-members",
]

autoapi_ignore = [
    '_*',
    '*backup*',
    '*migrations*',
    '*mycodes*',
    '*myviews*',
]

autoapi_keep_files = True
autodoc_typehints = "description"
autoapi_add_toctree_entry = False
autoapi_member_order = "groupwise"

# def skip_attributes(app, what, name, obj, skip, options):
#     if what == "attribute":
#         skip = True
#     return skip

# def setup(sphinx):
#     sphinx.connect("autoapi-skip-member", skip_attributes)

# -- Napoleon settings ----

napoleon_numpy_docstring = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True

# -- todo --
todo_include_todos = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "use_download_button": True,
}
html_css_files = [
    'custom.css',
]

# -- copybutton settings ----

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
