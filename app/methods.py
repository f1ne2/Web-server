from interface import Connection
from controller import Controller
from database import WorkWithDB
from Person import Person


class Methods(Connection):
    def __init__(self):
        self.data = WorkWithDB()
        Controller(self.data).create_table()

    def put(self, target: str) -> bool:
        array = target.split("/")[1:]
        new_arr = [array[i].replace("_", " ") for i in range(len(array))]
        return Controller(self.data).load_for_add(Person(new_arr[2],
                                                         new_arr[3],
                                                         new_arr[4],
                                                         new_arr[1]))

    def get(self, target: str):
        array = target.split("/")[1:]
        if len(array) == 1:
            return Controller(self.data).load_to_view()
        else:
            return [Controller(self.data).find_contact(array[1])]

    def post(self, target: str):
        array = target.split("/")[1:]
        new_arr = [array[i].replace("_", " ") for i in range(len(array))]
        return Controller(self.data).load_for_edit(Person(new_arr[2],
                                                          new_arr[3],
                                                          new_arr[4],
                                                          new_arr[1]),
                                                   new_arr[1])

    def delete(self, target: str):
        array = target.split("/")[2]
        return Controller(self.data).del_contact(array)
