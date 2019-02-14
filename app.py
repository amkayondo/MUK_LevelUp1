from flask import Flask, request, jsonify
from db import DatabaseConnection

app = Flask(__name__)

@app.route('/students')
def get_all_students():
	db = DatabaseConnection()
	students = db.get_students()
	response = {
	"Students": students
	}
	return jsonify(response), 200

@app.route('/students', methods=['POST'])
def add_student():
	data = request.get_json()

	name = data.get('name')
	email = data.get('email')

	db = DatabaseConnection()
	db.add_student(name, email)

	response = {
	"message": "Student added"
	}

	return jsonify(response), 201

app.run(debug=True)
