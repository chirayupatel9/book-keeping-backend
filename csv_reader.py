import csv
from collections import defaultdict
from dbcrud import *
def reader(csv_file_path,trans_type):
    transactions = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader, None)
        if headers is None:
            raise ValueError("CSV file has no header.")
        column_indices = {header: index for index, header in enumerate(headers)}
        for row in csv_reader:
            transaction = {header: row[column_indices[header]] for header in headers}
            tc = get_transaction_type(trans_type)
            if tc.tcode == "CREDIT": #hard coded
                transaction['Amount'] = (-float(transaction['Amount']))
                transactions.append(transaction)
            else:
                transaction['Amount'] = float(transaction['Amount'])
                transactions.append(transaction)
            # transactions_by_category[transaction['Category']].append(transaction)
        return transactions
    # for category, transactions in transactions_by_category.items():
    #     print(f"Category: {category}")
        # for transaction in transactions:
        #     yield transaction
            # print(f"  {', '.join(f'{key}: {value}' for key, value in transaction.items())}")
    # return transactions_by_category

# csv_file_path = 'static/datasets/statement.CSV'
# grouped_transactions = reader(csv_file_path,"CREDIT")
# print(grouped_transactions)
# # Print the grouped transactions
# for category, transactions in grouped_transactions.items():
#     # print(f"Category: {category}")
#     for transaction in transactions:
#         print(f"  {', '.join(f'{key}: {value}' for key, value in transaction.items())}")
