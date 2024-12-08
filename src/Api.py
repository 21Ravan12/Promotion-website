from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('MyDataBase.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api', methods=['POST'])
def student_signin():
    try:
        data = request.json
        if not all(field in data for field in ('name', 'surname', 'phone','email','tree','region','donation')):
            return jsonify({"message": "Missing required fields!"}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (name,surname,phone,email,tree,region,donation,suggestions) VALUES (?, ?, ?,?, ?, ?,?, ?)",
                       (data['name'], data['surname'], data['phone'],data['email'], data['tree'], data['region'],data['donation'], data['suggestions']))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Success!"}), 201
    except sqlite3.Error as e:
        return jsonify({"message": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
