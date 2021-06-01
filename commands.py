from database import DatabaseManager
from datetime import datetime
import sys

db = DatabaseManager('interview.db')




class BaseTable():
    '''Base class for handling all common table functions'''

    def __init__(self, table_name):
        self.table_name = table_name

    def print_title_bar(self, name):
        max_width = 80
        space = max_width - len(name) - 10
        left_pad = ('⎼' * (space // 2)) + (' ' * 5)
        right_pad = (' ' * 5) + ('⎼' * (space // 2))
        title = f'{left_pad}{name.upper()}{right_pad}'
        top_border = '⎺' * len(title)
        bottom_border = '⎽' * len(title)
        print('\n'.join([top_border, title, bottom_border, '']))

    def print_records(self, cursor):
        columns = [tuple[0] for tuple in cursor.description]
        records = cursor.fetchall()
        if records:
            for i, record in enumerate(records):
                for column, record_item in zip(columns, record):
                    print(f'{column.upper()}:  '
                          f'{"Y" if record_item == 1 else "N" if record_item == 0 else record_item}')
                print()
        else:
            print('No matching records found.')
            print()
        print('-' * 80)
        print()

    def populate_defaults(self, records):
        for record in records:
            db.add(self.table_name, record)

    def validate_input(self, input_message, option_map):
        """option_map should be a dictionary of mappings"""
        choice = input(f'{input_message} ').upper()
        while choice not in option_map.keys():
            choice = input(f'{input_message} ').upper()
        return option_map.get(choice)
    
    def view(self, selection_criteria):
        user_choice = input(f'Select {selection_criteria.upper()}: ')
        # print(f'selection: {selection_criteria}, user_choice: {user_choice}')
        cursor = db.select(self.table_name, criteria={selection_criteria: user_choice})
        self.print_title_bar('View by ID')
        self.print_records(cursor)

    def view_all(self):
        cursor = db.select(self.table_name)
        self.print_title_bar(f'View All {self.table_name}')
        self.print_records(cursor)

    def add(self, data):
        input_data = input(f'Enter new question: ')
        table_data = {data: input_data}
        db.add(self.table_name, table_data)

    def edit(self):
        pass

    def delete(self):
        db.delete()

    def delete_all(self):
        db.delete()

    def reset(self):
        pass

    def drop_table(self):
        db.drop_table(self.table_name)


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

    def get_random_question(self, data=None):
        if data:
            cursor = db.select_random(self.table_name, data)
            name = 'Random Unanswered Question'
        else:
            cursor = db.select_random(self.table_name)
            name = 'Random Question'
        self.print_title_bar(name)
        self.print_records(cursor)

    def view_answered(self):
        cursor = db.select(self.table_name, criteria={'answered': 1})
        self.print_title_bar('Answered Questions')
        self.print_records(cursor)

    def add_question(self):
        input_data = input(f'Enter new question: ')
        table_data = {'question': input_data, 'answered': 0}
        db.add(self.table_name, table_data)

    def edit_question(self):
        id = input('ID to Edit: ')
        record = db.select(self.table_name, criteria={'id': id}).fetchone()
        print()
        print(f'ID: {record[0]}')
        print(f'Question: {record[1]}')
        print()
        edited_question = input('Enter the edited question: ')
        answered = self.validate_input(
            f'Question is answered? (Currently: {"Y" if record[2] == 1 else "N"}), Y/N?', {'Y': 1, 'N': 0})
        update_data = {'id': id, 'question': edited_question, 'answered': answered}
        db.update(self.table_name, {'id': id}, update_data)


class Answers(BaseTable):
    def create_table(self, data=None):
        db.create_table('answers', {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'answer': 'text not null',
        })


class Tips(BaseTable):
    def create_table(self, data=None):
        db.create_table('tips', {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'tip': 'text not null',
        })


class Notes(BaseTable):
    def create_table(self, data=None):
        db.create_table('notes', {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'note': 'text not null',
        })

    def view_notes(self, criteria=None):
        db.select(self.table_name, criteria=question_id)
