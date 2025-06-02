import os
def br():
    print("###################################")
folders = input("Please provide list of folders [names with spaces in between]: ").split()
for folder in folders:
    try:
        br()
        print(folder)
        br()
        files=os.listdir(folder)
    except FileNotFoundError:
        print(f"Error!!!!\nThis folder {folder} does not exist.\nPlease provide a valid folder name")
        continue
    except PermissionError:
        print(f"Error!!!!\nYou dont have permission to access the {folder} folder")
        continue
    for file in files:
        print(file)
        

