# importing the os module
import os

# defining the main function
def main():

    # making a new directory called MyFIles
    main_directory = "MyFiles"
    os.mkdir(main_directory)

    # list holding the names of the subdirectories
    sub_directories = ['Docs', 'Images', 'Videos']

    # making the subdirectories inside the main directory
    for sub_directory in sub_directories:
        os.mkdir(f"{main_directory}/{sub_directory}")
        print(f"Creating {sub_directory}, inside {main_directory}.")

# calling the main function
main()