from openpyxl import load_workbook


def format_excel_columns(file_path, sheet_name):
    # Load the workbook and select the sheet
    workbook = load_workbook(file_path)
    sheet = workbook[sheet_name]

    # Define the formatting rules for each column
    format_rules = {
        "A": "'company_name' => '{}',",
        "B": "'phone' => '{}',",
        "C": "'email' => '{}',",
        "D": "'website' => '{}',",
    }

    # Apply the formatting rules
    for col_letter, format_rule in format_rules.items():
        for cell in sheet[col_letter]:
            if cell.value:  # Check if the cell is not empty
                # Format the cell value
                cell.value = format_rule.format(cell.value)

    # Save the workbook
    workbook.save(file_path)
    print(f"Columns A, B, C, and D in sheet '{sheet_name}' have been updated.")


# Example usage
file_path = "BaccoData.xlsx"  # Path to your Excel file
sheet_name = "Sheet1"  # Name of the sheet to modify

format_excel_columns(file_path, sheet_name)
