import sqlite3

# HELPER METHODS

def createTable(db_file):
	"""
		Creates a table (if it doesn’t already exist) for storing user data (like username, total_solved, etc.)
	"""
	try:
		#Connect database file
		connection = sqlite3.connect(db_file)
		cursor = connection.cursor()

		query = """
		CREATE TABLE IF NOT EXISTS users(
		username TEXT PRIMARY KEY,
		total_solved INTEGER,
		points INTEGER,
		easy_solved INTEGER DEFAULT 0,
		medium_solved INTEGER DEFAULT 0,
		hard_solved INTEGER DEFAULT 0
		)
		"""

		#Execute, close, and commit
		cursor.execute(query)
		connection.commit()
		connection.close()

	except sqlite3.Error as e:
		print(f"Error occurred: {e}")

def addUser(db_file, username, total_solved, points, easy_solved=0, medium_solved=0, hard_solved=0):
	"""
		Inserts a new user record into the table.
	"""
	try:
		#Connect database file
		connection = sqlite3.connect(db_file)
		cursor = connection.cursor()

		query = """
		INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)
		"""
		
		#Execute, close, and commit
		cursor.execute(query, (username, total_solved, points, easy_solved, medium_solved, hard_solved))
		connection.commit()

	except sqlite3.Error as e:
		print(f"Error occurred: {e}")
	finally:
		connection.close()

def updateUser(db_file, username, total_solved, points, easy_solved=0, medium_solved=0, hard_solved=0):
	"""
		Updates an existing user’s info in the table.
	"""
	try:
		#Connect database file
		connection = sqlite3.connect(db_file)
		cursor = connection.cursor()

		query = """
		UPDATE users SET total_solved=?, points=?, easy_solved=?, medium_solved=?, hard_solved=? WHERE username=?;
		"""
		
		#Execute, close, and commit
		cursor.execute(query, (total_solved, points, easy_solved, medium_solved, hard_solved, username))
		connection.commit()


	except sqlite3.Error as e:
		print(f"Error occurred: {e}")
	finally:
		connection.close()


def resetAllUsers(db_file):
	"""
		Resets certain fields for all users (e.g., sets total_solved and points back to 0).
	"""
	try:
		#Connect database file
		connection = sqlite3.connect(db_file)
		cursor = connection.cursor()

		query = """
		UPDATE users SET total_solved=0, points=0, easy_solved=0, medium_solved=0, hard_solved=0
		"""
		
		#Execute, close, and commit
		cursor.execute(query)
		connection.commit()


	except sqlite3.Error as e:
		print(f"Error occurred: {e}")
	finally:
		connection.close()

def displayAllUsers(db_file):
	"""
		Fetches all user records from the database and prints them out in a formatted table.
	"""
	try:
		#Connect database file
		connection = sqlite3.connect(db_file)
		cursor = connection.cursor()

		query = """
		SELECT * FROM users 
		"""
		
		#Execute, close
		cursor.execute(query)
		users = cursor.fetchall()

		if not users:
			print("No users found in the database!")
			return None
		
		#Print user data

		print("\nUser Records:\n")
		print("-"*100)
		for user in users:
			print(f"Username: {user[0]}, Total Solved: {user[1]}, Points: {user[2]}, Easy Solved: {user[3]}, Medium Solved: {user[4]}, Hard Solved: {user[5]}")
		print("-"*100)


		return users

	except sqlite3.Error as e:
		print(f"Error occurred: {e}")
	finally:
		connection.close()



def top_users(db_file):
	"""
		Retrieves the top 5 users based on their points
	"""
	try:
		#Connect database file
		connection = sqlite3.connect(db_file)
		cursor = connection.cursor()

		query = """
		SELECT * FROM users ORDER BY points DESC LIMIT 5
		"""
		
		#Execute, close
		cursor.execute(query)
		users = cursor.fetchall()

		#Extract top 5 users

		top_5 = users[:5]
		print("\nTop 5 Users:\n")
		print("-"*100)
		for user in top_5:
			print(f"Username: {user[0]}, Total Solved: {user[1]}, Points: {user[2]}, Easy Solved: {user[3]}, Medium Solved: {user[4]}, Hard Solved: {user[5]}")
		print("-"*100)
		

		return top_5

	except sqlite3.Error as e:
		print(f"Error occurred: {e}")
	finally:
		connection.close()
