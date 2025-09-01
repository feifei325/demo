#!/usr/bin/env python3
"""
MySQL Connection Example
A comprehensive example showing how to connect to MySQL database using Python.
"""

import mysql.connector
from mysql.connector import Error
import logging
from typing import Optional, List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MySQLConnection:
    """MySQL database connection handler"""
    
    def __init__(self, host: str, database: str, username: str, password: str, port: int = 3306):
        """
        Initialize MySQL connection parameters
        
        Args:
            host: MySQL server host
            database: Database name
            username: MySQL username
            password: MySQL password
            port: MySQL port (default: 3306)
        """
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.port = port
        self.connection: Optional[mysql.connector.MySQLConnection] = None
        self.cursor: Optional[mysql.connector.cursor.MySQLCursor] = None
    
    def connect(self) -> bool:
        """
        Establish connection to MySQL database
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password,
                autocommit=True
            )
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                db_info = self.connection.get_server_info()
                logger.info(f"Successfully connected to MySQL Server version {db_info}")
                logger.info(f"Connected to database: {self.database}")
                return True
            
        except Error as e:
            logger.error(f"Error while connecting to MySQL: {e}")
            return False
    
    def disconnect(self) -> None:
        """Close MySQL connection"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection and self.connection.is_connected():
                self.connection.close()
                logger.info("MySQL connection is closed")
        except Error as e:
            logger.error(f"Error while disconnecting from MySQL: {e}")
    
    def execute_query(self, query: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        """
        Execute SELECT query and return results
        
        Args:
            query: SQL query string
            params: Query parameters (optional)
            
        Returns:
            List of dictionaries containing query results
        """
        try:
            if not self.cursor:
                raise Exception("No active database connection")
            
            self.cursor.execute(query, params or ())
            result = self.cursor.fetchall()
            logger.info(f"Query executed successfully. Rows returned: {len(result)}")
            return result
            
        except Error as e:
            logger.error(f"Error executing query: {e}")
            return []
    
    def execute_update(self, query: str, params: Optional[tuple] = None) -> int:
        """
        Execute INSERT, UPDATE, DELETE queries
        
        Args:
            query: SQL query string
            params: Query parameters (optional)
            
        Returns:
            Number of affected rows
        """
        try:
            if not self.cursor:
                raise Exception("No active database connection")
            
            self.cursor.execute(query, params or ())
            affected_rows = self.cursor.rowcount
            logger.info(f"Update query executed successfully. Rows affected: {affected_rows}")
            return affected_rows
            
        except Error as e:
            logger.error(f"Error executing update query: {e}")
            return 0
    
    def execute_many(self, query: str, data: List[tuple]) -> int:
        """
        Execute query with multiple parameter sets
        
        Args:
            query: SQL query string
            data: List of parameter tuples
            
        Returns:
            Number of affected rows
        """
        try:
            if not self.cursor:
                raise Exception("No active database connection")
            
            self.cursor.executemany(query, data)
            affected_rows = self.cursor.rowcount
            logger.info(f"Batch query executed successfully. Rows affected: {affected_rows}")
            return affected_rows
            
        except Error as e:
            logger.error(f"Error executing batch query: {e}")
            return 0

def demo_mysql_operations():
    """Demonstrate various MySQL operations"""
    
    # Database connection configuration
    config = {
        'host': 'localhost',
        'database': 'test_db',
        'username': 'your_username',
        'password': 'your_password',
        'port': 3306
    }
    
    # Create database connection
    db = MySQLConnection(**config)
    
    try:
        # Connect to database
        if not db.connect():
            logger.error("Failed to connect to database")
            return
        
        # Create sample table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            age INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        db.execute_update(create_table_query)
        logger.info("Users table created successfully")
        
        # Insert single record
        insert_query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        db.execute_update(insert_query, ("John Doe", "john@example.com", 30))
        
        # Insert multiple records
        users_data = [
            ("Alice Smith", "alice@example.com", 25),
            ("Bob Johnson", "bob@example.com", 35),
            ("Carol Brown", "carol@example.com", 28)
        ]
        db.execute_many(insert_query, users_data)
        
        # Select all users
        select_all_query = "SELECT * FROM users ORDER BY created_at DESC"
        users = db.execute_query(select_all_query)
        
        print("\n=== All Users ===")
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Age: {user['age']}")
        
        # Select users with condition
        select_filtered_query = "SELECT * FROM users WHERE age > %s"
        adult_users = db.execute_query(select_filtered_query, (25,))
        
        print(f"\n=== Users older than 25 ===")
        for user in adult_users:
            print(f"Name: {user['name']}, Age: {user['age']}")
        
        # Update record
        update_query = "UPDATE users SET age = %s WHERE email = %s"
        updated_rows = db.execute_update(update_query, (31, "john@example.com"))
        print(f"\nUpdated {updated_rows} record(s)")
        
        # Delete record
        delete_query = "DELETE FROM users WHERE email = %s"
        deleted_rows = db.execute_update(delete_query, ("bob@example.com",))
        print(f"Deleted {deleted_rows} record(s)")
        
        # Count remaining users
        count_query = "SELECT COUNT(*) as total_users FROM users"
        count_result = db.execute_query(count_query)
        print(f"\nTotal users remaining: {count_result[0]['total_users']}")
        
    except Exception as e:
        logger.error(f"Demo execution error: {e}")
    
    finally:
        # Always close the connection
        db.disconnect()

def test_connection(host: str, database: str, username: str, password: str, port: int = 3306) -> bool:
    """
    Test MySQL database connection
    
    Args:
        host: MySQL server host
        database: Database name
        username: MySQL username
        password: MySQL password
        port: MySQL port
        
    Returns:
        bool: True if connection successful
    """
    db = MySQLConnection(host, database, username, password, port)
    
    if db.connect():
        print("✅ MySQL connection test successful!")
        db.disconnect()
        return True
    else:
        print("❌ MySQL connection test failed!")
        return False

if __name__ == "__main__":
    print("MySQL Connection Example")
    print("=" * 50)
    
    # Example usage:
    # Uncomment and modify the following lines with your MySQL credentials
    
    # Test connection
    # test_connection(
    #     host='localhost',
    #     database='your_database',
    #     username='your_username',
    #     password='your_password'
    # )
    
    # Run demo (make sure to update credentials in demo_mysql_operations function)
    # demo_mysql_operations()
    
    print("\n📝 Instructions:")
    print("1. Install mysql-connector-python: pip install mysql-connector-python")
    print("2. Update database credentials in the configuration")
    print("3. Uncomment and run test_connection() or demo_mysql_operations()")
    print("4. Make sure your MySQL server is running and accessible")