import commands
import os
import subprocess
import sys
import defaults


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    print("\n" * 150)
    subprocess.call(clear, shell=True)
    return (None, None)


def reset_program():
    make_sure = input('Are you sure you want to reset the program? Y/N')
    if make_sure.upper() == 'Y':
        # delete all tables
        # create all tables
        # populate tables with defaults
        print('Program Reset Successfully!')
    else:
        print('That was a close call!')
    return (None, None)


def get_user_input(label, required=True):
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value


class Option:
    def __init__(self, name, menu, command):
        self.name = name
        self.menu = menu
        self.command = command

    def execute(self, return_data):
        if return_data:
            return self.command(return_data)
        return self.command()


class Menu:
    def __init__(self):
        self.current_menu = 'main'
        self._menus = {
            'main': {

                # (name, menu, command)
                '1': Option('Get a Random Question', 'questions', questions.get_random_question),
                '2': Option('Get a Random Unanswered Question', 'questions', questions.get_random_question),
                '3': Option('Questions Menu', 'questions', clear_screen),
                '4': Option('Answers Menu', 'answers', clear_screen),
                '5': Option('Notes Menu', 'notes', clear_screen),
                '6': Option('Tips Menu', 'tips', clear_screen),
                'R': Option('Reset Program to Defaults', 'main', reset_program),
                'Q': Option('Quit Program', 'main', sys.exit)
            },
            'questions': {
                '1': Option('Get a Random Question', 'questions', questions.get_random_question),
                '2': Option('Get a Random Unanswered Question', 'questions', questions.get_random_unanswered_question),
                '3': Option('View Answered Questions', 'questions', questions.view_answered),
                'A': Option('View All Questions', 'questions', questions.view_all_questions),
                'B': Option('View a Question by ID', 'questions', questions.view_question_by_id),
                'C': Option('Add a question', 'questions', questions.add_question),
                'D': Option('Edit a question', 'questions', questions.edit_question),
                'E': Option('Delete a question', 'questions', questions.delete),
                'F': Option('Delete All questions', 'questions', questions.delete_all),
                'G': Option('Reset questions to Default', 'questions', questions.reset_to_default),
                'M': Option('Return to Main Menu', 'main', clear_screen),
                'Q': Option('Quit Program', 'main', sys.exit)
            },
            'single_question': {
                '1': Option('Answer this question', 'questions', answers.add_answer),
                '2': Option('Get a Random Unanswered Question', 'questions', questions.get_random_unanswered_question),
                '3': Option('View Answered Questions', 'questions', questions.view_answered),
                'A': Option('View All Questions', 'questions', questions.view_all_questions),
                'B': Option('View a Question by ID', 'questions', questions.view_question_by_id),
                'C': Option('Add a question', 'questions', questions.add_question),
                'D': Option('Edit a question', 'questions', questions.edit_question),
                'E': Option('Delete a question', 'questions', questions.delete),
                'F': Option('Delete All questions', 'questions', questions.delete_all),
                'G': Option('Reset questions to Default', 'questions', questions.reset_to_default),
                'M': Option('Return to Main Menu', 'main', clear_screen),
                'Q': Option('Quit Program', 'main', sys.exit)
            },
            'answers': {
                'B': Option('View an answer by ID', 'answers', answers.view_answer_by_id),
                'C': Option('Add an answer', 'answers', answers.add_answer),
                'D': Option('Edit an answer', 'answers', answers.edit_answer),
                'E': Option('Delete an answer', 'answers', answers.delete),
                'F': Option('Delete All answers', 'answers', answers.delete_all),
                'G': Option('Reset answers to Default', 'answers', answers.reset_to_default),
                'M': Option('Return to Main Menu', 'main', clear_screen),
                'Q': Option('Quit Program', 'main', sys.exit)
            },
            'notes': {
                'B': Option('View a note by ID', 'notes', notes.view_note_by_id),
                'C': Option('Add a note', 'notes', notes.add_note),
                'D': Option('Edit a note', 'notes', notes.edit_note),
                'E': Option('Delete a note', 'notes', notes.delete),
                'F': Option('Delete All notes', 'notes', notes.delete_all),
                'G': Option('Reset notes to Default', 'notes', notes.reset_to_default),
                'M': Option('Return to Main Menu', 'main', clear_screen),
                'Q': Option('Quit Program', 'main', sys.exit)
            },
            'tips': {
                'B': Option('View a tip by ID', 'tips', tips.view_tip_by_id),
                'C': Option('Add a tip', 'tips', tips.add_tip),
                'D': Option('Edit a tip', 'tips', tips.edit_tip),
                'E': Option('Delete a tip', 'tips', tips.delete),
                'F': Option('Delete All tips', 'tips', tips.delete_all),
                'G': Option('Reset tips to Default', 'tips', tips.reset_to_default),
                'M': Option('Return to Main Menu', 'main', clear_screen),
                'Q': Option('Quit Program', 'main', sys.exit)
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
        submenu = self._menus.get(self.current_menu)
        for key, option in submenu.items():
            print(f'{key} : {option.name}')
            print()


# MAIN PROGRAM


questions = commands.Questions(defaults=defaults.default_questions)
questions.create_table()
questions.populate_defaults()

answers = commands.Answers()
answers.create_table()

tips = commands.Tips()
tips.create_table()

notes = commands.Notes()
notes.create_table()

clear_screen()
menu = Menu()

menu.print_menu()
return_data = None

while True:

    command = menu.get_command()
    clear_screen()
    return_message, return_data = command.execute(return_data=return_data)
    print(return_message)
    menu.print_menu()
