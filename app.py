from flask import Flask, request
from flask_restful import Resource, Api
from pony.orm import db_session
from dbModels import *  # Assuming your models are defined in a module named "models"
from dbcrud import *
from csv_reader import reader

app = Flask(__name__)
api = Api(app)


# Helper function to serialize Pony ORM entities to JSON
def serialize(entity):
    return {column: getattr(entity, column) for column in entity._columns_}


@app.route("/", methods=["GET"])
def get():
    return "hello"


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/bk/hello')


# Resource for Org
class OrgResource(Resource):
    @db_session
    def get(self, org_id):
        org = Org.get(id=org_id)
        if org:
            return serialize(org)
        return {'message': 'Org not found'}, 404

    @db_session
    def post(self):
        data = request.get_json()
        org = create_org(**data)
        return serialize(org), 201

    @db_session
    def put(self, org_id):
        org = Org.get(id=org_id)
        if org:
            data = request.get_json()
            update_org(org_id, **data)
            return serialize(org)
        return {'message': 'Org not found'}, 404

    @db_session
    def delete(self, org_id):
        org = Org.get(id=org_id)
        if org:
            delete_org(org_id)
            return {'message': 'Org deleted successfully'}
        return {'message': 'Org not found'}, 404


api.add_resource(OrgResource, '/org', '/org/<int:org_id>')


# Resource for Vendor
class VendorResource(Resource):
    @db_session
    def get(self, vendor_id):
        vendor = Vendor.get(id=vendor_id)
        if vendor:
            return serialize(vendor)
        return {'message': 'Vendor not found'}, 404

    @db_session
    def post(self):
        data = request.get_json()
        vendor = create_vendor(**data)
        return serialize(vendor), 201

    @db_session
    def put(self, vendor_id):
        vendor = Vendor.get(id=vendor_id)
        if vendor:
            data = request.get_json()
            update_vendor(vendor_id, **data)
            return serialize(vendor)
        return {'message': 'Vendor not found'}, 404

    @db_session
    def delete(self, vendor_id):
        vendor = Vendor.get(id=vendor_id)
        if vendor:
            delete_vendor(vendor_id)
            return {'message': 'Vendor deleted successfully'}
        return {'message': 'Vendor not found'}, 404


api.add_resource(VendorResource, '/vendor/<int:vendor_id>', '/vendor')


# Resource for Role
class RoleResource(Resource):
    @db_session
    def get(self, role_id):
        role = Role.get(id=role_id)
        if role:
            return serialize(role)
        return {'message': 'Role not found'}, 404

    @db_session
    def post(self):
        data = request.get_json()
        role = create_role(**data)
        return serialize(role), 201

    @db_session
    def put(self, role_id):
        role = Role.get(id=role_id)
        if role:
            data = request.get_json()
            update_role(role_id, **data)
            return serialize(role)
        return {'message': 'Role not found'}, 404

    @db_session
    def delete(self, role_id):
        role = Role.get(id=role_id)
        if role:
            delete_role(role_id)
            return {'message': 'Role deleted successfully'}
        return {'message': 'Role not found'}, 404


api.add_resource(RoleResource, '/role/<int:role_id>', '/role')


# Resource for User
class UserResource(Resource):
    @db_session
    def get(self, user_id):
        user = User.get(id=user_id)
        if user:
            return serialize(user)
        return {'message': 'User not found'}, 404

    @db_session
    def post(self):
        data = request.get_json()
        user = create_user(**data)
        return serialize(user), 201

    @db_session
    def put(self, user_id):
        user = User.get(id=user_id)
        if user:
            data = request.get_json()
            update_user(user_id, **data)
            return serialize(user)
        return {'message': 'User not found'}, 404

    @db_session
    def delete(self, user_id):
        user = User.get(id=user_id)
        if user:
            delete_user(user_id)
            return {'message': 'User deleted successfully'}
        return {'message': 'User not found'}, 404


api.add_resource(UserResource, '/user/<int:user_id>', '/user')


# Resource for Log
class LogResource(Resource):
    @db_session
    def get(self, log_id):
        log = Log.get(id=log_id)
        if log:
            return serialize(log)
        return {'message': 'Log not found'}, 404

    @db_session
    def post(self):
        data = request.get_json()
        log = create_log(**data)
        return serialize(log), 201

    @db_session
    def put(self, log_id):
        log = Log.get(id=log_id)
        if log:
            data = request.get_json()
            update_log(log_id, **data)
            return serialize(log)
        return {'message': 'Log not found'}, 404

    @db_session
    def delete(self, log_id):
        log = Log.get(id=log_id)
        if log:
            delete_log(log_id)
            return {'message': 'Log deleted successfully'}
        return {'message': 'Log not found'}, 404


