from database import DatabaseManager
from datetime import datetime
import sys

db = DatabaseManager('interview.db')


class BaseTable():
    '''Base class for handling all common table functions'''

    def __init__(self, table_name):
        self.table_name = table_name

    def populate_defaults(self, records):
        for record in records:
            db.add(self.table_name, record)

    def drop_table(self):
        db.drop_table(self.table_name)

    def view(self, criteria):
        db.select(self.table_name, criteria=criteria)

    def view_all(self):
        data = db.select(self.table_name).fetchall()
        for record in data:
            print(record)

    def add(self, data):
        db.add(self.table_name, data)

    def edit(self, data):
        db.update(self.table_name, data)

    def delete(self):
        db.delete()

    def delete_all(self):
        db.delete()

    def reset(self):
        pass

    def print_title_bar(self, name):
        left_pad = '|' + ('-' * 20) + (' ' * 5)
        right_pad = (' ' * 5) + ('-' * 20) + '|'
        title = f'{left_pad}{name.upper()}{right_pad}'
        border = '|' + ('-' * (len(title) - 2)) + '|'
        print('\n'.join([border, title, border, '']))


class Jobs(BaseTable):

    def create_table(self, data=None):
        db.create_table('jobs', {
            'id': 'integer primary key autoincrement',
            'job': 'text not null',
            'date_added': 'text'
        })

    def view_practiced(self):
        db.select('jobs', criteria={'reviewed': True})

    def view_not_practiced(self):
        db.select('jobs', criteria={'reviewed': False})


class Questions(BaseTable):

    def create_table(self, data=None):
        db.create_table('questions', {
            'id': 'integer primary key autoincrement',
            'question': 'text not null',
            'answered': 'integer'
        })

    def get_random_question(self):
        pass

    def view_all(self):
        self.print_title_bar(self.table_name)
        data = db.select(self.table_name).fetchall()
        for record in data:
            print(f'ID: {record[0]}')
            print(f'Question: {record[1]}')
            print()


class Answers(BaseTable):
    def create_table(self, data=None):
        db.create_table('answers', {
            'id': 'integer primary key autoincrement',
            'answer': 'text not null',
        })


class Tips(BaseTable):
    def create_table(self, data=None):
        db.create_table('tips', {
            'id': 'integer primary key autoincrement',
            'tip': 'text not null',
        })


class Notes(BaseTable):
    def create_table(self, data=None):
        db.create_table('notes', {
            'id': 'integer primary key autoincrement',
            'note': 'text not null',
        })

    def view_notes(self, criteria=None):
        db.select(self.table_name, criteria=question_id)
