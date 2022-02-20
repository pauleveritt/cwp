project = 'Code With Paul'
copyright = '2022, Paul Everitt'
author = 'Paul Everitt'
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints"
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]
html_static_path = ["_static"]
templates_path = ["_templates"]
html_theme = "furo"
