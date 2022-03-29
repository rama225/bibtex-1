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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'bibtex'
copyright = '2022, Tarakarama'
author = 'Tarakarama'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.bibtex',]
bibtex_bibfiles = ['13_dir/$_13-bibliography.rst',
                             '13_dir/$_14-reference-1-book-food-method.bib',
                            '13_dir/$_14-reference-2-article-food-method.bib',
                            '13_dir/$_14-reference-3-book-food-ref.bib',
                            '13_dir/$_14-reference-4-article-food-ref.bib',
                            '13_dir/$_14-reference-5-misc-ontology.bib',
                            '13_dir/$_14-reference-6-misc-data.bib',
                            '13_dir/$_14-reference-7-misc-web.bib',
                            '13_dir/$_14-reference-8-article-technology.bib',
                           ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output ---------------------------------------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': '',

# Latex figure (float) alignment
'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
                  ('index', 'sample_doc.tex', 'sample\\_doc Documentation', 'hidepy', 'manual'),
                  ]

# The name of an image file (relative to this directory) to place at the top of the title page.
latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts, not chapters.
latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output -----------------------------------------------------------

# One entry per manual page.
# List of tuples (source start file, name, description, authors, manual section).
man_pages = [
            ('index', 'sample_doc', 'sample_doc Documentation', ['hidepy'], 1)
            ]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for Texinfo output ---------------------------------------------------------------

# Grouping the document tree into Texinfo files.
# List of tuples (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [
                    ('index', 'sample_doc', 'sample_doc Documentation', 'hidepy', 
                    'sample_doc', 'One line description of project.', 'Miscellaneous'),
                    ]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

