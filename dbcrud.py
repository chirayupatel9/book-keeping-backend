from pony.orm import db_session, commit, select
from dbModels import *


# Create Operations

@db_session
def create_org(description, orgcode, address, phone, email, ein):
    org = Org(description=description, orgcode=orgcode, address=address, phone=phone, email=email, ein=ein)
    commit()
    return org


@db_session
def create_vendor(description, vendorcode, address, phone, email, label, org):
    vendor = Vendor(description=description, vendorcode=vendorcode, address=address, phone=phone, email=email,
                    label=label, org=org)
    commit()
    return vendor


@db_session
def create_role(description, id, org):
    role = Role(description=description, id=id, org=org)
    commit()
    return role


@db_session
def create_user(username, password, org):
    user = User(username=username, password=password, org=org)
    commit()
    return user


@db_session
def create_log(timestamp, message):
    log = Log(timestamp=timestamp, message=message)
    commit()
    return log


var = {'Card': '6740', 'Transaction Date': '02/01/2023', 'Post Date': '02/01/2023',
       'Description': 'Payment Thank You-Mobile',
       'Category': '', 'Type': 'Payment', 'Amount': -4000.0, 'Memo': ''},

# description thi vendor
@db_session
def create_account_transaction(description, vendor, postingdate, transactiondate, importfile, invoicefile, importdate):
    account_transaction = AccountTransaction(
        description=description,
        vendor=vendor,
        postingdate=postingdate,
        transactiondate=transactiondate,
        importfile=importfile,
        invoicefile=invoicefile,
        importdate=importdate
    )
    commit()
    return account_transaction


@db_session
def create_transaction_type(description, tcode):
    transaction_type = TransactionType(description=description, tcode=tcode)
    commit()
    return transaction_type


@db_session
def create_import_file(filename, user):
    import_file = ImportFile(filename=filename, user=user)
    commit()
    return import_file


@db_session
def create_invoice_file(filename, user):
    invoice_file = InvoiceFile(filename=filename, user=user)
    commit()
    return invoice_file


# Read Operations

@db_session
def get_org(org_id):
    return Org.get(id=org_id)


@db_session
def get_vendor(vendor_id):
    return Vendor.get(id=vendor_id)


@db_session
def get_role(role_id):
    return Role.get(id=role_id)


@db_session
def get_user(user_id):
    return User.get(id=user_id)


@db_session
def get_log(log_id):
    return Log.get(id=log_id)


@db_session
def get_account_transaction(transaction_id):
    return AccountTransaction.get(id=transaction_id)


@db_session
def get_transaction_type(trans_type):
    return TransactionType.get(tcode=trans_type)


@db_session
def get_import_file(file_id):
    return ImportFile.get(id=file_id)


@db_session
def get_invoice_file(file_id):
    return InvoiceFile.get(id=file_id)


# Update Operations

@db_session
def update_org(org_id, **kwargs):
    org = Org.get(id=org_id)
    org.set(**kwargs)
    commit()


@db_session
def update_vendor(vendor_id, **kwargs):
    vendor = Vendor.get(id=vendor_id)
    vendor.set(**kwargs)
    commit()


@db_session
def update_role(role_id, **kwargs):
    role = Role.get(id=role_id)
    role.set(**kwargs)
    commit()


@db_session
def update_user(user_id, **kwargs):
    user = User.get(id=user_id)
    user.set(**kwargs)
    commit()


@db_session
def update_log(log_id, **kwargs):
    log = Log.get(id=log_id)
    log.set(**kwargs)
    commit()


@db_session
def update_account_transaction(transaction_id, **kwargs):
    account_transaction = AccountTransaction.get(id=transaction_id)
    account_transaction.set(**kwargs)
    commit()


@db_session
def update_transaction_type(type_id, **kwargs):
    transaction_type = TransactionType.get(id=type_id)
    transaction_type.set(**kwargs)
    commit()


@db_session
def update_import_file(file_id, **kwargs):
    import_file = ImportFile.get(id=file_id)
    import_file.set(**kwargs)
    commit()


@db_session
def update_invoice_file(file_id, **kwargs):
    invoice_file = InvoiceFile.get(id=file_id)
    invoice_file.set(**kwargs)
    commit()


# Delete Operations

@db_session
def delete_org(org_id):
    org = Org.get(id=org_id)
    org.delete()
    commit()


@db_session
def delete_vendor(vendor_id):
    vendor = Vendor.get(id=vendor_id)
    vendor.delete()
    commit()


@db_session
def delete_role(role_id):
    role = Role.get(id=role_id)
    role.delete()
    commit()


@db_session
def delete_user(user_id):
    user = User.get(id=user_id)
    user.delete()
    commit()


@db_session
def delete_log(log_id):
    log = Log.get(id=log_id)
    log.delete()
    commit()


@db_session
def delete_account_transaction(transaction_id):
    account_transaction = AccountTransaction.get(id=transaction_id)
    account_transaction.delete()
    commit()


@db_session
def delete_transaction_type(type_id):
    transaction_type = TransactionType.get(id=type_id)
    transaction_type.delete()
    commit()


@db_session
def delete_import_file(file_id):
    import_file = ImportFile.get(id=file_id)
    import_file.delete()
    commit()


@db_session
def delete_invoice_file(file_id):
    invoice_file = InvoiceFile.get(id=file_id)
    invoice_file.delete()
    commit()
