# Data Visualization Dashboard

This is a web-based dashboard for visualizing data from a JSON file. It uses Flask (a Python web framework), SQLite (a database), and Chart.js (for charts). You can filter data by categories like year, topic, sector, region, and more, and see the results in interactive bar charts. The dashboard has a modern design with light/dark mode support.

## Setup Instructions

### 1. Clone the Repository
Clone the project to your computer:
git clone https://github.com/akasumitlamba/dashboard_project.git
cd dashboard_project

### 2. Install Dependencies
Install the required Python packages:
pip install -r requirements.txt

### 3. Generate the Database (optional if no new data)
Create the database from the JSON file:
python load_data.py

### 4. Run the Application
Start the Flask server:
python app.py

### 5. Access the Dashboard
Open your browser and go to:
http://127.0.0.1:5000
You should see the dashboard with filters and charts.

## PREVIEW

![image](https://github.com/user-attachments/assets/c944a49a-e95b-4922-88e1-1d6e74db60a6)

