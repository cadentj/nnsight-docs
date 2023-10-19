# Configuration file for the Sphinx documentation builder.

import sys
sys.path.insert(0,'/home/caden/Programming/engine-docs')

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'nnsight'
copyright = '2023, Jaden Fiotto-Kaufman'
author = 'Jaden Fiotto-Kaufman'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_charts.charts',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

html_static_path = ['_static']
html_sidebars = {
    '**': [
        'globaltoc.html',
        'searchbox.html',
    ]
}
