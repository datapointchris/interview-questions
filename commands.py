from database import DatabaseManager
from printer import Printer
from datetime import datetime
import sys

db = DatabaseManager('interview.db')
printer = Printer()


class BaseTable():
    '''Base class for handling all common table functions'''

    def __init__(self, defaults):
        self.defaults = defaults

    def view_by_id(self, id=None, skip_title=None):
        if id is None:
            id = input('Select ID: ')
        cursor = db.select(self.table_name, criteria={'id': id})
        if skip_title is None:
            printer.print_title_bar('View by ID')
        printer.print_records(cursor)

    def validate_input(self, input_message, option_map):
        """option_map should be a dictionary of mappings"""
        choice = input(f'{input_message} ').upper()
        while choice not in option_map.keys():
            choice = input(f'{input_message} ').upper()
        return option_map.get(choice)

    def populate_defaults(self):
        for record in self.defaults:
            db.add(self.table_name, record)

    def delete(self):
        delete_id = input('ID to delete: ')
        db.delete(self.table_name, {'id': delete_id})

    def delete_all(self):
        self.drop_table()
        self.create_table()

    def reset_to_default(self):
        self.delete_all()
        if self.defaults:
            self.populate_defaults()

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

    def __init__(self, defaults=None):
        super().__init__(defaults)
        self.table_name = 'questions'

    def create_table(self):
        db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'question': 'text not null',
            'answered': 'integer'
        })

    def get_random_question(self, return_data=None):
        cursor = db.select_random(self.table_name)
        record = cursor.fetchone()
        question_id = record[0]
        printer.print_title_bar('Random Question')
        printer.print_records(record, print_function=printer.question_printer)
        return_message = ''
        return_data = {'question_id': question_id}
        return (return_message, return_data)

    def get_random_unanswered_question(self, return_data=None):
        cursor = db.select_random(self.table_name, criteria={'answered': 0})
        record = cursor.fetchone()
        question_id = record[0]
        printer.print_title_bar('Random Unanswered Question')
        printer.print_records(record, print_function=printer.question_printer)
        return_message = ''
        return_data = {'question_id': question_id}
        return (return_message, return_data)

    def view_answered(self, return_data=None):
        cursor = db.select(self.table_name, criteria={'answered': 1})
        records = cursor.fetchall()
        printer.print_title_bar('Answered Questions')
        printer.print_records(records, print_function=printer.question_printer)
        return_message = ''
        return_data = None
        return (return_message, return_data)

    def view_all_questions(self, return_data=None):
        cursor = db.select(self.table_name)
        records = cursor.fetchall()
        printer.print_title_bar('View all questions')
        printer.print_records(records, print_function=printer.question_printer)
        return_message = ''
        return_data = None
        return (return_message, return_data)

    def view_question_by_id(self, return_data=None):
        id = input('ID to View: ')
        cursor = db.select(table_name=self.table_name, criteria={'id': id})
        record = cursor.fetchone()
        printer.print_title_bar('View by ID')
        printer.print_records(record, print_function=printer.question_printer)
        return_message = ''
        return_data = {'question_id': id}
        return (return_message, return_data)

    def add_question(self, return_data=None):
        input_data = input('Enter new question: ')
        table_data = {'question': input_data, 'answered': 0}
        return_cursor = db.add(self.table_name, table_data)
        inserted_id = return_cursor.lastrowid
        cursor = db.select(self.table_name, criteria={'id': inserted_id})
        record = cursor.fetchone()
        print()
        print(f'~~ Successfully Added Question ~~')
        printer.print_records(record, print_function=printer.question_printer)
        # question_id, question, answered = record
        # return_message = (
        #     f'~~ Successfully Added Question ~~\n'
        #     f'ID: {question_id}\n'
        #     f'Question: {question}\n'
        #     f'Answered: {"Y" if answered == 1 else "N" if answered == 0 else answered}\n'
        # )
        return_message = None
        return_data = None
        return (return_message, return_data)

    def edit_question(self, data):
        if data:
            question_id = data.get('question_id')
        if question_id is None:
            question_id = input('Enter question ID: ')
        record = db.select(self.table_name, criteria={'id': id}).fetchone()
        printer.question_printer(record)
        edited_question = input('Enter the edited question: ')
        answered = self.validate_input(
            f'Question is answered? (Currently: {"Y" if record[2] == 1 else "N"}), Y/N?', {'Y': 1, 'N': 0})
        update_data = {'id': id, 'question': edited_question, 'answered': answered}
        db.update(self.table_name, {'id': id}, update_data)
        return_message = '~~ Successfully edited question ~~'
        return_data = None
        return (return_message, return_data)


