def write_data_to_html(input_file, output_file):
    try:
        # Read the file and process lines
        with open(input_file, "r") as file:
            lines = file.readlines()

        # Start building the HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Command and Description Table</title>
            <style>
                table {
                    width: 80%;
                    margin: 20px auto;
                    border-collapse: collapse;
                }
                table, th, td {
                    border: 1px solid #ddd;
                }
                th, td {
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f4f4f4;
                }
                h1 {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>Command and Description Table</h1>
            <table>
                <tr>
                    <th>Command/Description</th>
                    <th>Details</th>
                </tr>
        """

        # Process each line
        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace

            if not line:  # Skip empty lines
                continue

            if ":" in line:
                # Split lines with a colon into two parts
                command, details = line.split(":", 1)
                html_content += f"""
                <tr>
                    <td>{command.strip()}</td>
                    <td>{details.strip()}</td>
                </tr>
                """
            else:
                # Lines without a colon go in the first column
                html_content += f"""
                <tr>
                    <td>{line}</td>
                    <td></td>
                </tr>
                """

        # Close the HTML tags
        html_content += """
            </table>
        </body>
        </html>
        """

        # Write the HTML content to the output file
        with open(output_file, "w") as file:
            file.write(html_content)

        print(f"Data successfully written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"Error: {str(e)}")


# Input and Output file paths
input_file = "data.txt"
output_file = "prblm3_3.html"

write_data_to_html(input_file, output_file)
