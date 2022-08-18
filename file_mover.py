import os

#before we start, make sure to create a new directory under emotions called val
# and then inside that directory have a directory for each emotion

file_path_base = "/home/nvidia/project/detect_A/"
#We create this variable to prepend to all of our other filepaths because this will
#be the start of every filepath we use.

counter = 0
#The idea here is to go through the training dataset and put every tenth element in the validation dataset

#80% training 10% validation 10% testing

os.mkdir(file_path_base+"train")
os.mkdir(file_path_base+"test")
os.mkdir(file_path_base+"val")

classifications = ['Karolina','package','unrecognized']

for cat in classifications: #we have to do this for every emotion
    os.mkdir(file_path_base+"train/"+cat)
    os.mkdir(file_path_base+"test/"+cat)
    os.mkdir(file_path_base+"val/"+cat)

    for fname in os.listdir(file_path_base+cat): #this goes through the files in the directory
        old_filepath = file_path_base + cat + "/" + fname

        counter += 1
        if counter%10 == 0: #put in testing
            #create new filepath
            new_filepath = file_path_base + "test/" + cat + "/" + fname
        elif counter %10 == 1: #put in validation
            new_filepath = file_path_base + "val/" + cat + "/" + fname
            #create new filepath
        else: #other 80% go in training
            new_filepath = file_path_base + "train/" + cat + "/" + fname
            #create new filepath

        #after setting the old and new filepath, we use os.rename to actually move it
        os.rename(old_filepath,new_filepath)
    print(cat + " done being moved")

