import random
import commands
from collections import namedtuple
import os


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


interview_questions = {
    'Q01': 'Tell me about yourself.',
    'Q02': 'Run through your resume for me.',
    'Q03': 'Why did you choose data science?',
    'Q04': 'Why did you switch to coding?',
    'Q05': 'Tell me about a time you dealt with an ambiguous situation.',
    'Q06': 'Where do you see yourself in five years?',
    'Q07': 'What kind of leadership style do you prefer?',
    'Q08': 'What is your greatest strength?',
    'Q09': 'What is a weakness you have improved?',
    'Q10': 'Tell me about yourself.',
    'Q11': 'Describe a time you had to work with a difficult coworker.',
    'Q12': 'Describe a time you had to work as part of a team.',
    'Q13': 'Tell me about a time you had to meet a strict deadline.',
    'Q14': 'What is your greatest weakness?',
    'Q15': 'What is your greatest professional achievement?',
    'Q16': 'Tell me about a challenge you faced at work.',
    'Q17': 'How would your previous bosses describe you?',
    'Q18': 'Tell me about a time you demonstrated leadership skills.',
    'Q19': 'Describe a time you had a conflict with a customer.',
    'Q20': 'Tell me about yourself',
    'Q21': 'Tell me about a time you disagreed with your boss.',
    'Q22': 'What type of work environment do you prefer?',
    'Q23': 'How do you deal with pressure or stress?',
    'Q24': 'What should I know that is not on your resume?',
    'Q25': 'Why are you the best candidate for this position?',
    'Q26': 'Describe your dream job.',
    'Q27': 'Tell me about a difficult decision you have made professionally.',
    'Q28': 'What do you like to do outside of work?',
    'Q29': 'Tell me about a time you went above and beyond.',
    'Q30': 'Tell me about yourself',
    'Q31': 'What has been your greatest failure?',
    'Q32': 'Discuss your resume.',
    'Q33': 'Discuss your education.',
    'Q34': 'What motivates you?',
    'Q35': 'What can you offer us that other candidates cannot?',
}

# try:
#     with open('answered.txt', 'r') as ans:
#         answered = ans.read().splitlines()
# except Exception as e:
#     print(e)
#     answered = []

# not_answered = [q for q in questions.keys() if q not in answered]

# try:
#     selected = random.choice(not_answered)
#     print(selected + ':')
#     print(questions[selected])

#     with open('answered.txt', 'a') as ans:
#         ans.write(f'\n{selected}')
# except IndexError:
#     print('CONGRATULATIONS!!!')
#     print('Answered All Questions!!')
#     print('Are you employed yet???')


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


class Questions(commands.Questions):
    def __init__(self, name):
        self.name = name
        super().__init__(table_name=name)


class Menu():
    def __init__(self):
        self._menus = {
            'main': {

                # (name, command, data)
                'M': Option('Print Main Menu', 'main', print_menu, 'main'),
                '1': Option('Get a Random Question', 'questions', four, None),
                '2': Option('Get a Random Unanswered Question', 'questions', five, None),
                'J': Option('View All Questions', 'questions', questions.view_all, None),
                'R': Option('Reset Program to Defaults', 'main', print_menu, 'jobs'),
                'Q': Option('Quit Program', 'main', commands.QuitCommand, None)
            },
            # 'questions': {
            #     'A': Option('View All Questions', 'questions', questions.view_all, None),
            #     'B': Option('View a Question by ID', 'questions', questions.view, None),
            #     'C': Option('Add a question', 'questions', questions.add, None),
            #     'D': Option('Edit a question', 'questions', questions.edit, None),
            #     'E': Option('Delete a question', 'questions', questions.delete, None),
            #     'F': Option('Delete All questions', 'questions', questions.delete_all, None),
            #     'G': Option('Reset questions to Default', 'questions', questions.reset, None),
            #     'M': Option('Return to Main Menu', 'main', self.print_menu, 'main'),
            # },
        }

    def get_command(self, menu, chosen_option):
        submenu = self._menus.get(menu)
        command = submenu[chosen_option]
        return command

# MAIN PROGRAM


def print_menu(menu):
    # clear_screen()
    print()
    print(f'---------- {menu.upper()} MENU ----------')
    print()
    submenu = menus._menus.get(current_menu)
    for key, option in submenu.items():
        print(f'{key} : {option.name}')
        print()


def four():
    print(4)


def five():
    return {'5': 'yeah five'}


questions = Questions(name='questions')
questions.create_table()

menus = Menu()

current_menu = 'main'
print_menu(current_menu)


while True:
    chosen_option = input('Choose option: ')
    command = menus.get_command(current_menu, chosen_option)
    current_menu = command.menu
    print()
    print('New Menu', command.menu)
    print('Command Question Class', command)
    print('Command', command.command)
    print('Data', command.data)
    print()
    command.execute()
    # print_menu(new_menu)


# 'jobs': {
#     'A': Option('View Jobs Listing', 'jobs', jobs.view_all, None),
#     'B': Option('View a Specific Job by ID', 'jobs', jobs.view, None),
#     'C': Option('Add a Job', 'jobs', jobs.add, None),
#     'D': Option('Edit a Job', 'jobs', jobs.edit, None),
#     'E': Option('Delete a Job', 'jobs', jobs.delete, None),
#     'F': Option('Delete All Jobs', 'jobs', jobs.delete_all, None),
#     'G': Option('Reset Jobs to Default', 'jobs', jobs.reset, None),
#     'M': Option('Return to Main Menu', 'main', print_menu, 'main'),
# },

# 'answers': {
#     'A': Option('View answers Listing', answers.view_all, None),
#     'B': Option('View a Specific answer by ID', answers.view, None),
#     'C': Option('Add a answer', answers.add, None),
#     'D': Option('Edit a answer', answers.edit, None),
#     'E': Option('Delete a answer', answers.delete, None),
#     'F': Option('Delete All answers', answers.delete_all, None),
#     'G': Option('Reset answers to Default', answers.reset, None),
#     'M': Option('Return to Main Menu', print_menu, 'main'),
# },
# 'notes': {
#     'A': Option('View notes Listing', notes.view_all, None),
#     'B': Option('View a Specific note by ID', notes.view, None),
#     'C': Option('Add a note', notes.add, None),
#     'D': Option('Edit a note', notes.edit, None),
#     'E': Option('Delete a note', notes.delete, None),
#     'F': Option('Delete All notes', notes.delete_all, None),
#     'G': Option('Reset notes to Default', notes.reset, None),
#     'M': Option('Return to Main Menu', print_menu, 'main'),
# },
# 'tips': {
#     'A': Option('View tips Listing', tips.view_all, None),
#     'B': Option('View a Specific tip by ID', tips.view, None),
#     'C': Option('Add a tip', tips.add, None),
#     'D': Option('Edit a tip', tips.edit, None),
#     'E': Option('Delete a tip', tips.delete, None),
#     'F': Option('Delete All tips', tips.delete_all, None),
#     'G': Option('Reset tips to Default', tips.reset, None),
#     'M': Option('Return to Main Menu', print_menu, 'main'),
# },
