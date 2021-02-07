"""
BaseManager class - provides common singleton manager behavior
"""


class BaseManager:
    # Singleton instance that everyone should call
    _instance = None

    @staticmethod
    def get_instance():
        # Must be implemented by derived class
        return BaseManager._instance

    _NEXT_ID = 0

    @staticmethod
    def _get_next_id():
        BaseManager._NEXT_ID += 1
        return BaseManager._NEXT_ID

