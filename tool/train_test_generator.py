import os
import random
import shutil

all_images_file = 'all.txt'
shuffled_file = 'shuffled.txt'
train_file = 'train.txt'
test_file = 'test.txt'


def shuffle_list():
    lines = open(all_images_file, "r").readlines()
    random.shuffle(lines)
    random.shuffle(lines)
    random.shuffle(lines)
    random.shuffle(lines)
    open(shuffled_file, 'w').writelines(lines)


def split_train_test():
    lines = open(shuffled_file, "r").readlines()
    total = len(lines)
    train_amount = int(0.8 * total)
    test_amount = (total - train_amount)

    train = lines[:train_amount]
    print(len(train))
    open(train_file, 'w').writelines(train)

    test = lines[-test_amount:]
    print(len(test))
    open(test_file, 'w').writelines(test)


def copy_images():
    train_file_lines = open(train_file, 'r').readlines()
    test_file_lines = open(test_file, 'r').readlines()
    print(3, os.listdir(os.getcwd()))

    os.chdir("../Images")
    print(4, os.listdir(os.getcwd()))

    # Train files
    for line in train_file_lines:
        filename = line.rstrip() + '.jpg'
        shutil.copy(filename, '../train/' + filename)

    # Test files
    for line in test_file_lines:
        filename = line.rstrip() + '.jpg'
        shutil.copy(filename, '../test/' + filename)


def copy_annotations():
    train_file_lines = open(train_file, 'r').readlines()
    test_file_lines = open(test_file, 'r').readlines()
    print(3, os.listdir(os.getcwd()))

    os.chdir("../Annotations-output")
    print(4, os.listdir(os.getcwd()))

    # Train files
    for line in train_file_lines:
        filename = line.rstrip() + '.txt'
        shutil.copy(filename, '../train/' + filename)

    # Test files
    for line in test_file_lines:
        filename = line.rstrip() + '.txt'
        shutil.copy(filename, '../test/' + filename)


if __name__ == '__main__':
    dataset_folder = "CARPK_devkit"
    # dataset_folder = "PUCPR+_devkit"
    imageSet_folder = "ImageSets"

    os.chdir("..")
    os.chdir(os.path.join(dataset_folder, "data", imageSet_folder))

    # shuffle_list()
    # split_train_test()
    # copy_images()
    copy_annotations()
