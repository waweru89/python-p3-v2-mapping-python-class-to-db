import pytest
from department import Department  
from __init__ import CURSOR, CONN  

class TestDepartment:
    '''Test cases for Department class in department.py'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''Drops the table before each test to ensure a clean state.'''
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        CONN.commit()

    def test_creates_table(self):
        '''Test that the create_table() method creates the 'departments' table if it does not exist.'''
        Department.create_table()
        
        CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='departments'")
        result = CURSOR.fetchone()
        assert result is not None  # If table exists, result will not be None

    def test_drops_table(self):
        '''Test that the drop_table() method drops the 'departments' table if it exists.'''

        # Create the table if it doesn't exist
        Department.create_table()

        # Drop the table
        Department.drop_table()

        # Check if the table was dropped
        CURSOR.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='departments'")
        result = CURSOR.fetchone()
        assert result is None  # If table does not exist, result will be None
