import pandas as pd
import re

# List of common pronouns that should be replaced by "SM"
pronoun_list = [
    "he", "she", "man", "him", "her", "woman", "his", "hers", "men", "women", "guy",
    "himself", "stud", "brother", "brotherhood", "girl", "boy", "dude"
]

# Function to replace pronouns in the specified column
def change_pronouns(input_file, output_file, column_name, pronoun_list):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Check if the specified column exists
    if column_name not in df.columns:
        print(f"Error: The column '{column_name}' does not exist in the file.")
        return
    
    # Build a regular expression pattern to match the pronouns
    pronoun_pattern = r'\b(?:' + '|'.join(map(re.escape, pronoun_list)) + r')\b'

    # Function to replace pronouns with "SM"
    def replace_pronouns(text):
        if isinstance(text, str):  
            return re.sub(pronoun_pattern, 'SM', text, flags=re.IGNORECASE)
        return text  

    # Apply the function to the specified column
    df[column_name] = df[column_name].apply(replace_pronouns)
    
    # Export the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"File has been updated and saved as {output_file}")

# Example usage
input_file = '~/Desktop/pdif peer feedback 2 excel report 1737063746924.csv'  # The path to your input CSV file
output_file = '~/Desktop/output_file.csv'  # The path where the updated CSV should be saved
column_name = 'Comment'  # The name of the column containing pronouns

change_pronouns(input_file, output_file, column_name, pronoun_list)
