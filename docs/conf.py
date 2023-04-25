# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "shedding.py"
copyright = "2023-present, toolifelesstocode"
author = "toolifelesstocode"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "hoverxref.extension",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Hoverxref options -------------------------------------------------------
# Thanks to Disnake for the hoverxref config https://github.com/DisnakeDev/disnake/blob/master/docs/conf.py#L228-L242
hoverx_default_type = "tooltip"
hoverxref_domains = ["python", "py"]
hoverxref_role_types = dict.fromkeys(
    ["ref", "class", "func", "meth", "attr", "exc", "data"],
    "tooltip",
)
hoverxref_tooltip_theme = ["tooltipster-custom"]
hoverxref_tooltip_lazy = True

hoverxref_intersphinx = [
    "python",
    "py",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_theme_options = {
    "source_repository": "https://github.com/toolifelesstocode/shedding.py",
    "source_branch": "main"
}

# -- Intersphinx options ------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}