# wai-annotations-coco
wai.annotations module for dealing MSCOCO object detection file formats.

## Plugins
### FROM-COCO-OD
Reads image object-detection annotations in the MS-COCO JSON-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: from-coco-od [-I FILENAME] [-i FILENAME] [-N FILENAME] [-n FILENAME] [--seed SEED]

optional arguments:
  -I FILENAME, --inputs-file FILENAME
                        Files containing lists of input files (can use glob syntax)
  -i FILENAME, --input FILENAME
                        Input files (can use glob syntax)
  -N FILENAME, --negatives-file FILENAME
                        Files containing lists of negative files (can use glob syntax)
  -n FILENAME, --negative FILENAME
                        Files that have no annotations (can use glob syntax)
  --seed SEED           the seed to use for randomisation
```

### TO-COCO-OD
Writes image object-detection annotations in the MS-COCO JSON-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: to-coco-od [--annotations-only] [--categories CATEGORY [CATEGORY ...]] [--category-output-file FILENAME] [--default-supercategory SUPERCATEGORY] [--error-on-new-category] [--license-name LICENSE_NAME] [--license-url LICENSE_URL] -o PATH [--pretty] [--sort-categories] [--split-names SPLIT NAME [SPLIT NAME ...]] [--split-ratios RATIO [RATIO ...]]

optional arguments:
  --annotations-only    skip the writing of data files, outputting only the annotation files
  --categories CATEGORY [CATEGORY ...]
                        defines the order of the categories
  --category-output-file FILENAME
                        file to write the categories into, as a simple comma-separated list
  --default-supercategory SUPERCATEGORY
                        the supercategory to use for pre-defined categories
  --error-on-new-category
                        whether unspecified categories should raise an error
  --license-name LICENSE_NAME
                        the license of the images
  --license-url LICENSE_URL
                        the license of the images
  -o PATH, --output PATH
                        output file to write annotations to (images are placed in same directory)
  --pretty              whether to format the JSON annotations file with indentation
  --sort-categories     whether to put the categories in alphabetical order
  --split-names SPLIT NAME [SPLIT NAME ...]
                        the names to use for the splits
  --split-ratios RATIO [RATIO ...]
                        the ratios to use for the splits
```
