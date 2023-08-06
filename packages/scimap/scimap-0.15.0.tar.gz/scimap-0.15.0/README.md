# Single-Cell Image Analysis Package

Scimap is a scalable toolkit for analyzing single-cell multiplex imaging data. The package uses the [anndata](https://anndata.readthedocs.io/en/stable/anndata.AnnData.html) framework making it easy to integrate with other popular single-cell analysis toolkits such as [scanpy](https://scanpy.readthedocs.io/en/latest/#). It includes preprocessing, phenotyping, visualization, clustering, spatial analysis and differential spatial testing. The Python-based implementation efficiently deals with datasets of more than one million cells.


[![build: Unix-Mac-Win](https://github.com/ajitjohnson/scimap/actions/workflows/build-unix-mac-win.yml/badge.svg)](https://github.com/ajitjohnson/scimap/actions/workflows/build-unix-mac-win.yml)
[![Documentation Status](https://readthedocs.org/projects/scimap-doc/badge/?version=latest)](https://scimap-doc.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/scimap)](https://pepy.tech/project/scimap)
[![PyPI Version](https://img.shields.io/pypi/v/scimap.svg)](https://pypi.org/project/scimap)
[![PyPI License](https://img.shields.io/pypi/l/scimap.svg)](https://pypi.org/project/scimap)
[![Gitter chat](https://badges.gitter.im/scimap_io/community.png)](https://gitter.im/scimap_io/community)

## Installation

We strongly recommend installing `scimap` in a fresh virtual environment.

```
# If you have conda installed
conda create --name scimap python=3.7
conda activate scimap
```

Install `scimap` directly into an activated virtual environment:

```python
$ pip install scimap
$ pip install napari[all] # For visualizing images
```

After installation, the package can be imported as:

```python
$ python
>>> import scimap as sm
```

## Get Started


#### Detailed documentation of `scimap` functions and tutorials are available [here](https://scimap-doc.readthedocs.io/en/latest/).
