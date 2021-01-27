import unittest
from app.database import *


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.person_info = Person("Alex", "T", "+375", "22")
        self.sql = WorkWithDB()
        self.conn = sqlite3.connect("my_database.db")
        self.cursor = self.conn.cursor()

    def test_insert_into_table(self):
        self.sql.insert_into_table(self.person_info)
        self.cursor.execute("SELECT * FROM contacts WHERE id=22")
        cursor_out = self.cursor.fetchall()
        self.assertEqual(cursor_out, [('Alex', 'T', '+375',
                                       '22')])

    def test_update_table(self):
        self.sql.insert_into_table(self.person_info)
        new_person_info = Person('Olga', 'Minsk', '+375', '22')
        self.sql.update_table(new_person_info, '22')
        self.cursor.execute("SELECT * FROM contacts WHERE id=22")
        cursor_out = self.cursor.fetchone()
        self.assertEqual(cursor_out, ('Olga', 'Minsk', '+375', '22'))
        self.sql.delete_from_table('22')

    def test_delete_from_table(self):
        self.res = self.cursor.execute("SELECT * FROM contacts WHERE id=33")
        self.conn.commit()
        cursor_out = self.cursor.fetchall()
        self.assertEqual(cursor_out, [])

    def test_select_from_db(self):
        self.sql.insert_into_table(self.person_info)
        info = self.sql.select_from_db('22')
        self.assertEqual(info, self.person_info)
        self.sql.delete_from_table('22')

    def test_get_all_contact(self):
        self.sql.insert_into_table(self.person_info)
        list_contacts = self.sql.get_all_contacts()
        self.assertEqual(list_contacts[0], self.person_info)
        self.sql.delete_from_table('22')

    def test_create_table(self):
        self.sql.create_table()
        res = self.cursor.execute("SELECT * FROM contacts")
        res = res.fetchall()
        self.assertEqual(res, [])


if __name__ == "__main__":
    unittest.main()
