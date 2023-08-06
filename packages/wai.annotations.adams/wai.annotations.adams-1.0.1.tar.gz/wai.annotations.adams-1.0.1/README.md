# wai-annotations-adams
wai.annotations module for ADAMS-related formats.

## Plugins
### FROM-ADAMS-IC
Reads image classification annotations in the ADAMS report-format

#### Domain(s):
- **Image Classification Domain**

#### Options:
```
usage: from-adams-ic [-I FILENAME] [-i FILENAME] [-N FILENAME] [-n FILENAME] [--seed SEED] [-e FORMAT FORMAT FORMAT] -c FIELD

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
  -e FORMAT FORMAT FORMAT, --extensions FORMAT FORMAT FORMAT
                        image format extensions in order of preference
  -c FIELD, --class-field FIELD
                        the report field containing the image class
```

### FROM-ADAMS-OD
Reads image object-detection annotations in the ADAMS report-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: from-adams-od [-I FILENAME] [-i FILENAME] [-N FILENAME] [-n FILENAME] [--seed SEED] [-e FORMAT FORMAT FORMAT] [-p PREFIXES [PREFIXES ...]]

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
  -e FORMAT FORMAT FORMAT, --extensions FORMAT FORMAT FORMAT
                        image format extensions in order of preference
  -p PREFIXES [PREFIXES ...], --prefixes PREFIXES [PREFIXES ...]
                        prefixes to parse
```

### TO-ADAMS-IC
Writes image classification annotations in the ADAMS report-format

#### Domain(s):
- **Image Classification Domain**

#### Options:
```
usage: to-adams-ic -c FIELD [--annotations-only] -o PATH [--split-names SPLIT NAME [SPLIT NAME ...]] [--split-ratios RATIO [RATIO ...]]

optional arguments:
  -c FIELD, --class-field FIELD
                        the report field containing the image class
  --annotations-only    skip the writing of data files, outputting only the annotation files
  -o PATH, --output PATH
                        output directory to write files to
  --split-names SPLIT NAME [SPLIT NAME ...]
                        the names to use for the splits
  --split-ratios RATIO [RATIO ...]
                        the ratios to use for the splits
```

### TO-ADAMS-OD
Writes image object-detection annotations in the ADAMS report-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: to-adams-od [--annotations-only] -o PATH [--split-names SPLIT NAME [SPLIT NAME ...]] [--split-ratios RATIO [RATIO ...]]

optional arguments:
  --annotations-only    skip the writing of data files, outputting only the annotation files
  -o PATH, --output PATH
                        output directory to write files to
  --split-names SPLIT NAME [SPLIT NAME ...]
                        the names to use for the splits
  --split-ratios RATIO [RATIO ...]
                        the ratios to use for the splits
```
