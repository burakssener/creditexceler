import os
import glob
import pandas as pd

def collect_and_credit_to_excel(folder_path):
    # Get all .txt files recursively in the specified folder
    txt_files = glob.glob(os.path.join(folder_path, '**/*.txt'), recursive=True)

    # Create an empty list to store data
    data = []

    # Extract the folder name for credit
    folder_name = os.path.basename(folder_path)
    credit_text = "\n\nCredit: " + folder_name

    for txt_file in txt_files:
        try:
            # Read the content of the .txt file
            with open(txt_file, "r", encoding="utf-8") as file:
                content = file.read()

            # Add credit text to the content
            content_with_credit = content + credit_text

            # Append data as a tuple (file name, content) to the list
            data.append((txt_file, content_with_credit))
        except UnicodeDecodeError:
            print(f"Error reading file: {txt_file}. Skipping.")

    # Create a DataFrame from the list of data
    df = pd.DataFrame(data, columns=['File Name', 'Content'])

    # Create an Excel file and write the DataFrame to it
    excel_file = os.path.join(folder_path, 'output.xlsx')
    df.to_excel(excel_file, index=False)

# Specify the folder path where your .txt files are located
folder_path = 'C:/Users/burak/Desktop/instaloader/babybearyuki'

# Call the function to collect .txt files, add credit, and save to an Excel file
collect_and_credit_to_excel(folder_path)
