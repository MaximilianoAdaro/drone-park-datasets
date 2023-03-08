# Draw PUCPR+ ground truth bounding boxes
ipython ./tool/draw_bounding_boxes.py -- --annots_dir ./PUCPR+_devkit/data/Annotations/ --images_dir ./PUCPR+_devkit/data/Images/ --output_dir ./output_images/original/PUCPR+/

# Draw CARPK ground truth bounding boxes
ipython ./tool/draw_bounding_boxes.py -- --annots_dir ./CARPK_devkit/data/Annotations/ --images_dir ./CARPK_devkit/data/Images/ --output_dir ./output_images/original/CARPK/

# Draw PUCPR+ ground truth bounding boxes
ipython ./tool/draw_bounding_boxes.py -- --annots_dir ./test_copy/data/Annotations/ --images_dir ./test_copy/data/Images/ --output_dir ./output_images/original/test_copy/
