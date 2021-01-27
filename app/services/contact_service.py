from app.repository.contacts_interface import FormalParserInterface
from app.services.Person import Person
from typing import List


class Controller:
    def __init__(self, storage: FormalParserInterface):
        self.storage = storage

    def find_contact(self, search_id_str: str) -> Person:
        try:
            tupl = self.storage.select_from_db(search_id_str)
            find_info = Person("", "", "", "")
            find_info.name = tupl[0][0]
            find_info.address = tupl[0][1]
            find_info.phone = tupl[0][2]
            find_info.id = tupl[0][3]
        except:
            find_info = Person("", "", "", "")
            return find_info
        return find_info

    def del_contact(self, search_id_str: str) -> bool:
        if self.storage.checking_id(search_id_str):
            self.storage.delete_from_table(search_id_str)
            return True
        return False

    def load_for_add(self, new_contact_info: Person) -> bool:
        if self.storage.checking_id(new_contact_info.id):
            return False
        self.storage.insert_into_table(new_contact_info)
        return True

    def load_for_edit(self, new_contact_info: Person, contact_id: str) -> int:
        if not self.storage.checking_id(new_contact_info.id):
            return False
        self.storage.update_table(new_contact_info, contact_id)
        return True

    def load_to_view(self) -> List[Person]:
        return self.storage.get_all_contacts()

    def edt_contact(self, edit_id_str: str) -> bool:
        if not self.storage.checking_id(edit_id_str):
            return False
        tupl = self.storage.select_from_db(edit_id_str)
        find_info = Person("", "", "", "")
        find_info.name = tupl[0][0]
        find_info.address = tupl[0][1]
        find_info.phone = tupl[0][2]
        find_info.id = tupl[0][3]
        return True

    def create_table(self) -> None:
        self.storage.create_table()

    def fill_edit_contact(self, edit_id_str: str) -> Person:
        tupl = self.storage.select_from_db(edit_id_str)
        return Person(tupl[0][0], tupl[0][1], tupl[0][2], tupl[0][3])
