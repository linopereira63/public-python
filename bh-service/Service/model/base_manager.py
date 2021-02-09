"""
BaseManager class - provides common singleton manager behavior
"""


class BaseManager:

    def __init__(self):
        self.next_id = 0

    def _get_next_id(self):
        self.next_id += 1
        return self.next_id

    @staticmethod
    def convert_string_id(str_id):
        if str_id.isdigit():
            return int(str_id), None
        else:
            return -1, "Invalid ID " + str_id


