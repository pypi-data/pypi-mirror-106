# wai-annotations-roi
wai.annotations module for managing object detection annotations using ROI CSV files.

## Plugins
### FROM-ROI-OD
Reads image object-detection annotations in the ROI CSV-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: from-roi-od [-I FILENAME] [-i FILENAME] [-N FILENAME] [-n FILENAME] [--seed SEED] [-e FORMAT FORMAT FORMAT] [--prefix READER_PREFIX] [--suffix READER_SUFFIX]

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
  --prefix READER_PREFIX
                        the prefix for output filenames (default = '')
  --suffix READER_SUFFIX
                        the suffix for output filenames (default = '-rois.csv')
```

### TO-ROI-OD
Writes image object-detection annotations in the ROI CSV-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: to-roi-od [-d WIDTH HEIGHT] [--annotations-only] [--comments COMMENTS [COMMENTS ...]] -o PATH [--size-mode] [--split-names SPLIT NAME [SPLIT NAME ...]] [--split-ratios RATIO [RATIO ...]] [--prefix WRITER_PREFIX] [--suffix WRITER_SUFFIX]

optional arguments:
  -d WIDTH HEIGHT, --image-dimensions WIDTH HEIGHT
                        image dimensions to use if none can be inferred
  --annotations-only    skip the writing of data files, outputting only the annotation files
  --comments COMMENTS [COMMENTS ...]
                        comments to write to the beginning of the ROI file
  -o PATH, --output PATH
                        output directory to write files to
  --size-mode           writes the ROI files with x,y,w,h headers instead of x0,y0,x1,y1
  --split-names SPLIT NAME [SPLIT NAME ...]
                        the names to use for the splits
  --split-ratios RATIO [RATIO ...]
                        the ratios to use for the splits
  --prefix WRITER_PREFIX
                        the prefix for output filenames (default = '')
  --suffix WRITER_SUFFIX
                        the suffix for output filenames (default = '-rois.csv')
```
