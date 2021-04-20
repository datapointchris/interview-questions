from database import DatabaseManager
from datetime import datetime


db = DatabaseManager('interview.db')

class QuitCommand():
    def execute(self, data=None):
        sys.exit()

class BaseTable():
    '''Base class for handling all common table functions'''

    def __init__(self, table_name):
        self.table_name = table_name

    def drop_table():
        db.drop_table(self.table_name)

    def view(criteria):
        db.select(self.table_name, criteria=criteria)

    def view_all():
        db.select(self.table_name, criteria=criteria)

    def add(data):
        db.add(self.table_name, data)

    def edit(criteria):
        db.update(self.table_name, data)

    def delete():
        db.delete()

    def delete_all():
        db.delete()

    def reset():
        pass


class Jobs():

    def create_table(self, data=None):
        db.create_table('jobs', {
            'id': 'integer primary key autoincrement',
            'job': 'text not null',
            'date_added': 'text'
        })

    def view_practiced():
        db.select('jobs', criteria={'reviewed': True})

    def view_not_practiced():
        db.select('jobs', criteria={'reviewed': False})


class Questions():

    def create_table(self, data=None):
        db.create_table('questions', {
            'id': 'integer primary key autoincrement',
            'question': 'text not null',
            'answered': 'integer'
        })

    def view_answered():
        pass

    def view_not_answered():
        pass


class Answers():
    def create_table(self, data=None):
        db.create_table('answers', {
            'id': 'integer primary key autoincrement',
            'answer': 'text not null',
        })


class Tips():
    def create_table(self, data=None):
        db.create_table('tips', {
            'id': 'integer primary key autoincrement',
            'tip': 'text not null',
        })


class Notes():
    def create_table(self, data=None):
        db.create_table('notes', {
            'id': 'integer primary key autoincrement',
            'note': 'text not null',
        })

    def view_notes(self, criteria=None):
        db.select(self.table_name, criteria=question_id)
