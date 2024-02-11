# ICustomerService.py
from abc import ABC, abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def get_customer_by_id(self, customer_id):
        pass

    @abstractmethod
    def get_customer_by_username(self, username):
        pass

    @abstractmethod
    def save_to_database(self, customer_data):
        pass

    @abstractmethod
    def update_customer(self, customer_id, updated_customer):
        pass

    @abstractmethod
    def delete_customer(self, customer_id):
        pass
