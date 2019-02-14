import psycopg2
import psycopg2.extras

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection = psycopg2.connect(
				# Fill in the appropriate credentials
			dbname="learn", user="postgres", host="localhost", password="kengo1234", port="5432"
			)
			self.connection.autocommit = True
			self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

			create_student_table = """
			CREATE TABLE IF NOT EXISTS student(name TEXT, email TEXT);
			"""

			self.cursor.execute(create_student_table)
		except:
			print("Cannot connect to the database.")

	def get_students(self):
		query = """
		SELECT * FROM student;
		"""
		self.cursor.execute(query)
		students = self.cursor.fetchall()
		return students

	def add_student(self, name, email):
		query = f"""
		INSERT INTO student(name, email) VALUES('{name}', '{email}');
		"""
		self.cursor.execute(query)



