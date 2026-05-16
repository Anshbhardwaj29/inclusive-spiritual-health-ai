import sqlite3

class MemoryManager:
    def __init__(self, db_name="misty_memory.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS history 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, user_text TEXT, bot_text TEXT)"""
        self.conn.execute(query)
        self.conn.commit()

    def save_chat(self, user_input, bot_response):
        query = "INSERT INTO history (user_text, bot_text) VALUES (?, ?)"
        self.conn.execute(query, (user_input, bot_response))
        self.conn.commit()

    def get_recent_history(self, limit=5):
        query = "SELECT user_text, bot_text FROM history ORDER BY id DESC LIMIT ?"
        cursor = self.conn.execute(query, (limit,))
        rows = cursor.fetchall()
        # History ko string mein convert karna taaki LLM samajh sake
        history_str = ""
        for row in reversed(rows):
            history_str += f"User: {row[0]}\nMisty: {row[1]}\n"
        return history_str