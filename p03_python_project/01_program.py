def file_backup(file_path, content):
    backup_file=f"{file_path}_bak"
    file_backup=open(backup_file, "w")
    file_backup.writelines(content)

def update_config(file_path, key, value):
    f=open(file_path, "r")
    content=f.readlines()

    file_backup(file_path, content)
    
    with open(file_path, "w") as file:
        for line in content:
            if key in line:
            #if line.startswith(key + "="):  # match exact key 
                file.write(f"{key}={value}\n")
            else:
                file.write(line)


def main():
    config_file="./server.conf"
    key="MAX_CONNECTIONS"
    new_value='1000'
    
    update_config(config_file, key, new_value)

if __name__== "__main__":
    main()
