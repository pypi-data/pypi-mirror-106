# wai-annotations-vgg
wai.annotations module for managing VGG object detection annotations.

## Plugins
### FROM-VGG-OD
Reads image object-detection annotations in the VGG JSON-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: from-vgg-od [-I FILENAME] [-i FILENAME] [-N FILENAME] [-n FILENAME] [--seed SEED]

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

### TO-VGG-OD
Writes image object-detection annotations in the VGG JSON-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: to-vgg-od [--annotations-only] -o PATH [--pretty] [--split-names SPLIT NAME [SPLIT NAME ...]] [--split-ratios RATIO [RATIO ...]]

optional arguments:
  --annotations-only    skip the writing of data files, outputting only the annotation files
  -o PATH, --output PATH
                        output file to write annotations to (images are placed in same directory)
  --pretty              whether to format the JSON annotations file with indentation
  --split-names SPLIT NAME [SPLIT NAME ...]
                        the names to use for the splits
  --split-ratios RATIO [RATIO ...]
                        the ratios to use for the splits
```
