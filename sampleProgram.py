'''
Problem Statement:
An organization needs to store data of its customer's accounts and the point of contacts related to those accounts.
Create two classes: Account and Contact.
Account class has two fields:
    Name: Validate the value which can be alphanumeric characters with length not more than 40
    Contact list which contains all linked Contacts to a particular Account. Default value = []
Contact list of an Account can be updated only through method updatecontactlist()

A Contact has fields:
    Name: Can only be can be alphanumeric characters, not starting with any number & length should not be greater than 80
    Phone number: Should start with "+" and have 12 digits
    Account: An object of Account class

Whenever, a Contact is assigned an Account, it should update contactlist for the Account to which it is linked. Please
note that if an contact with same name and phone number is already present in the list, don't append it to contactlist.

Prerequisites:
--------------
Python 3.x
Import Python package:
    Pytest (to run test cases in test_sampleProgram_Swati.py)
    Pytest-Cov  (for code coverage)
'''

import re


class Account:
    """
    The class stores information about customers (Organizations)

    Attributes
    ----------
    _name: str
        name of the Account (customer Organization)
    _contactlist: list
        list of contacts associated with an account (default: empty list)

    Methods
    -------
    updatecontactlist(contact):
        Updates contactlist by appending contact.
    """

    def __init__(self, name):
        if self.checkname(name):
            self._name = name
        self._contactlist = []

    @property
    def name(self):
        """
        Getter method for name
        :return: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Setter method for name. name can be any string which doesn't start with a number and whose length is <80.
        :param name: str
        :return: None
        """
        if self.checkname(name):
            self._name = name

    @property
    def contactlist(self):
        """
        Getter method for contactlist
        :return: _contactlist (type: list)
        """
        return self._contactlist

    @staticmethod
    def checkname(name):
        if len(name) > 40:
            raise ValueError("Account name should have length <=40")
        return True

    def updatecontactlist(self, contact):
        """
        Updates contact list by adding contact to it.
        :param contact: Contact
        :return: contactlist
        """
        if not isinstance(contact, Contact):
            raise ValueError("contact should be an object of Contact class")
        if not contact in self._contactlist:
            self._contactlist.append(contact)
        return self.contactlist


class Contact:
    """
     The class stores information about point of contact for an Account

     Attributes
     ----------
     _name: str
         name of the Contact
     _phonenumber: str
         Phone number of the contact
     _account: Account
         Account to which a contact is linked
     """

    def __init__(self, name):
        if self.checkcontactname(name):
            self._name = name
        self._phonenumber = ''
        self._account = None

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return True if self._name == other._name\
            and self._phonenumber == other._phonenumber\
            and self._account == other._account\
            else False

    @property
    def name(self):
        """
        Getter method for name
        :return: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Setter method for name
        :param name: str
        :return: None
        """
        if self.checkcontactname(name):
            self._name = name

    @property
    def phonenumber(self):
        """
        Getter method for phonenumber
        :return: str
        """
        return self._phonenumber

    @phonenumber.setter
    def phonenumber(self, pnumber):
        """
        Setter method for phonenumber
        :param phonenumber: str
        :return: None
        """
        if not re.match(r'^\+\d{12}', pnumber, flags=re.I):
            raise ValueError("")
        self._phonenumber = pnumber

    @property
    def account(self):
        """
        Setter for account
        :return: Account
        """

    @account.setter
    def account(self, account):
        """
        Setter for _account
        :param account: Account
        :return: None
        """
        if self.isaccount(account):
            self._account = account
            account.updatecontactlist(self)

    @staticmethod
    def checkcontactname(name):
        """
        Checks if name is a valid Contact name
        :param name: str
        :return: Bool
        """
        if re.match(r'^\d+.*', name, flags=re.I) or len(name) > 80:
            raise ValueError("Contact name cannot start with a number and should have length <=80")
        return True

    @staticmethod
    def isaccount(account):
        """
        Checks if account is a valid Account object
        :return:
        """
        if not isinstance(account, Account):
            raise ValueError("account should be a valid object of Account class.")
        return True


if __name__ == "__main__":
    account_samsung = Account("Samsung")

    contact_samsung = Contact("Marie Pierre")
    contact_samsung.phonenumber = "+01843727172717"
    contact_samsung.account = account_samsung

    contact_samsung_2 = Contact("Claudia Serret")
    contact_samsung_2.phonenumber = "+102933828183"
    contact_samsung_2.account = account_samsung

    contact_samsung_3 = Contact("Marie Pierre")
    contact_samsung_3.phonenumber = "+01843727172717"
    contact_samsung_3.account = account_samsung

    print(f"Account name: {account_samsung.name}")
    print(f"Contacts related to Account {account_samsung.name} are: {account_samsung.contactlist}")

