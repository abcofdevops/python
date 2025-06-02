import os
def br():
    print("###################################")

def list_of_files(folder):
    try:
        files=os.listdir(folder)
        return files 
    except FileNotFoundError:
        print(f"Error!!!!\nThis folder {folder} does not exist.\nPlease provide a valid folder name")
    except PermissionError:
        print(f"Error!!!!\nYou dont have permission to access the {folder} folder")


def main():
    folders = input("Please provide list of folders [names with spaces in between]: ").split()
    for folder in folders:
        br()
        print(folder)
        br()

        files = list_of_files(folder)
        if files is not None:
            for file in files:
                print(file)

main()
