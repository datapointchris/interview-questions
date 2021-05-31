import commands
import os
import subprocess
import sys
import defaults


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    print("\n" * 150)
    subprocess.call(clear, shell=True)


def reset_program():
    make_sure = input('Are you sure you want to reset the program? Y/N')
    if make_sure.upper() == 'Y':
        # delete all tables
        # create all tables
        # populate tables with defaults
        print('Program Reset Successfully!')
    else:
        print('That was a close call!')


def get_user_input(label, required=True):
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value


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


class Menu:
    def __init__(self):
        self.current_menu = 'main'
        self._menus = {
            'main': {

                # (name, menu, command, data)
                '5': Option('Questions Menu', 'questions', clear_screen, None),
                '1': Option('Get a Random Question', 'questions', questions.get_random_question, None),
                '2': Option('Get a Random Unanswered Question',
                            'questions',
                            questions.get_random_question,
                            {'answered': 0}),
                'J': Option('View All Questions', 'questions', questions.view_all, None),
                'R': Option('Reset Program to Defaults', 'main', reset_program, None),
                'Q': Option('Quit Program', 'main', sys.exit, None)
            },
            'questions': {
                '1': Option('Get a Random Question', 'questions', questions.get_random_question, None),
                '2': Option('Get a Random Unanswered Question',
                            'questions',
                            questions.get_random_question,
                            {'answered': 0}),
                'A': Option('View All Questions', 'questions', questions.view_all, None),
                'B': Option('View a Question by ID', 'questions', questions.view, 'id'),
                'C': Option('Add a question', 'questions', questions.add, None),
                'D': Option('Edit a question',
                            'questions',
                            questions.edit_question,
                            None),
                'E': Option('Delete a question', 'questions', questions.delete, None),
                'F': Option('Delete All questions', 'questions', questions.delete_all, None),
                'G': Option('Reset questions to Default', 'questions', questions.reset, None),
                'M': Option('Return to Main Menu', 'main', clear_screen, None),
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
                'M': Option('Return to Main Menu', 'main', clear_screen, None),
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
                'M': Option('Return to Main Menu', 'main', clear_screen, None),
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
                'M': Option('Return to Main Menu', 'main', clear_screen, 'main'),
                'Q': Option('Quit Program', 'main', sys.exit, None)
            },
        }

    def _option_choice_is_valid(self, choice, options):
        return choice in options

    def get_command(self):
        submenu = self._menus.get(self.current_menu)
        choice = input('Choose option: ').upper()
        while not self._option_choice_is_valid(choice, options=submenu):
            print()
            print(f'Invalid option: "{choice}"')
            print()
            choice = input('Choose option: ').upper()
        command = submenu.get(choice)
        self.current_menu = command.menu
        return command

    def print_menu(self):
        border = '⑊ '
        width = (80 - len(self.current_menu)) // 6
        padding = 5
        menu_string = f'{border*width}{" "*padding}{self.current_menu.upper()} MENU{" "*padding}{border*width}'
        q, r = divmod(len(menu_string), len(border))
        adjusted_menu_string = f'{border*width}{" "*padding}{self.current_menu.upper()} MENU{" "*padding}{" "*r}{border*width}'
        print(border * (q + r))
        print(' ' + adjusted_menu_string)
        print('  ' + border * (q + r))
        print()
        submenu = menu._menus.get(self.current_menu)
        for key, option in submenu.items():
            print(f'{key} : {option.name}')
            print()


# MAIN PROGRAM


questions = commands.Questions(table_name='questions')
questions.create_table()
questions.populate_defaults(defaults.default_questions)

answers = commands.Answers(table_name='answers')
answers.create_table()

tips = commands.Tips(table_name='tips')
tips.create_table()

notes = commands.Notes(table_name='notes')
notes.create_table()

clear_screen()
menu = Menu()

menu.print_menu()


while True:

    command = menu.get_command()
    clear_screen()
    command.execute()
    menu.print_menu()
