import sqlite3
import os
from typing import List
from Person import Person
from abstract import FormalParserInterface


class WorkWithDB(FormalParserInterface):
    def __init__(self):
        self.file_path = "my_database.db"
        self.conn = sqlite3.connect("my_database.db")
        self.cursor = self.conn.cursor()

    def insert_into_table(self, new_contact_info: Person) -> None:
        self.cursor.execute("""INSERT INTO contacts (name, address, phone, id) 
        VALUES (?, ?, ?, ?)""", [new_contact_info.name,
                                 new_contact_info.address,
                                 new_contact_info.phone, new_contact_info.id])
        self.conn.commit()

    def delete_from_table(self, search_id_str: str) -> None:
        self.cursor.execute("DELETE FROM contacts WHERE id = ?",
                            (search_id_str,))
        self.conn.commit()

    def update_table(self, new_contact_info: Person, contact_id: str) -> None:
        self.cursor.execute("""UPDATE contacts SET name = ?, address = ?, 
        phone = ?, id = ? WHERE id = ?""", [new_contact_info.name,
                                            new_contact_info.address,
                                            new_contact_info.phone,
                                            new_contact_info.id,
                                            contact_id])
        self.conn.commit()

    def get_all_contacts(self) -> List[Person]:
        self.cursor.execute("""SELECT * FROM contacts""")
        out_info = Person("", "", "", "")
        out_list = []
        tupl = self.cursor.fetchall()
        for i in range(len(tupl)):
            out_info.name = tupl[i][0]
            out_info.address = tupl[i][1]
            out_info.phone = tupl[i][2]
            out_info.id = tupl[i][3]
            out_list.append(out_info)
            out_info = Person("", "", "", "")
        return out_list

    def select_from_db(self, search_id_str: str) -> List[tuple]:
        sql = "SELECT * FROM contacts WHERE id=?"
        self.cursor.execute(sql, [search_id_str])
        return self.cursor.fetchall()

    def create_table(self) -> None:
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (name text, 
               address text, phone text, id text)""")

    def checking_id(self, new_contact_id: str) -> bool:
        self.cursor.execute("SELECT * FROM contacts WHERE id=?",
                            [new_contact_id])
        if not self.cursor.fetchall():
            return False
        return True

    def check_file_exist(self):
        if not os.path.exists(self.file_path):
            print("DB not found")
            quit()
