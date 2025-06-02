import os

def br():
    print("#" * 40)

def list_of_files(folder):
    try:
        files = os.listdir(folder)
        files.sort()  # Sort alphabetically
        return files, None
    except FileNotFoundError:
        return None, f"[ERROR] Folder not found: {folder}"
    except PermissionError:
        return None, f"[ERROR] Permission denied: {folder}"

def main():
    folders = input("Enter folder names separated by spaces: ").split()

    for folder in folders:
        full_path = os.path.abspath(folder)
        br()
        print(f" Folder: {full_path}")
        #br()

        files, error = list_of_files(folder)
        if files:
            print(f" {len(files)} file(s) found:")
            for file in files:
                print(f"   - {file}")
        else:
            print(error or "[INFO] Folder is empty or inaccessible")

if __name__ == "__main__":
    main()

