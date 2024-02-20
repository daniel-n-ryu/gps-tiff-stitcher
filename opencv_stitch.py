import os
import numpy as np
import cv2
import time

# Directory should be a string of the local path to the directory where the tif files are stored

def get_image_paths(directory):
    """
    Directory: a string of the local path to the directory where the tif files are stored
    Return: an array of filenames in directory as strings
    """
    files = []
    for filename in os.listdir(directory):
        # print(filename)
        files.append("activations_tif/" + filename)
    return files


def stitch_images(image_paths):
    """
    Stitches the provided images using OpenCV's stitching method in SCANS mode
    Return: the stitched image if successful as an array of arrays, returns None if not.
    """
    # Read the images
    images = [cv2.imread(path) for path in image_paths]

    # Create the stitcher. Default mode for composing scans. Affine estimator
    stitcher = cv2.Stitcher_create(mode=cv2.Stitcher_SCANS)
    # Stitch the images
    status, stitched = stitcher.stitch(images)

    # Check if stitching was successful
    if status == cv2.Stitcher_OK:
        return stitched
    else:
        print(f"Stitching failed with error code {status}")
        return None

# time1 = time.time()
# tif_files = get_image_paths("activations_tif")
tif_files = get_image_paths("activations_tif")
stitched_image = stitch_images(tif_files)
time2 = time.time()
# print(time2 - time1)

if stitched_image is not None:
    # # Display or save the stitched image. Used for debugging
    # cv2.imshow("Stitched Image", stitched_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Save the stitched image
    cv2.imwrite("stitched_image.tif", stitched_image)
    