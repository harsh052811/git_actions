from dotenv import load_dotenv
import mysql.connector as connector
import os
load_dotenv()

class Database:

    def __init__(self):
        self.cursor = None
        try:
            self.con = connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database=os.getenv("DB_NAME"),
                port=os.getenv("DB_PORT"))

        except Exception as e:
            print(e)

    def get_cursor(self):
        if self.cursor is not None:
            return self.cursor
        else:
            self.cursor=self.con.cursor(buffered=True)
        
        return self.cursor