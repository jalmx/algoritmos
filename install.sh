#!/bin/sh

pip install mkdocs mkdocs-material
pip install mkdocs-material
pip install mkdocs-plugin-tags
pip install mkdocs-markmap
pip install mkdocs-pdf-export-plugin
pip install bs4
pip install mkdocs-minify-plugin

pip install --upgrade Pillow 
pip install cairosvg

sudo apt-get install libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev
libpng-dev libz-dev -y
