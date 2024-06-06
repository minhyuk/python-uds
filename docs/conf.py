"""
Configuration file for the Sphinx documentation builder.

This file contains the configuration settings for building Sphinx documentation. It includes project information, general settings, HTML output options, LaTeX output options, and more.

The configuration includes details like author, project name, theme, output options, extensions, and document mappings.

For the full list of configuration options, refer to the Sphinx documentation: http://www.sphinx-doc.org/en/master/config
"""

# The code block contains the configuration settings for the Sphinx documentation builder.

# Project information
project = 'python-uds'
copyright = '2018, Richard Clubb'
author = 'Richard Clubb'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None

# HTML output
html_theme = 'default'
html_static_path = []

# HTMLHelp output
htmlhelp_basename = 'python-udsdoc'

# LaTeX output
latex_documents = [
    (master_doc, 'python-uds.tex', 'python-uds Documentation', 'Richard Clubb', 'manual'),
]

# Manual page output
man_pages = [
    (master_doc, 'python-uds', 'python-uds Documentation', [author], 1)
]

# Texinfo output
texinfo_documents = [
    (master_doc, 'python-uds', 'python-uds Documentation', author, 'python-uds', 'One line description of the project.', 'Miscellaneous')
]

# Epub output
epub_title = project
epub_exclude_files = ['search.html']

# Intersphinx configuration
intersphinx_mapping = {'https://docs.python.org/': None}

# Todo extension
todo_include_todos = True
