import sqlite3


class DatabaseManager:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)

    def __del__(self):
        self.connection.close()

    def _execute(self, statement, values=None):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, table_name, columns):
        columns_and_types = [f'{column_name} {data_type}'
                             for column_name, data_type in columns.items()]

        self._execute(
            f'''
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_and_types)});
            '''
        )
    
    def drop_table(self, table_name):
        self._execute(f'DROP TABLE {table_name}')

    