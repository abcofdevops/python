import os
def br():
    print("#" * 40)

def list_of_files(folder):
    try:
        files=os.listdir(folder)
        return files, None 
    except FileNotFoundError:
        return None, f"Error!!!!\nThis folder {folder} does not exist.\nPlease provide a valid folder name"
    except PermissionError:
        return None, f"Error!!!!\nYou dont have permission to access the {folder} folder"


def main():
    folders = input("Please provide list of folders [names with spaces in between]: ").split()
    for folder in folders:
        br()
        print(folder)
        br()

        files, message = list_of_files(folder)
        if files:
            for file in files:
                print(file)
        else:
            print(message or "[INFO] Folder is empty or inaccessible")

if __name__ == "__main__":
    main()
