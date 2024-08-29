# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'seshat.settings.base'
import seshat

# -- Project information -----------------------------------------------------

project = 'Seshat'
copyright = '2024, Majid Benam'
author = 'Majid Benam'

release = seshat.__version__

# -- General configuration ---------------------------------------------------

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


# -- Napoleon settings ----

napoleon_numpy_docstring = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True

# -- todo --
todo_include_todos = False

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_theme_options = {
    "use_download_button": True,
}

# -- copybutton settings ----

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
