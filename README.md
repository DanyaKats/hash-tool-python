# hash-tool-python

After learning about hashes in my university lecture, I thought that I should make a program that incorporates this into actual file tracking and logging.
Here is the result:

A python script for getting SHA 256 hashes of files, creating logs of hashes to automatically track changes to the file and checking these logs to find differences in hashes for files.

This script stores logs in a local txt file named logs.txt in the scripts directory, it also stores hashes in a local hashes.txt file. If these files don't exist it will create them automatically.

The script features 3 modes and an exit:
Modes:
          getfilehash - gets a file hash
          log - logs file hashes in a file every specified amount of seconds
          checklog - checks logs file to see if the hash of a file has been changed
          exit - exits the script


getfilehash asks for user input for a file path on their computer. If it cannot find this it automatically returns to the main menu. The hash is created using Hashlib and is SHA 256. This hashes the contents of the file. It then outputs the file name and hash in a file_name: hash format to hashes.txt in the scripts directory. This is used for manual hash logging.

log mode is more interesting, it asks for user input for a file path on their computer. It then records the current time in year-mm-dd and time format, the name of the file and the hash of the file in a logs.txt text file. The user chooses how often the logs are saved in seconds. It can stay running for as long as you want. When changes are recorded to the file, the hash changes which allows you to track data integrity. How do we track these changes? Let's move on to the next mode.

checklog mode takes the file path of the logs.txt file. It separates the file names and hashes and adds them to an array. It asks whether you want to track just one file within the logs.txt file or all changes that have been made to all files. It then checks for difference in hashes between files to output where the difference is and at what time it was logged. This integrates nicely with the previous log mode to easily search for changes in data integrity in a file's lifespan.

exit simply exits the script.

To exit log mode, you must stop the program entirely, as I do not know of a way to allow the user to input an exit message whilst also logging what changes were made to the log file, since python goes line by line and waits for you to type in an input, while stopping the logging of changes.

This script can monitor the changes to basically any file or get their file hashes.

Integrating this script could allow a business to monitor changes to certain files to preserve data integrity, switching the logs.txt file for an off-site, secure file where it cannot be accessed by or changed by typical employees and running it in the background on files where data integrity is critical.

Example usage:
I want to check the logs of my log file with which I previously logged a couple different files. I only want to know the differences of one, hash_this.txt. I ran the script for around 2 minutes and made 3 changes. One where I added data, changing it once. Adding more data, changing it twice. And then reverting to the old data, changing it another time.

My script automatically tracks these changes and points out at what time my file was changed:
<img width="807" height="488" alt="image" src="https://github.com/user-attachments/assets/dcb7cef1-98c3-4bf5-9e0f-0dae14e63d24" />

