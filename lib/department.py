from __init__ import CURSOR, CONN

class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        '''Creates the 'departments' table if it doesn't exist.'''
        sql = """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        '''Drops the 'departments' table if it exists.'''
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        CONN.commit()

    def save(self):
        '''Saves a department to the database.'''
        if self.id is None:
            CURSOR.execute("INSERT INTO departments (name, location) VALUES (?, ?)", (self.name, self.location))
            self.id = CURSOR.lastrowid
            CONN.commit()

    @classmethod
    def create(cls, name, location):
        '''Creates a new department instance and saves it to the database.'''
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        '''Updates the department record in the database.'''
        CURSOR.execute("UPDATE departments SET name = ?, location = ? WHERE id = ?", 
                       (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        '''Deletes the department record from the database.'''
        CURSOR.execute("DELETE FROM departments WHERE id = ?", (self.id,))
        CONN.commit()
