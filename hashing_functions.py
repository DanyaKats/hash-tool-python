from hashlib import sha256
from pathlib import Path
import time

def clear():
    print("\n" * 50)
def compute_file_hash(file_path):
    hash_sha256 = sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def getfilehash():
    clear()
    while True:
        file_path = input("Enter file path (or exit): ")
        if file_path.lower() == "exit":
            main_menu()
        try:
            filename = Path(file_path).name
            hash1 = compute_file_hash(file_path)
            print("SHA-256 Hash: ", hash1)
            with open("hashes.txt", "a") as hashes:
                hashes.write(f"{filename}: {hash1}\n")
                print("Successfully wrote to file")
        except Exception as e:
            print(f"Error ({e})! Returning to main menu..")
            time.sleep(3)
            main_menu()

def logmode():
    clear()
    while True:
        try:
            time_input = int(input("Enter delay between log recordings in seconds: "))
            file_path = input("Enter file path of file that you want to log changes of: ")
            filename = Path(file_path).name
            while True:
                hash2 = compute_file_hash(file_path)
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                with open("logs.txt", "a") as log:
                          log.write(f"Time: {current_time} | File_name: {filename} | Hash: {hash2}\n")
                          print(f"Wrote this to file: Time: {current_time} | File_name: {filename} | Hash: {hash2}\n")
                time.sleep(time_input)
        except Exception as e:
            print("Error ({e})! Returning to main menu..")
            time.sleep(3)
            main_menu()
        
def check_logs():
    while True:
        try:
            log_list = []
            file_path = input("Enter file path of log file: ")
            filename = Path(file_path).name
            with open(file_path, "r") as file:
                for line in file:
                    clean_line = line.strip()
                    if not clean_line:
                        continue

                    entry = {}
                    parts = clean_line.split(" | ")
                    for part in parts:
                        key, value = part.split(": ", 1)
                        entry[key] = value
                    log_list.append(entry)
            print("Checking hashes...")
            name_storage = log_list[0]["File_name"]
            hash_storage  = log_list[0]["Hash"]
            differences = 0
            user_option = input("Only track one file or all? (one/all)")

            
            if user_option.lower() == "all":
                for log in log_list:
                    if log["File_name"] == name_storage and log["Hash"] != hash_storage:
                        differences += 1
                        print(f"One difference found at {log["Time"]}, file name {log["File_name"]}")
                    name_storage = log["File_name"]
                    hash_storage = log["Hash"]
                print(f"In total, {differences} differences found.")
                if differences > 0:
                    print("Your files have been changed, data may have been tampered with, added to, or removed.")
                elif differences == 0:
                    print("Your files have not changed within the time specified in the logs file.\n")


                    
            elif user_option.lower() == "one":
                file_name_input = input("Enter the name of the file you want to track")
                for log in log_list:
                    if log["File_name"] == name_storage and log["Hash"] != hash_storage and log["File_name"] == file_name_input:
                        differences += 1
                        print(f"One difference found at {log["Time"]}, file name {log["File_name"]}")
                    name_storage = log["File_name"]
                    hash_storage = log["Hash"]
                print(f"In total, {differences} differences found.")
                if differences > 0:
                    print("Your file has been changed, data may have been tampered with, added to, or removed.")
                elif differences == 0:
                    print("Your file was not changed within the time specified in the logs file.\n")






                
            print("Return to main menu? (Y/N)")
            user_input = input("")
            if user_input.lower() == "y":
                main_menu()

                
        except Exception as e:
            print(f"Error ({e})! Returning to main menu..")
            main_menu()
            


def main_menu():
    clear()
    print("Welcome to the main menu.")
    print("This python script uses SHA-256 Hashing.")
    print("""Modes:
          getfilehash - gets a file hash\n
          log - logs file hashes in a file every specified amount of seconds\n
          checklog - checks logs file to see if the hash of a file has been changed\n
          exit - exits the script
          """)
    mode = input("Enter mode: ")
    if mode.lower() == "getfilehash":
        getfilehash()
    elif mode.lower() == "log":
        logmode()
    elif mode.lower() == "checklog":
        check_logs()
    elif mode.lower() == "exit":
        exit

main_menu()


