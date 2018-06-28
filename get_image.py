# Sort out (get) images based on how many objects are in there

# Get the csv file
import pandas as pd
import os
import shutil
dataset = pd.read_csv("detected_object.csv")


# Get an image that has at least one "jack"
# Here, two conditions are specified: that image should have one "ace" and no "queen"
# You can add more conditions if you need to 
object_name1 = "jack"
number_object1 = 1

object_name2 = "queen"
number_object2 = 0

# Create a folder with the conditions name
image_folder_name = "target_images/" + object_name1 + ">=" + str(number_object1) + "_" + object_name2 + "=" + str(number_object2)
if not os.path.exists(image_folder_name):    
    os.makedirs(image_folder_name)

# Get the image name based on the criteria
conditions = (dataset[object_name1] >= number_object1) & (dataset[object_name2] == number_object2)
targeted_images_list = dataset["image"][conditions].tolist()

# Copy corresponded images to the created folder
for targeted_image in targeted_images_list:
    src_dir = "target_images/" + targeted_image
    shutil.copy(src_dir, image_folder_name)



