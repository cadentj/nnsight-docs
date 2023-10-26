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


fixed_sidebar=True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_charts.charts',
    'sphinx_copybutton',
    'jupyter_sphinx',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"


html_static_path = ['_static']

# html_sidebars = {
#     "**": ["search-field.html", "sidebar-nav-bs"]
# }

# html_logo = "_static/images/final.png"
# html_logo = "_static/images/edited_dalle.png"

html_theme_options = {
  "logo": {"text":"nnsight"},
  "show_nav_level": 2,
  "navbar_end": ["navbar-icon-links"],
  "search_bar_text": "Your text here...",
}


html_context = {
   "default_mode": "light"
}

