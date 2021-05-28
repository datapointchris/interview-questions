from database import DatabaseManager
from datetime import datetime
import sys

db = DatabaseManager('interview.db')


def validate_input(input_message, option_map):
    """option_map should be a dictionary of mappings"""
    choice = input(f'{input_message} ').upper()
    while choice not in option_map.keys():
        choice = input(f'{input_message} ').upper()
    return option_map.get(choice)


class BaseTable():
    '''Base class for handling all common table functions'''

    def __init__(self, table_name):
        self.table_name = table_name

    def populate_defaults(self, records):
        for record in records:
            db.add(self.table_name, record)

    def drop_table(self):
        db.drop_table(self.table_name)

    def view(self, selection_criteria):
        user_choice = input(f'Select {selection_criteria.upper()}: ')
        print(f'selection: {selection_criteria}, user_choice: {user_choice}')
        record = db.select(self.table_name, criteria={selection_criteria: user_choice}).fetchone()
# TODO: #79 Make this print programatically
        print(f'ID: {record[0]}')
        print(f'Question: {record[1]}')
        print(f'Answered: {"Y" if record[2] == 1 else "N"}')
        print()

    def view_all(self):
        data = db.select(self.table_name).fetchall()
        for record in data:
            print(record)

    def add(self, data):
        db.add(self.table_name, data)

    def edit(self):
        pass

    def delete(self):
        db.delete()

    def delete_all(self):
        db.delete()

    def reset(self):
        pass

    def print_title_bar(self):
        max_width = 80
        space = max_width - len(self.table_name) - 10
        left_pad = ('⎼' * (space // 2)) + (' ' * 5)
        right_pad = (' ' * 5) + ('⎼' * (space // 2))
        title = f'{left_pad}{self.table_name.upper()}{right_pad}'
        top_border = '⎺' * len(title)
        bottom_border = '⎽' * len(title)
        print('\n'.join([top_border, title, bottom_border, '']))


class Jobs(BaseTable):  # this class and table isn't going to be used in v1.0

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
        record = db.select_random(self.table_name).fetchone()
        print(f'ID: {record[0]}')
        print(f'Question: {record[1]}')
        print()
        print()

# TODO: #76 add get_random_unanswered_question_function

    def get_not_viewed_question(self, data):
        record = db.select_random(self.table_name, data).fetchone()
        print(f'ID: {record[0]}')
        print(f'Question: {record[1]}')
        print()
        print()

    def edit_question(self):
        id = input('ID to Edit: ')
        record = db.select(self.table_name, criteria={'id': id}).fetchone()
        print()
        print(f'ID: {record[0]}')
        print(f'Question: {record[1]}')
        print()
        edited_question = input('Enter the edited question: ')
        answered = validate_input(
            f'Question is answered? (Currently: {"Y" if record[2] == 1 else "N"}), Y/N?', {'Y': 1, 'N': 0})
        update_data = {'question': edited_question, 'answered': answered}
        db.update(self.table_name, {'id': id}, update_data)

    def view_all(self):
        self.print_title_bar()
        data = db.select(self.table_name).fetchall()
# TODO: #78 Automate this so that it gets the columns and prints them
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