api.add_resource(LogResource, '/log/<int:log_id>', '/log')


# Resource for AccountTransaction
class AccountTransactionResource(Resource):
    @db_session
    def get(self, transaction_id):
        transaction = AccountTransaction.get(id=transaction_id)
        if transaction:
            return serialize(transaction)
        return {'message': 'Transaction not found'}, 404

    @db_session
    def post(self):
        data = request.get_json()
        transaction = create_account_transaction(**data)
        return serialize(transaction), 201

    @db_session
    def put(self, transaction_id):
        transaction = AccountTransaction.get(id=transaction_id)
        if transaction:
            data = request.get_json()
            update_account_transaction(transaction_id, **data)
            return serialize(transaction)
        return {'message': 'Transaction not found'}, 404

    @db_session
    def delete(self, transaction_id):
        transaction = AccountTransaction.get(id=transaction_id)
        if transaction:
            delete_account_transaction(transaction_id)
            return {'message': 'Transaction deleted successfully'}
        return {'message': 'Transaction not found'}, 404


api.add_resource(AccountTransactionResource, '/transaction/<int:transaction_id>', '/transaction')


# Resource for TransactionType
class TransactionTypeResource(Resource):
    @db_session
    def get(self, type_id):
        transaction_type = TransactionType.get(id=type_id)
        if transaction_type:
            return serialize(transaction_type)
        return {'message': 'Transaction Type not found'}, 404

    @db_session
    def post(self):
        data = request.get_json()
        transaction_type = create_transaction_type(**data)
        return serialize(transaction_type), 201

    @db_session
    def put(self, type_id):
        transaction_type = TransactionType.get(id=type_id)
        if transaction_type:
            data = request.get_json()
            update_transaction_type(type_id, **data)
            return serialize(transaction_type)
        return {'message': 'Transaction Type not found'}, 404

    @db_session
    def delete(self, type_id):
        transaction_type = TransactionType.get(id=type_id)
        if transaction_type:
            delete_transaction_type(type_id)
            return {'message': 'Transaction Type deleted successfully'}
        return {'message': 'Transaction Type not found'}, 404


api.add_resource(TransactionTypeResource, '/transactiontype/<int:type_id>', '/transactiontype')


# Resource for ImportFile
class ImportFileResource(Resource):
    @db_session
    def get(self, file_id):
        import_file = ImportFile.get(id=file_id)
        if import_file:
            return serialize(import_file)
        return {'message': 'Import File not found'}, 404

    @db_session
    def post(self):
        data = request.form
        file = request.files['file']
        if file:
            file_path = 'static/uploads/' + file.filename
            file.save(file_path)
            print("file saved")
            import_file = create_import_file(**data)
            file_data = reader(file_path)
            return serialize(import_file), 201
        # return "done"
    @db_session
    def put(self, file_id):
        import_file = ImportFile.get(id=file_id)
        if import_file:
            data = request.get_json()
            update_import_file(file_id, **data)
            return serialize(import_file)
        return {'message': 'Import File not found'}, 404

    @db_session
    def delete(self, file_id):
        import_file = ImportFile.get(id=file_id)
        if import_file:
            delete_import_file(file_id)
            return {'message': 'Import File deleted successfully'}
        return {'message': 'Import File not found'}, 404


api.add_resource(ImportFileResource, '/importfile/<int:file_id>', '/importfile')


# Resource for InvoiceFile
class InvoiceFileResource(Resource):
    @db_session
    def get(self, file_id):
        invoice_file = InvoiceFile.get(id=file_id)
        if invoice_file:
            return serialize(invoice_file)
        return {'message': 'Invoice File not found'}, 404

    @db_session
    def post(self):
        data = request.get_json()
        invoice_file = create_invoice_file(**data)
        return serialize(invoice_file), 201

    @db_session
    def put(self, file_id):
        invoice_file = InvoiceFile.get(id=file_id)
        if invoice_file:
            data = request.get_json()
            update_invoice_file(file_id, **data)
            return serialize(invoice_file)
        return {'message': 'Invoice File not found'}, 404

    @db_session
    def delete(self, file_id):
        invoice_file = InvoiceFile.get(id=file_id)
        if invoice_file:
            delete_invoice_file(file_id)
            return {'message': 'Invoice File deleted successfully'}
        return {'message': 'Invoice File not found'}, 404


api.add_resource(InvoiceFileResource, '/invoicefile/<int:file_id>', '/invoicefile')

api.init_app(app)
if __name__ == '__main__':
    app.run(debug=True,port=5002)
