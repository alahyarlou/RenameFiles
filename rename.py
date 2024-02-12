import os


def rename_files_with_names_from_text(text_file_path, folder_path):
    try:
        # Read names from the text file
        with open(text_file_path, 'r', encoding='UTF8') as file:
            names = file.read().splitlines()

        # Get list of files in the folder
        files = os.listdir(folder_path)

        # Make sure the number of names matches the number of files
        if len(names) != len(files):
            print("Number of names doesn't match the number of files.")
            return

        # Rename files
        for name, file_name in zip(names, files):
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, name)

            os.rename(old_file_path, f"{new_file_path}.mp4")

            print(f"File '{file_name}' renamed to '{name}'.")

        print("All files renamed successfully.")

    except FileNotFoundError:
        print("File or folder not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


text_file_path = input('text file path: ')
folder_path = input('folder path: ')

rename_files_with_names_from_text(text_file_path, folder_path)
