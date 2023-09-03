# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Road-MAP-DevOPS'
copyright = '2023, CFRJ'
author = 'CFRJ'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # Geração automática de documentação a partir do código-fonte
    'sphinx.ext.napoleon',   # Suporte para docstrings estilo Google
    'sphinx.ext.viewcode',   # Links para o código-fonte
    'sphinx.ext.autosummary',
]

# Set the location of the autosummary templates
autosummary_generate = True
autosummary_imported_members = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
# Exclui a geração de HTML ao criar o formato EPUB
if tags.has('epub'):
    html_theme = 'basic'

# -- Options for output ------------------------------------------------------
# Define o diretório de saída da compilação
html_output = '_build/html'
# Configurações do EPUB
epub_title = 'Seu Título EPUB'
epub_author = 'Seu Nome'
epub_publisher = 'Sua Editora'
epub_language = 'pt_BR'
epub_scheme = 'URL do seu site'
epub_identifier = 'URL única para seu livro'
epub_uid = 'Identificador único'
epub_cover = ('_static/cover.png', 'cover.html')
epub_exclude_files = ['_static/*']