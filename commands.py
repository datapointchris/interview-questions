from database import DatabaseManager
from printer import Printer
from datetime import datetime
import sys

db = DatabaseManager('interview.db')
printer = Printer()


def get_valid_id(prompt, table_name):
    id = input(f'{prompt}')
    answer = db.id_exists(id, table_name).fetchone()[0]
    while answer < 1:
        print(f'Invalid ID: {id}')
        id = input(f'{prompt}')
        answer = db.id_exists(id, table_name).fetchone()[0]
    return id


def validate_input(input_message, option_map):
    """option_map should be a dictionary of mappings"""
    choice = input(f'{input_message} ').upper()
    while choice not in option_map.keys():
        choice = input(f'{input_message} ').upper()
    return option_map.get(choice)


class BaseTable():
    '''Base class for handling all common table functions'''

    def __init__(self, defaults):
        self.defaults = defaults

    def _populate_defaults(self):
        for record in self.defaults:
            db.add(self.table_name, record)

    def delete(self, return_data=None):
        printer.print_title_bar('Delete by ID')
        delete_id = input('ID to Delete: ')
        cursor = db.select(table_name=self.table_name, criteria={'id': delete_id})
        record = cursor.fetchone()
        if record is not None:
            db.delete(self.table_name, {'id': delete_id})
            print()
            print(f'~~ Successfully Deleted {self.table_name[:-1:].capitalize()} ~~')
            printer.print_records(record, self.print_function)
        else:
            printer.print_no_records()
        return None

    def delete_all(self, return_data=None):
        printer.print_title_bar(f'Delete All {self.table_name}')
        self._drop_table()
        self.create_table()
        print(f'~~ Successfully Deleted All {self.table_name.capitalize()} ~~')
        return None

    def reset_to_default(self, return_data=None):
        printer.print_title_bar(f'Reset All {self.table_name} to Default')
        self._drop_table()
        self.create_table()
        if self.defaults:
            self._populate_defaults()
        print(f'~~ Successfully Set All {self.table_name.capitalize()} to Default ~~')
        return None

    def _drop_table(self, return_data=None):
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

    def __init__(self, defaults=None, print_fuction=printer.question_printer):
        super().__init__(defaults)
        self.table_name = 'questions'
        self.print_function = print_fuction

    def create_table(self):
        db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'question': 'text not null',
            'answered': 'integer'
        })

    def get_random_question(self, return_data=None):
        printer.print_title_bar('Random Question')
        cursor = db.select_random(self.table_name)
        record = cursor.fetchone()
        if record is not None:
            question_id = record[0]
            printer.print_records(record, self.print_function)
        else:
            printer.print_no_records()
            question_id = None
        return_data = {'question_id': question_id}
        return return_data

    def get_random_unanswered_question(self, return_data=None):
        printer.print_title_bar('Random Unanswered Question')
        cursor = db.select_random(self.table_name, criteria={'answered': 0})
        record = cursor.fetchone()
        if record is not None:
            question_id = record[0]
            printer.print_records(record, self.print_function)
        else:
            printer.print_no_records()
            question_id = None
        return_data = {'question_id': question_id}
        return return_data

    def view_answered(self, return_data=None):
        printer.print_title_bar('Answered Questions')
        cursor = db.select(self.table_name, criteria={'answered': 1})
        records = cursor.fetchall()
        if records:
            printer.print_records(records, self.print_function)
        else:
            printer.print_no_records()
        return None

    def view_all_questions(self, return_data=None):
        printer.print_title_bar('View all questions')
        cursor = db.select(self.table_name)
        records = cursor.fetchall()
        if records:
            printer.print_records(records, self.print_function)
        else:
            printer.print_no_records()
        return None

    def view_question_by_id(self, return_data=None):
        printer.print_title_bar('View by ID')
        id = input('ID to View: ')
        cursor = db.select(self.table_name, criteria={'id': id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, self.print_function)
        else:
            printer.print_no_records()
        return_data = {'question_id': id}
        return return_data

    def add_question(self, return_data=None):
        printer.print_title_bar('Add Question')
        input_data = input('Enter new question: ')
        table_data = {'question': input_data, 'answered': 0}
        return_cursor = db.add(self.table_name, table_data)
        inserted_id = return_cursor.lastrowid
        new_cursor = db.select(self.table_name, criteria={'id': inserted_id})
        new_record = new_cursor.fetchone()
        print()
        print('~~ Successfully Added Question ~~')
        printer.print_records(new_record, self.print_function)
        return None

    def edit_question(self, return_data=None):
        printer.print_title_bar('Edit Question')
        if return_data is not None:
            question_id = return_data.get('question_id')
        else:
            question_id = input('Enter question ID: ')
        cursor = db.select(self.table_name, criteria={'id': question_id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, self.print_function)
            edited_question = input('Enter the edited question: ')
            answered = validate_input(
                f'Question is answered? (Currently: {"Y" if record[2] == 1 else "N"}), Y/N?', {'Y': 1, 'N': 0})
            update_data = {'id': question_id, 'question': edited_question, 'answered': answered}
            db.update(self.table_name, {'id': question_id}, update_data)
            edited_cursor = db.select(self.table_name, criteria={'id': question_id})
            edited_record = edited_cursor.fetchone()
            print()
            print('~~ Successfully Edited Question ~~')
            printer.print_records(edited_record, self.print_function)
        else:
            printer.print_no_records()
        return None


class Answers(BaseTable):

    def __init__(self, defaults=None, print_fuction=printer.answer_printer):
        super().__init__(defaults)
        self.table_name = 'answers'
        self.print_function = print_fuction

    def create_table(self):
        db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'answer': 'text not null',
        })

    def view_answer_by_id(self, return_data=None):
        printer.print_title_bar('View by ID')
        id = input('ID to View: ')
        print()
        cursor = db.select(self.table_name, criteria={'id': id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, self.print_function)
            question_id = record[1]
            question_cursor = db.select('questions', criteria={'id': question_id})
            question_record = question_cursor.fetchone()
            print('Question for Reference:')
            print(question_record[1])
        else:
            printer.print_no_records()
        return None

    def add_answer(self, return_data=None):
        printer.print_title_bar('Add Answer')
        if return_data is not None:
            question_id = return_data.get('question_id')
        else:
            question_id = input('Enter question ID: ')
        print()
        cursor = db.select('questions', criteria={'id': question_id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, printer.question_printer)
            new_answer = input('Enter new answer: ')
            table_data = {'question_id': question_id, 'answer': new_answer}
            return_cursor = db.add(self.table_name, table_data)
            inserted_id = return_cursor.lastrowid
            new_cursor = db.select(self.table_name, criteria={'id': inserted_id})
            new_record = new_cursor.fetchone()
            print()
            print('~~ Successfully Added Answer ~~')
            printer.print_records(new_record, self.print_function)
        else:
            printer.print_no_records()
        return None

    def edit_answer(self, return_data=None):
        printer.print_title_bar('Edit Answer')
        if return_data is not None:
            id = return_data.get('answer_id')
        else:
            id = input('Enter Answer ID: ')
        cursor = db.select(self.table_name, criteria={'id': id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, self.print_function)
            answer_id, question_id, answer = record
            question_cursor = db.select('questions', criteria={'id': question_id})
            question_record = question_cursor.fetchone()
            print('Question for Reference:')
            print(question_record[1])
            print()
            edited_answer = input('Enter the new answer: ')
            update_data = {'id': answer_id, 'question_id': question_id, 'answer': edited_answer}
            db.update(self.table_name, {'id': answer_id}, update_data)
            edited_cursor = db.select(self.table_name, criteria={'id': answer_id})
            edited_record = edited_cursor.fetchone()
            print()
            print('~~ Successfully Edited Question ~~')
            printer.print_records(edited_record, self.print_function)
        else:
            printer.print_no_records()
        return None


class Notes(BaseTable):

    def __init__(self, defaults=None, print_fuction=printer.note_printer):
        super().__init__(defaults)
        self.table_name = 'notes'
        self.print_function = print_fuction

    def create_table(self):
        db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'note': 'text not null',
        })

    def view_note_by_id(self, return_data=None):
        printer.print_title_bar('View by ID')
        id = input('ID to View: ')
        print()
        cursor = db.select(self.table_name, criteria={'id': id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, self.print_function)
            question_id = record[1]
            question_cursor = db.select('questions', criteria={'id': question_id})
            question_record = question_cursor.fetchone()
            print('Question for Reference:')
            print(question_record[1])
        else:
            printer.print_no_records()
        return None

    def add_note(self, return_data=None):
        printer.print_title_bar('Add note')
        if return_data is not None:
            question_id = return_data.get('question_id')
        else:
            question_id = input('Enter question ID: ')
        print()
        cursor = db.select('questions', criteria={'id': question_id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, printer.question_printer)
            new_note = input('Enter new note: ')
            table_data = {'question_id': question_id, 'note': new_note}
            return_cursor = db.add(self.table_name, table_data)
            inserted_id = return_cursor.lastrowid
            new_cursor = db.select(self.table_name, criteria={'id': inserted_id})
            new_record = new_cursor.fetchone()
            print()
            print('~~ Successfully Added note ~~')
            printer.print_records(new_record, self.print_function)
        else:
            printer.print_no_records()
        return None

    def edit_note(self, return_data=None):
        printer.print_title_bar('Edit note')
        if return_data is not None:
            id = return_data.get('note_id')
        else:
            id = input('Enter note ID: ')
        cursor = db.select(self.table_name, criteria={'id': id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, self.print_function)
            note_id, question_id, note = record
            question_cursor = db.select('questions', criteria={'id': question_id})
            question_record = question_cursor.fetchone()
            print('Question for Reference:')
            print(question_record[1])
            print()
            edited_note = input('Enter the new note: ')
            update_data = {'id': note_id, 'question_id': question_id, 'note': edited_note}
            db.update(self.table_name, {'id': note_id}, update_data)
            edited_cursor = db.select(self.table_name, criteria={'id': note_id})
            edited_record = edited_cursor.fetchone()
            print()
            print('~~ Successfully Edited Question ~~')
            printer.print_records(edited_record, self.print_function)
        else:
            printer.print_no_records()
        return None


class Tips(BaseTable):

    def __init__(self, defaults=None, print_fuction=printer.tip_printer):
        super().__init__(defaults)
        self.table_name = 'tips'
        self.print_function = print_fuction

    def create_table(self):
        db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'question_id': 'integer not null',
            'tip': 'text not null',
        })

    def view_tip_by_id(self, return_data=None):
        printer.print_title_bar('View by ID')
        id = input('ID to View: ')
        print()
        cursor = db.select(self.table_name, criteria={'id': id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, self.print_function)
            question_id = record[1]
            question_cursor = db.select('questions', criteria={'id': question_id})
            question_record = question_cursor.fetchone()
            print('Question for Reference:')
            print(question_record[1])
        else:
            printer.print_no_records()
        return None

    def add_tip(self, return_data=None):
        printer.print_title_bar('Add tip')
        if return_data is not None:
            question_id = return_data.get('question_id')
        else:
            question_id = input('Enter question ID: ')
        print()
        cursor = db.select('questions', criteria={'id': question_id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, printer.question_printer)
            new_tip = input('Enter new tip: ')
            table_data = {'question_id': question_id, 'tip': new_tip}
            return_cursor = db.add(self.table_name, table_data)
            inserted_id = return_cursor.lastrowid
            new_cursor = db.select(self.table_name, criteria={'id': inserted_id})
            new_record = new_cursor.fetchone()
            print()
            print('~~ Successfully Added tip ~~')
            printer.print_records(new_record, self.print_function)
        else:
            printer.print_no_records()
        return None

    def edit_tip(self, return_data=None):
        printer.print_title_bar('Edit tip')
        if return_data is not None:
            id = return_data.get('tip_id')
        else:
            id = input('Enter tip ID: ')
        cursor = db.select(self.table_name, criteria={'id': id})
        record = cursor.fetchone()
        if record is not None:
            printer.print_records(record, self.print_function)
            tip_id, question_id, tip = record
            question_cursor = db.select('questions', criteria={'id': question_id})
            question_record = question_cursor.fetchone()
            print('Question for Reference:')
            print(question_record[1])
            print()
            edited_tip = input('Enter the new tip: ')
            update_data = {'id': tip_id, 'question_id': question_id, 'tip': edited_tip}
            db.update(self.table_name, {'id': tip_id}, update_data)
            edited_cursor = db.select(self.table_name, criteria={'id': tip_id})
            edited_record = edited_cursor.fetchone()
            print()
            print('~~ Successfully Edited Question ~~')
            printer.print_records(edited_record, self.print_function)
        else:
            printer.print_no_records()
        return None