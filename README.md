Streamlit CSV Manager with Email Notification
Overview
This Streamlit app allows users to upload and manage a CSV file (GFF_March_2025.csv). The app includes features such as displaying data, filtering and downloading a filtered version of the file, deleting specific rows, and sending email notifications with a date-wise summary of the filtered data.

Features
Upload CSV File: Upload a CSV file (GFF_March_2025.csv) to load data into the app.

Display CSV Data: Display the contents of the uploaded CSV file.

Download with Filters: Filter data by Order Date and Restaurant Name, and download the filtered CSV.

Delete Filtered Records: Delete rows that match the chosen filters.

Email Notification: Send an email with a summary of the filtered data, including total orders and amounts by Order Date.

Prerequisites
Make sure you have the following installed:

Python 3.7+

Streamlit

pandas

Install the dependencies required with:

bash
Copy
Edit
pip install streamlit pandas
How to Run
Clone or download this repository.

Go to the project directory in your terminal.

Execute the following command to run the app:

bash
Copy
Edit
streamlit run app.py
Open the app in your browser at the URL displayed in the terminal.

File Structure
bash
Copy
Edit
.
├── app.py                # Main Streamlit app file
├── GFF_March_2025.csv    # CSV file with data
├── requirements.txt      # Dependencies list
└── README.md             # Project description and usage
Code Explanation
app.py: The central code that creates the Streamlit app, processes file upload, shows the CSV data, includes filtering, deletion, and email functionality.

GFF_March_2025.csv: The CSV file holding the data to be processed.

requirements.txt: A list of Python libraries needed to execute the app.

Usage
Upload a CSV: Upload a CSV file with the required data (e.g., GFF_March_2025.csv).

Filter by Date or Restaurant: Filter the data by Order Date or Restaurant Name using the dropdowns.

Download Filtered Data: Download the filtered data as a new CSV file.

Delete Data: Remove the rows that have the currently selected filters.

Send Email Summary: Send an email containing a summary of the filtered data, i.e., total orders and amounts. 

License
This project is licensed under the MIT License - see the LICENSE file for details.
