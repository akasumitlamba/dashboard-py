from flask import Flask, jsonify, send_from_directory
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('dashboard.db')
    conn.row_factory = sqlite3.Row  # Returns rows as dictionaries
    return conn

@app.route('/')
def serve_dashboard():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM insights')
    rows = cursor.fetchall()
    conn.close()
    
    # Convert rows to list of dictionaries and ensure numeric values
    data = []
    for row in rows:
        row_dict = dict(row)
        try:
            row_dict['intensity'] = int(row_dict['intensity']) if row_dict['intensity'] is not None else None
        except (ValueError, TypeError):
            row_dict['intensity'] = None
        try:
            row_dict['likelihood'] = int(row_dict['likelihood']) if row_dict['likelihood'] is not None else None
        except (ValueError, TypeError):
            row_dict['likelihood'] = None
        data.append(row_dict)
    
    return jsonify(data)

@app.route('/api/filters', methods=['GET'])
def get_filters():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Fetch unique values for filters
    filters = {
        'end_year': [row[0] for row in cursor.execute('SELECT DISTINCT end_year FROM insights WHERE end_year != ""').fetchall()],
        'topics': [row[0] for row in cursor.execute('SELECT DISTINCT topic FROM insights WHERE topic != ""').fetchall()],
        'sectors': [row[0] for row in cursor.execute('SELECT DISTINCT sector FROM insights WHERE sector != ""').fetchall()],
        'regions': [row[0] for row in cursor.execute('SELECT DISTINCT region FROM insights WHERE region != ""').fetchall()],
        'pestle': [row[0] for row in cursor.execute('SELECT DISTINCT pestle FROM insights WHERE pestle != ""').fetchall()],
        'sources': [row[0] for row in cursor.execute('SELECT DISTINCT source FROM insights WHERE source != ""').fetchall()],
        'countries': [row[0] for row in cursor.execute('SELECT DISTINCT country FROM insights WHERE country != ""').fetchall()],
        # Add intensity and likelihood ranges
        'intensity_range': {
            'min': cursor.execute('SELECT MIN(intensity) FROM insights WHERE intensity IS NOT NULL').fetchone()[0] or 0,
            'max': cursor.execute('SELECT MAX(intensity) FROM insights WHERE intensity IS NOT NULL').fetchone()[0] or 100
        },
        'likelihood_range': {
            'min': cursor.execute('SELECT MIN(likelihood) FROM insights WHERE likelihood IS NOT NULL').fetchone()[0] or 0,
            'max': cursor.execute('SELECT MAX(likelihood) FROM insights WHERE likelihood IS NOT NULL').fetchone()[0] or 5
        }
    }
    conn.close()
    return jsonify(filters)

if __name__ == '__main__':
    app.run(debug=True)