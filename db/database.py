
import psycopg2

# class for connecting and performing operations
class TaskDatabase: 
    def __init__(self, dbname, dbuser, dbpassword, dbport="5432", dbhost="localhost"):
        self.conn= psycopg2.connect(dbname=dbname, host=dbhost, user=dbuser, password=dbpassword, port=dbport)

    def create_task(self, title, description):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tasks.task_manager(title, description, created_at) VALUES(%s, %s, now())", (title, description))
        self.conn.commit()

    def read_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks.task_manager")
        tasks = cursor.fetchall()
        return tasks
    
    def update_task(self, task_id, new_title, new_description):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tasks.task_manager SET title = %s, description = %s WHERE id = %s", (new_title, new_description, task_id))
        self.conn.commit()
    
    def delete_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tasks.task_manager WHERE id = %s", (task_id,))
        self.conn.commit()
    
    def close(self):
        self.conn.close()