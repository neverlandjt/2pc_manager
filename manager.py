from sqlalchemy import create_engine


class Manager:
    def __init__(self, credentials: list):
        self.connections = [create_engine(cred).connect() for cred in credentials]
        self.transactions = [conn.begin_twophase() for conn in self.connections]

    def execute_all(self, queries: list):
        if len(queries) == len(self.connections):
            # change transaction limit to block
            transaction_count = transaction_limit = len(queries)
            try:
                for transaction_no in range(transaction_count):
                    self.connections[transaction_no].execute(queries[transaction_no])
                    self.transactions[transaction_no].prepare()
                for transaction_no in range(transaction_limit):
                    self.transactions[transaction_no].commit()
                print('Success')
            except Exception as e:
                for transaction_no in range(transaction_limit):
                    self.transactions[transaction_no].rollback()
                print('Failure, ', e)
