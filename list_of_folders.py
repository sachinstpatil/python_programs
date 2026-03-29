import os
folders = input("Provide the list of folders separated by space: ").split()

for folder in folders:

    try:
        files = os.listdir(folder) #list the contents of the folder
        #print(f"Contents of folder '{folder}':", files)
    
    
    except FileNotFoundError:
        print(f"Folder '{folder}' not found.")
        #break #break statement to exit the loop if a folder is not found
        continue #continue statement to skip the rest of the loop if a folder is not found
    
    
    except PermissionError:
        print(f"Permission denied for folder '{folder}'.")
        continue #continue statement to skip the rest of the loop if permission is denied
    
    print(f"{folder}:") #print the contents of the folder
    for file in files:
            print(f" - {file}") #print each file in the folder