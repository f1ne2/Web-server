from Person import Person
from typing import List
from abc import ABCMeta, abstractmethod


class FormalParserInterface(metaclass=ABCMeta):

    @abstractmethod
    def check_file_exist(self):
        pass

    @abstractmethod
    def delete_from_table(self, delete_id_str: str) -> int:
        pass

    @abstractmethod
    def update_table(self, new_contact_info: Person, contact_id: str) -> None:
        pass

    @abstractmethod
    def get_all_contacts(self) -> List[Person]:
        pass

    @abstractmethod
    def insert_into_table(self, new_contact_info: Person) -> None:
        pass

    @abstractmethod
    def select_from_db(self, search_id_str: str) -> List[tuple]:
        pass

    @abstractmethod
    def create_table(self) -> None:
        pass

    @abstractmethod
    def checking_id(self, new_contact_id: str) -> bool:
        pass

