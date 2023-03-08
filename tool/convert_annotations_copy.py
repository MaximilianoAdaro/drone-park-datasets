import os

import numpy as np
from tqdm import tqdm

width = 1280
height = 720


# function that turns XMin, YMin, XMax, YMax coordinates to normalized yolo format
# noinspection DuplicatedCode
def convert(coords):
    coords[2] -= coords[0]
    coords[3] -= coords[1]
    x_diff = int(coords[2] / 2)
    y_diff = int(coords[3] / 2)
    coords[0] = coords[0] + x_diff
    coords[1] = coords[1] + y_diff
    coords[0] /= width
    coords[1] /= height
    coords[2] /= width
    coords[3] /= height
    return coords


def revert_conversion(coords):
    coords[0] *= width
    coords[1] *= height
    coords[2] *= width
    coords[3] *= height
    y_diff = int(coords[3] / 2)
    x_diff = int(coords[2] / 2)
    coords[1] = coords[1] - y_diff
    coords[0] = coords[0] - x_diff
    coords[3] += coords[1]
    coords[2] += coords[0]
    return coords


# noinspection DuplicatedCode
def main():
    print(1, os.listdir(os.getcwd()))

    dataset_folder = "PUCPR+_devkit"
    annotations_folder = "Annotations"
    output_annotations_folder = "Annotations-output"

    os.chdir("..")
    os.chdir(os.path.join(dataset_folder, "data", annotations_folder))
    print(2, os.listdir(os.getcwd()))

    # for all flies into directory change annotations
    for filename in tqdm(os.listdir(os.getcwd())):
        annotations = get_new_annotations_from_file(filename)

        os.chdir("../..")
        os.chdir(output_annotations_folder)

        write_new_annotations(annotations, filename)

        os.chdir("../..")
        os.chdir(annotations_folder)


def write_new_annotations(annotations, filename):
    with open(filename, "w") as outfile:
        for line in annotations:
            outfile.write(line)
            outfile.write("\n")
        outfile.close()


def get_new_annotations_from_file(filename):
    annotations = []
    with open(filename) as file:
        for line in file:
            labels = line.split()
            coords_old = np.asarray([float(labels[0]), float(labels[1]), float(labels[2]), float(labels[3])])
            coords = convert(coords_old)
            labels[1], labels[2], labels[3], labels[4] = coords[0], coords[1], coords[2], coords[3]
            labels[0] = str(0)  # Only one class
            newline = str(labels[0]) + " " + str(labels[1]) + " " + \
                      str(labels[2]) + " " + str(labels[3]) + " " + str(labels[4])
            line = line.replace(line, newline)
            annotations.append(line)
        file.close()
    return annotations


if __name__ == '__main__':
    main()
