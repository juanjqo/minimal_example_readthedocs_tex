# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'minimal_example'
copyright = '2024, Juan Jose Quiroz'
author = 'Juan Jose Quiroz'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'


mathjax3_config = {
    "TeX": {
        "Macros": {
            "imi": '{\\hat{\\imath}}',
	    "imj": '{\\hat{\\jmath}}',
	    "imk": '{\\hat{k}}',
            "dual": '{\\varepsilon}',
            "dq": ['{\\underline{\b{#1}}}',1],
            "quat": ['\b{#1}',1],
            "mymatrix": ['\b{#1}',1],
            }
        }
    }
