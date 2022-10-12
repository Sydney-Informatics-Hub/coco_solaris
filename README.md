# Generate COCO-formatted labels from one or multiple geojsons and images

Coco_solaris is a refactored and slimmed-down version of the package solaris, with a focus on conversion of geojson and image file to COCO format.

The original package, Solaris, is a collection of tools for converting data to and from the COCO format, however it cannot be installed on some of the latest operating systems due to fixed dependencies on older tensorflow, torch and other libraries.


## Installation

```bash
conda env create -f environment.yml
conda activate coco_solaris
```

## Usage

For a complete example see notebook `json2coco.ipynb`.

It is advised that both input files, geojson and tif image, are in the same coordinate reference system (crs).

The COCO dictionary is gnererated as:
```python
from coco_solaris.data import coco
coco_dict = coco.geojson2coco(image_name, json_name)
```

## Syntax

The coco_solaris.data.coco.geojson2coco() takes the following arguments:

`image_src`: a str or list or dict defining source image(s) to use in the dataset. These are required not only to list as part of the dataset, but also to convert georegistered labels to pixel coordinates. This argument can be:


1. a string path to an image (e.g. `"path/to/a/geotiff.tif"`)
2. the path to a directory containing a bunch of images (e.g. `"/path/to/geotiff/dir/"`)
3. a list of image paths (e.g. `["path/to/geotiff_1.tif", "path/to/geotiff_2.tif"]`)
4. a dictionary corresponding to COCO-formatted image records (e.g.
[
    {
      "id": 1,
      "file_name": "path/to/geotiff.tif",
      "height": 640,
      "width": 640,
    },
    {etc.}
]
5. a string path to a COCO JSON containing image records (e.g. `"path/to/coco_dataset.json"`)

If `image_src` is a directory, the recursive flag will be used to determine whetheror not to descend into sub-directories.

`label_src`: str or list of source labels to use in the dataset. This can be a string path to a geojson, the path to a directory containing multiple geojsons, or a list of geojson file paths. If a directory, the recursive flag will determine whether or not to descend into sub-directories.

`output_path` : an optional str path to save the JSON-formatted COCO records to. If not provided, the records will only be returned as a dict, and not saved to file.

`image_ext`: The string extension to use to identify images when searching directories. Only has an effect if image_src is a directory path. Defaults to ".tif".

`matching_re` : A regular expression pattern to match filenames between image_src and label_src if both are directories of multiple files. This has no effect if those arguments do not both correspond to directories or lists of files. If this isn’t provided, it is assumed that label filenames and image filenames differ only in their extensions, and filenames will be compared for identity to find matches.

`category_attribute`: The str name of an attribute in the geojson that specifies which category a given instance corresponds to. If not provided, it’s assumed that only one class of object is present in the dataset, which will be termed "other" in the output json.

`preset_categories`: An optional pre-set list of dicts of categories to use for labels. These categories should be formatted per the COCO category specification.

`include_other`: A boolean which, if set to True, and preset_categories is provided, causes objects that don’t fall into the specified categories to be kept in the dataset. They will be passed into a category named "other" with its own associated category id. If False, objects whose categories don’t match a category from preset_categories will be dropped.

`info_dict`: An optional dict with the following key-value pairs:

"year": int year of creation

"version": str version of the dataset

"description": str string description of the dataset

"contributor": str who contributed the dataset

"url": str URL where the dataset can be found

"date_created": datetime.datetime when the dataset was created

If `info_dict` isn’t provided, it will be left out of the .json created by solaris.

`license_dict`: An optional dict containing the licensing information for the dataset, with the following key-value pairs:

"name": str the name of the license.

"url": str a link to the dataset’s license.

Note: This implementation assumes that all of the data uses one license. If multiple licenses are provided, the image records will not be assigned a license ID.

`recursive`: If image_src and/or label_src are directories, setting this flag to True will induce solaris to descend into subdirectories to find files. By default, solaris does not traverse the directory tree.

`verbose` : Verbose text output. By default, none is provided; if True or 1, information-level outputs are provided; if 2, extremely verbose text is output.

## Attribution and Acknowledgments

This software was developed by the Sydney Informatics Hub, a core research facility of the University of Sydney, as part of the Data Harvesting project for the Agricultural Research Federation (AgReFed).

Acknowledgments are an important way for us to demonstrate the value we bring to your research. Your research outcomes are vital for ongoing funding of the Sydney Informatics Hub.

If you make use of this software for your research project, please include the following acknowledgment:

“This research was supported by the Sydney Informatics Hub, a Core Research Facility of the University of Sydney."

## Contributors

Author: Sebastian Haan