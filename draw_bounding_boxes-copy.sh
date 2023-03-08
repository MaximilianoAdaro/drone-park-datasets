# Draw PUCPR+ ground truth bounding boxes
ipython ./tool/draw_bounding_boxes-copy.py -- --annots_dir ./PUCPR+_devkit/data/Annotations-output/ --images_dir ./PUCPR+_devkit/data/Images/ --output_dir ./output_images/copy/PUCPR+/

# Draw CARPK ground truth bounding boxes
ipython ./tool/draw_bounding_boxes-copy.py -- --annots_dir ./CARPK_devkit/data/Annotations-output/ --images_dir ./CARPK_devkit/data/Images/ --output_dir ./output_images/copy/CARPK/

# Draw test_copy ground truth bounding boxes
ipython ./tool/draw_bounding_boxes-copy.py -- --annots_dir ./test_copy/data/Annotations-output/ --images_dir ./test_copy/data/Images/ --output_dir ./output_images/copy/test_copy/
