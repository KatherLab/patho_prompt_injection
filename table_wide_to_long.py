import pandas as pd

def wide_to_long(input_file, output_file):
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Create an empty list to store the new rows
    new_rows = []

    # Iterate through each row in the original dataframe
    for _, row in df.iterrows():
        # Create three new rows for each original row
        for label_type in ['true', 'false', 'none']:
            new_row = row.copy()
            new_row['Label_Type'] = label_type
            new_rows.append(new_row)

    # Create a new dataframe from the list of new rows
    new_df = pd.DataFrame(new_rows)

    # Reorder columns if needed
    columns_order = [
        'Patient_ID_File_Name', 'Ground_Truth', 'Project_Part', 
        'True_Prompt', 'False_Prompt', 'Study_ID', 'Label_Type'
    ]
    new_df = new_df[columns_order]

    # Save the new dataframe to an Excel file
    new_df.to_excel(output_file, index=False)

    print(f"Transformed data saved to {output_file}")

# Usage
path= "C:/Users/janni/OneDrive/Dokumente/PostDoc/Projects/Patho Prompt Injection/First_Dataset"
input_file = f"{path}/Patient_Metadata_wide.xlsx"
output_file = f"{path}/Patient_Metadata_long.xlsx"

wide_to_long(input_file, output_file)