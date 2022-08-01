import pytest
from sampleProgram_Swati import Account, Contact

# Test case 1: When Account name length is > 40
def test_invalidaccount():
    with pytest.raises(ValueError):
        accountname = "Test"*11
        testaccount = Account(accountname)


# Testcase 2: When name is not passed when creating Account object
def test_createaccountwithnoname():
    with pytest.raises(TypeError):
        testaccount = Account()


#  TestCase 3: An Account object is created. Update name using setter
def test_createaccount():
    testaccount = Account("Test")
    assert testaccount.name == "Test"
    assert testaccount.contactlist == []
    testaccount.name = "ABC"
    assert testaccount.name == "ABC"


# Testcase 4: Incorrect type provided when updating contactlist of an Account
def test_updatecontactlist():
    with pytest.raises(ValueError):
        testaccount = Account("Test")
        testaccount.updatecontactlist("contact")


# Testcase 5: Name of Contact is not correct
contactnames= ["Test"*21, "1test"]
@pytest.mark.parametrize("paramdict", contactnames)
def test_invalidcontact(paramdict):
    with pytest.raises(ValueError):
        contactname = Contact(paramdict)


# Testcase 6: Correct Contact object created
def test_createcontact():
    testcontact = Contact("test")
    assert testcontact.name == "test"
    assert testcontact.phonenumber == ""
    assert not testcontact.account

    testcontact.phonenumber = "+124637284713"
    assert testcontact.phonenumber == "+124637284713"

    testcontact.name = "ABCContact"
    assert testcontact.name == "ABCContact"

    assert repr(testcontact) == "ABCContact"


# Incorect Contact phonenumber assigned
def test_incorrectcontactphonenumber():
    testcontact = Contact("Test")
    with pytest.raises(ValueError):
        testcontact.phonenumber = "7463846372"


# Incorrect object type assigned to account of a Contact
def test_incorrectaccountlinkedtocontact():
    with pytest.raises(ValueError):
        testcontact = Contact("Test")
        testcontact.account = "account"


# Create multiple Contacts and assign an Account to them. Two contacts have same name and phone number
def test_assignaccounttocontact():
    testaccount = Account("TestAccount")

    testcontact1 = Contact("TestContact")
    testcontact1.account = testaccount

    testcontact2 = Contact("TestContact2")
    testcontact2.account = testaccount

    testcontact3 = Contact("TestContact")
    testcontact3.account = testaccount

    assert [contact.name for contact in testaccount.contactlist] == ["TestContact", "TestContact2"]
