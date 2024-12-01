file_path = "LinuxCommands.txt"

output_html = "output.html"


try:

    with open(file_path, "r") as file:
        lines = file.readlines()

        table_data = [line.strip().split(": ", 1) for line in lines if line.strip()]

    # Start creating the HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Command Table</title>
        <style>
            table {
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #000;
                padding: 8px 12px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">Command and Description Table</h1>
        <table>
            <tr>
                <th>Command</th>
                <th>Description</th>
            </tr>
    """
    for command, description in table_data:
        html_content += f"""
            <tr>
                <td>{command}</td>
                <td>{description}</td>
            </tr>
        """
    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_html, "w") as output_file:
        output_file.write(html_content)

    print("HTMLtable successfully written to {output_html}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
