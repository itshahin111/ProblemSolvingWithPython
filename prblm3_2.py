from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def display_table():
    input_file = "data.txt"  # Path to your data file

    try:
        # Read the file and process lines
        with open(input_file, "r") as file:
            lines = file.readlines()

        table_data = []
        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace

            if not line:  # Skip empty lines
                continue

            if ":" in line:
                # Split lines with a colon into two parts
                command, details = line.split(":", 1)
                table_data.append((command.strip(), details.strip()))
            else:
                # Lines without a colon go in the first column
                table_data.append((line, ""))

        # HTML template for rendering
        html_template = """
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
                {% for command, details in table_data %}
                <tr>
                    <td>{{ command }}</td>
                    <td>{{ details }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
        </html>
        """

        # Render the template with the data
        return render_template_string(html_template, table_data=table_data)

    except FileNotFoundError:
        return "<h1 style='color:red; text-align:center;'>File not found: data.txt</h1>"
    except Exception as e:
        return f"<h1 style='color:red; text-align:center;'>Error: {str(e)}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
