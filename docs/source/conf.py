# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# 参考：
# jupyterhub的docs
# 设置：https://github.com/jupyterhub/jupyterhub/blob/master/docs/source/conf.py
# 效果：https://jupyterhub.readthedocs.io/en/stable/index.html
# binderhub的docs
# 设置：https://github.com/jupyterhub/binderhub/blob/master/doc/conf.py
# 效果：https://mybinder.readthedocs.io/en/latest/index.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import shlex
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'dfdata'
copyright = '2020, dfdata'
author = 'dfdata'

# The full version, including alpha/beta/rc tags
release = '0.0.3'



# Autopopulate version
from os.path import dirname

docs = dirname(dirname(__file__))
root = dirname(docs)
sys.path.insert(0, root)


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# pydata_sphinx_theme 插件
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'nbsphinx',
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '**.ipynb_checkpoints' ,    ## 忽略所有jupyter文件
    #'.ipynb_checkpoints/index-checkpoint.rst'
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "pydata_sphinx_theme"
#html_theme = "sphinx_rtd_theme"
#html_theme_path = ["_themes"]

html_logo = '_static/dfdata_logo.svg'


html_theme_options = {
    "github_url": "https://github.com/Eric2827/dfdata",
    "twitter_url": "https://twitter.com",
    # "use_edit_page_button": True   #在readthedocs构建不成功
}

'''
html_context = {
    "github_user": "Eric2827",
    "github_repo": "dfdata",
    "github_version": "master",
    "doc_path": "docs",
}
'''


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Read The Docs --------------------------------------------------------

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    # readthedocs.org uses their theme by default, so no need to specify it
    # build rest-api, since RTD doesn't run make
    from subprocess import check_call as sh

    #sh(['make', 'html'], cwd=docs)
    print("===============conf.py===================on_rtd==============")

