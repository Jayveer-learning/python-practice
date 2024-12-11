import requests
import os

# creating folder (directory) using the os module or pathlib for working with file path

# here we creating file using os module

# todo:- Yes, you can create a folder using both the os module and 
# the pathlib module in Python.

# define the folder name

# folder_name = "leslie_Burke_Gallery"

# Create the folder (if it doesn't already exist)

# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)
#     print(f"Folder: {folder_name} created succesfully.")
# else:
#     print(f"Folder {folder_name} already exists.")


def CreateFolder(folder_name: str = "leslie_Burke_Gallery") -> None:
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder: {folder_name} is created successfully.")
        else:
            print(f"Folder {folder_name} already exists.")
    except Exception as e:
        print(f"An error occurred in CreateFolder function: {e}")


def imageDownload(url: str, file_name: str = "leslie_Burke_cute_photo", folder_name: str = "leslie_Burke_Gallery") -> None:
    try:
        # Ensure the folder exists before downloading the image
        CreateFolder(folder_name) # why we call :- reason if folder doesn't exist The folder is created automatically
        # -> Calling the createFolder fun and pass the imageDownload parameter folder_name as argument.
        
        response = requests.get(url)
        file_name_data = file_name + ".jpg"

        # Construct the full file path -> folder_name/file_name_data
        full_file_path = os.path.join(folder_name, file_name_data)

        if os.path.exists(full_file_path): #-> ckecking if file in folder
            print(f"Image '{file_name_data}' is already in folder '{folder_name}'.")
            return # Exits the function if the file already exists


        elif response.status_code == 200 and "image" in response.headers['Content-type']:
            # Using os: os.path.join() is used to construct the full path.
            with open(os.path.join(folder_name, file_name_data), "wb") as download_image:
                download_image.write(response.content) # -> response.content add only 
                # content of response not other information like status header 
                # like that.
                print(f"File {file_name} added to {folder_name} successfully")
        else:
            print(f"Failed to download this image {response.status_code}")
    except Exception as e:
        print(f"An error occurred in imageDownload function: {e}")

# # imageDownload("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm126GIY51zHOTGdPz-ebF_5tgZoztJgohbQ&s", "leslie_Burke_cute_photo")
# # imageDownload("https://miro.medium.com/v2/resize:fit:700/1*iYUeWwFhLwKL7Zzp3wDiWQ.jpeg", "leslie_Burke_best_scene")
# # imageDownload("https://i.pinimg.com/474x/d0/89/0e/d0890e7c2d2cab8f4082091edaff52d4.jpg", "leslie_Burke_memory")
imageDownload("https://i.pinimg.com/550x/a6/22/7e/a6227e7c995c773e422943078904f832.jpg", "leslie_burke_forest")



#? code discreption :

# CreateFolder(folder_name) # why we call :- reason if folder doesn't exist The folder is created automatically

        # but how folder id create we write creation code in CreateFolder and we call the fun. in imageDowload 
        # or imageDonload we create parameter name is folder_name and set defult value do if the folder value if not 
        # not passed in arg so imgDownload parameter value pass in createFolder all we give two to pass the folder 
        # name first in CreateFolder parameter name is folder_name and alos we create one parameter in imageDownload name
        # is folder_name so we can give arg of folder name is two place.













# chat gpt code

# import os
# import requests

# # Function to create a folder if it doesn't exist
# def CreateFolder(folder_name: str = "leslie_Burke_Gallery") -> None:
#     try:
#         if not os.path.exists(folder_name):
#             os.makedirs(folder_name)
#             print(f"Folder: {folder_name} is created successfully.")
#         else:
#             print(f"Folder {folder_name} already exists.")
#     except Exception as e:
#         print(f"An error occurred in CreateFolder function: {e}")

# # Function to download an image
# def imageDownload(url: str, file_name: str, folder_name: str = "leslie_Burke_Gallery") -> None:
#     try:
#         CreateFolder(folder_name)

#         # Construct the full file path and file name
#         file_name_data = file_name + ".jpg"
#         full_file_path = os.path.join(folder_name, file_name_data)

#         # Check if the image is already downloaded by checking the history file
#         if image_already_downloaded(file_name_data):
#             print(f"Image '{file_name_data}' is already downloaded.")
#             return

#         # Download the image
#         response = requests.get(url)
#         if response.status_code == 200 and "image" in response.headers['Content-Type']:
#             with open(full_file_path, "wb") as download_image:
#                 download_image.write(response.content)
#                 print(f"File {file_name} added to {folder_name} successfully")
            
#             # Record the downloaded image
#             record_downloaded_image(file_name_data)
#         else:
#             print(f"Failed to download this image {response.status_code}")
#     except Exception as e:
#         print(f"An error occurred in imageDownload function: {e}")

# # Function to check if an image has already been downloaded
# def image_already_downloaded(file_name: str, history_file: str = "download_history.txt") -> bool:
#     if os.path.exists(history_file):
#         with open(history_file, "r") as f:
#             if file_name in f.read():
#                 return True
#     return False

# # Function to record the downloaded image in the history file
# def record_downloaded_image(file_name: str, history_file: str = "download_history.txt") -> None:
#     with open(history_file, "a") as f:
#         f.write(file_name + "\n")


# # Call the function to download images only once, and they won't be downloaded again.
# imageDownload("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm126GIY51zHOTGdPz-ebF_5tgZoztJgohbQ&s", "leslie_Burke_cute_photo")
# imageDownload("https://miro.medium.com/v2/resize:fit:700/1*iYUeWwFhLwKL7Zzp3wDiWQ.jpeg", "leslie_Burke_best_scene")