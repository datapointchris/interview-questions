import random
import commands
import os
import sys
import defaults


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


class Option:
    def __init__(self, name, menu, command, data):
        self.name = name
        self.menu = menu
        self.command = command
        self.data = data

    def execute(self):
        if self.data:
            return self.command(self.data)
        return self.command()


class Menu():
    def __init__(self):
        self._menus = {
            'main': {

                # (name, command, data)
                'M': Option('Print Main Menu', 'main', print_menu, None),
                '1': Option('Get a Random Question', 'questions', four, None),
                '2': Option('Get a Random Unanswered Question', 'questions', five, None),
                'J': Option('View All Questions', 'questions', questions.view_all, None),
                'R': Option('Reset Program to Defaults', 'main', reset_program, None),
                'Q': Option('Quit Program', 'main', sys.exit, None)
            },
            'questions': {
                'A': Option('View All Questions', 'questions', questions.view_all, None),
                'B': Option('View a Question by ID', 'questions', questions.view, None),
                'C': Option('Add a question', 'questions', questions.add, None),
                'D': Option('Edit a question', 'questions', questions.edit, None),
                'E': Option('Delete a question', 'questions', questions.delete, None),
                'F': Option('Delete All questions', 'questions', questions.delete_all, None),
                'G': Option('Reset questions to Default', 'questions', questions.reset, None),
                'M': Option('Return to Main Menu', 'main', print_menu, None),
                'Q': Option('Quit Program', 'main', sys.exit, None)
            },
            'answers': {
                'A': Option('View answers Listing', 'answers', answers.view_all, None),
                'B': Option('View a Specific answer by ID', 'answers', answers.view, None),
                'C': Option('Add a answer', 'answers', answers.add, None),
                'D': Option('Edit a answer', 'answers', answers.edit, None),
                'E': Option('Delete a answer', 'answers', answers.delete, None),
                'F': Option('Delete All answers', 'answers', answers.delete_all, None),
                'G': Option('Reset answers to Default', 'answers', answers.reset, None),
                'M': Option('Return to Main Menu', 'main', print_menu, None),
                'Q': Option('Quit Program', 'main', sys.exit, None)
            },
            'notes': {
                'A': Option('View notes Listing', 'notes', notes.view_all, None),
                'B': Option('View a Specific note by ID', 'notes', notes.view, None),
                'C': Option('Add a note', 'notes', notes.add, None),
                'D': Option('Edit a note', 'notes', notes.edit, None),
                'E': Option('Delete a note', 'notes', notes.delete, None),
                'F': Option('Delete All notes', 'notes', notes.delete_all, None),
                'G': Option('Reset notes to Default', 'notes', notes.reset, None),
                'M': Option('Return to Main Menu', 'main', print_menu, None),
                'Q': Option('Quit Program', 'main', sys.exit, None)
            },
            'tips': {
                'A': Option('View tips Listing', 'tips', tips.view_all, None),
                'B': Option('View a Specific tip by ID', 'tips', tips.view, None),
                'C': Option('Add a tip', 'tips', tips.add, None),
                'D': Option('Edit a tip', 'tips', tips.edit, None),
                'E': Option('Delete a tip', 'tips', tips.delete, None),
                'F': Option('Delete All tips', 'tips', tips.delete_all, None),
                'G': Option('Reset tips to Default', 'tips', tips.reset, None),
                'M': Option('Return to Main Menu', 'main', print_menu, None),
                'Q': Option('Quit Program', 'main', sys.exit, None)
            },
        }

    def get_command(self, menu, chosen_option):
        submenu = self._menus.get(menu)
        command = submenu[chosen_option]
        return command

# MAIN PROGRAM


def print_menu(name):
    clear_screen()
    print()
    print(f'---------- {name.upper()} MENU ----------')
    print()
    submenu = menu._menus.get(current_menu)
    for key, option in submenu.items():
        print(f'{key} : {option.name}')
        print()


def return_to_main_menu():
    pass
    # menu prints automatically


def four():
    print(4)


def five():
    return {'5': 'yeah five'}


def reset_program():
    make_sure = input('Are you sure you want to reset the program? Y/N')
    if make_sure.upper() == 'Y':
        # delete all tables
        # create all tables
        # populate tables with defaults
        print('Program Reset Successfully!')
    else:
        print('That was a close call!')


questions = commands.Questions(table_name='questions')
questions.create_table()
questions.populate_defaults(defaults.default_questions)

answers = commands.Answers(table_name='answers')
answers.create_table()

tips = commands.Tips(table_name='tips')
tips.create_table()

notes = commands.Notes(table_name='notes')
notes.create_table()


menu = Menu()

current_menu = 'main'
print_menu(current_menu)


while True:
    chosen_option = input('Choose option: ')
    # TODO: #70 Validate Input
    command = menu.get_command(current_menu, chosen_option)
    current_menu = command.menu
    
    # For Debugging ONLY
    # print()
    # print('New Menu', command.menu)
    # print('Command Question Class', command)
    # print('Command', command.command)
    # print('Data', command.data)
    # print()

    command.execute()
    print('=' * 25)
    print_menu(current_menu)
