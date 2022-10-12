"""
Generate COCO-formatted labels from one or multiple geojsons and images

Coco_solaris is a refactored and slimmed-down version of the package solaris, 
with a focus on conversion of geojson and image file to COCO format.

The original package, Solaris, is a collection of tools for converting data to
and from the COCO format, however it cannot be installed on some of the latest operating 
systems due to fixed dependencies on older tensorflow, torch and other libraries.

How to use:
from solaris2.data import coco

coco.geojson2coco(
    image_src, 
    label_src, 
    output_path, 
    image_type='tif', 
    label_type='geojson', 
    overwrite=False, 
    verbose=False)
"""


from . import data, raster, tile, utils, vector

__version__ = "0.1.0dev0"

__author__ = "Sebastian Haan"