class Answers(BaseTable):

    def __init__(self, defaults=None):
        super().__init__(defaults)
        self.table_name = 'answers'

    def create_table(self):
        db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'answer': 'text not null',
        })

    def view_answer_by_id(self, data):
        id = input('ID to View: ')
        answer_record = db.select(self.table_name, criteria={'id': id}).fetchone()
        if answer_record:
            answer_id, question_id, answer = answer_record
            question_record = db.select(table_name='questions',
                                        criteria={'id': question_id}).fetchone()
            printer.print_title_bar('View by ID')
            print('Question for Reference:')
            printer.question_printer(record=question_record)
            print()
            printer.answer_printer(record=answer_record)
            print()
        else:
            print('No matching records found.')
            print()
        print('-' * 80)
        print()

    def add_answer(self, data):
        question_id = data.get('question_id')
        if question_id is None:
            question_id = input('Enter question ID: ')

        print()
        new_answer = input('Enter new answer: ')
        table_data = {'question_id': question_id, 'answer': new_answer}
        db.add(self.table_name, table_data)

    def edit_answer(self, data):
        id = input('ID to Edit: ')
        answer_record = db.select(self.table_name, criteria={'id': id}).fetchone()
        if answer_record:
            answer_id, question_id, answer = answer_record
            question_record = db.select(table_name='questions',
                                        criteria={'id': question_id}).fetchone()
            printer.print_title_bar('View by ID')
            print('Question for Reference:')
            printer.question_printer(record=question_record)
            print()
            printer.answer_printer(record=answer_record)
            print()
            edited_answer = input('Enter the new answer: ')
            update_data = {'id': answer_id, 'question_id': question_id, 'answer': edited_answer}
            db.update(self.table_name, {'id': id}, update_data)
        else:
            print('No matching records found.')
            print()
        print('-' * 80)
        print()


class Notes(BaseTable):

    def __init__(self, defaults=None):
        super().__init__(defaults)
        self.table_name = 'notes'

    def create_table(self):
        db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'note': 'text not null',
        })

    def view_note_by_id(self, data):
        id = input('ID to View: ')
        record = db.select(self.table_name, criteria={'id': id}).fetchone()
        printer.print_title_bar('View by ID')
        if record:
            print()
            print('Question for Reference:')
            print()
            print_question = data.get('func')
            print_question(id=record[1], skip_title=True)
            print()
            self.view_by_id(id=id, skip_title=True)
            print()
        else:
            print('No matching records found.')
            print()
        print('-' * 80)
        print()

    def add_note(self, data):
        question_id = data.get('question_id')
        if question_id is None:
            question_id = input('Enter question ID: ')
        print_question = data.get('func')
        print_question(id=question_id, skip_title=True)
        print()
        new_note = input('Enter new note: ')
        table_data = {'question_id': question_id, 'note': new_note}
        db.add(self.table_name, table_data)

    def edit_note(self, data):
        id = input('ID to Edit: ')
        record = db.select(self.table_name, criteria={'id': id}).fetchone()
        print()
        print('Question for Reference:')
        print()
        print_question = data.get('func')
        print_question(id=record[1], skip_title=True)
        print()
        self.view_by_id(id=id, skip_title=True)
        print()
        edited_note = input('Enter the new note: ')

        update_data = {'id': id, 'question_id': record[1], 'note': edited_note}
        db.update(self.table_name, {'id': id}, update_data)


class Tips(BaseTable):

    def __init__(self, defaults=None):
        super().__init__(defaults)
        self.table_name = 'tips'

    def create_table(self):
        db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'tip': 'text not null',
        })

    def view_tip_by_id(self, data):
        id = input('ID to View: ')
        record = db.select(self.table_name, criteria={'id': id}).fetchone()
        printer.print_title_bar('View by ID')
        if record:
            print()
            print('Question for Reference:')
            print()
            print_question = data.get('func')
            print_question(id=record[1], skip_title=True)
            print()
            self.view_by_id(id=id, skip_title=True)
            print()
        else:
            print('No matching records found.')
            print()
        print('-' * 80)
        print()

    def add_tip(self, data):
        question_id = data.get('question_id')
        if question_id is None:
            question_id = input('Enter question ID: ')
        print_question = data.get('func')
        print_question(id=question_id, skip_title=True)
        print()
        new_tip = input('Enter new tip: ')
        table_data = {'question_id': question_id, 'tip': new_tip}
        db.add(self.table_name, table_data)

    def edit_tip(self, data):
        id = input('ID to Edit: ')
        record = db.select(self.table_name, criteria={'id': id}).fetchone()
        print()
        print('Question for Reference:')
        print()
        print_question = data.get('func')
        print_question(id=record[1], skip_title=True)
        print()
        self.view_by_id(id=id, skip_title=True)
        print()
        edited_tip = input('Enter the new tip: ')

        update_data = {'id': id, 'question_id': record[1], 'tip': edited_tip}
        db.update(self.table_name, {'id': id}, update_data)
