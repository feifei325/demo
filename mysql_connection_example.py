#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
import os

class MySQLConnection:
    def __init__(self, host='localhost', database='testdb', user='root', password=''):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print(f"Successfully connected to MySQL database: {self.database}")
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False

    def execute_query(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            print("Not connected to database")
            return None
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            
            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
                return result
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            age INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        result = self.execute_query(create_table_query)
        if result is not None:
            print("Table 'users' created successfully")

    def insert_user(self, name, email, age):
        insert_query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        result = self.execute_query(insert_query, (name, email, age))
        if result:
            print(f"User {name} inserted successfully")

    def get_all_users(self):
        select_query = "SELECT * FROM users"
        users = self.execute_query(select_query)
        if users:
            print("All users:")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}, Created: {user[4]}")
        return users

    def update_user(self, user_id, name=None, email=None, age=None):
        updates = []
        params = []
        
        if name:
            updates.append("name = %s")
            params.append(name)
        if email:
            updates.append("email = %s")
            params.append(email)
        if age:
            updates.append("age = %s")
            params.append(age)
        
        if updates:
            params.append(user_id)
            update_query = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
            result = self.execute_query(update_query, params)
            if result:
                print(f"User {user_id} updated successfully")

    def delete_user(self, user_id):
        delete_query = "DELETE FROM users WHERE id = %s"
        result = self.execute_query(delete_query, (user_id,))
        if result:
            print(f"User {user_id} deleted successfully")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

def main():
    db_config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'database': os.getenv('DB_NAME', 'testdb'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', '')
    }
    
    db = MySQLConnection(**db_config)
    
    if db.connect():
        try:
            db.create_table()
            
            db.insert_user("Alice", "alice@example.com", 25)
            db.insert_user("Bob", "bob@example.com", 30)
            db.insert_user("Charlie", "charlie@example.com", 35)
            
            db.get_all_users()
            
            db.update_user(1, name="Alice Smith", age=26)
            
            db.get_all_users()
            
            db.delete_user(3)
            
            db.get_all_users()
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            db.close_connection()

if __name__ == "__main__":
    main()