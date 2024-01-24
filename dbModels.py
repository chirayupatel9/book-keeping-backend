from datetime import datetime

from dbconnect import db
from pony.orm import *

# db.drop_all_tables(with_all_data=True)

# Master Entities
class Org(db.Entity):
    org_id = PrimaryKey(int, auto=True)
    description = Required(str)
    orgcode = Required(str)
    address = Optional(str)
    phone = Optional(str)
    email = Optional(str)
    ein = Optional(str)
    vendors = Set('Vendor')
    roles = Set('Role')
    users = Set('User')
    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())


class Vendor(db.Entity):
    ven_id = PrimaryKey(int, auto=True)
    description = Required(str)
    vendorcode = Required(str)
    address = Optional(str)
    phone = Optional(str)
    email = Optional(str)
    label = Optional(str)
    org = Required(Org)
    account_transactions = Set('AccountTransaction', reverse='vendor')  # Add reverse attribute
    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())

    # Add other vendor-related attributes


class Role(db.Entity):
    r_id = PrimaryKey(int, auto=True)
    description = Required(str)
    role_id = Required(str)
    org = Required(Org)
    users = Set('User', reverse='roles')
    # Add other role-related attributes
    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())


class User(db.Entity):
    user_id = PrimaryKey(int, auto=True)
    username = Required(str)
    password = Required(str)
    org = Required(Org)
    roles = Set(Role)
    import_files = Set('ImportFile', reverse='user')  # Add reverse attribute
    invoice_files = Set('InvoiceFile', reverse='user')  # Add reverse attribute

    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())


# Add other user-related attributes


# Transaction Entities
class Log(db.Entity):
    log_id = PrimaryKey(int, auto=True)
    timestamp = Required(str)
    message = Required(str)
    # Add other log-related attributes
    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())


class AccountTransaction(db.Entity):
    acc_id = PrimaryKey(int, auto=True)
    description = Optional(str)
    vendor = Required('Vendor')
    postingdate = Required(str)
    transactiondate = Required(str)
    filename = Required('ImportFile')
    if_filename = Optional('InvoiceFile')
    importdate = Required(str)
    # Add other account transaction-related attributes

    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())



class TransactionType(db.Entity):
    tra_id = PrimaryKey(int, auto=True)
    description = Required(str)
    tcode = Required(str)
    transactions = Required(str)
    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())


class ImportFile(db.Entity):
    im_id = PrimaryKey(int, auto=True)
    filename = Required(str)
    user = Required(User)
    account_transactions = Set(AccountTransaction, reverse='filename')  # Add reverse attribute
    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())

    # Add other import file-related attributes


class InvoiceFile(db.Entity):
    if_id = PrimaryKey(int, auto=True)
    if_filename = Required(str)
    user = Required(User)
    account_transactions = Set(AccountTransaction, reverse='if_filename')  # Add reverse attribute
    created_at = Required(datetime, default=datetime.utcnow)
    updated_at = Set('YourEntity', reverse='created_at', default=set())

    # Add other invoice file-related attributes
try:
    # db.drop_all_tables(with_all_data=True)
    db.generate_mapping(create_tables=True)
except Exception as e:
    print(f"Error: {e}")
    raise