import sqlite3
import os

class UseDatabase:

    def __init__(self,config:str) -> None:
        self.conn = config
        
    def __enter__(self) -> 'cursor':
        BASE_DIR = os.path.dirname('/home/hkumar/Code/DB/')
        DB_PATH = os.path.join(BASE_DIR,"vsearchlogdb.db")
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        return self.cursor


    def __exit__(self,exc_type,exc_value,exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
