import random
import commands
from collections import namedtuple
import os

def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)

jobs = commands.Jobs(table_name='jobs')
jobs.create_table()

questions = commands.Questions(table_name='questions')
questions.create_table()

answers = commands.Answers(table_name='answers')
answers.create_table()

tips = commands.Tips(table_name='tips')
tips.create_table()

notes = commands.Notes(table_name='notes')
notes.create_table()



questions = {
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
    def __init__(self, name, command, data):
        self.name = name
        self.command = command
        self.data = data

    def select(self):
        if self.data is not None:
            self.command(self.data)
        else:
            self.command()

class MainMenu:
    def __init__(self):
        pass

    def practice(self):
        # Get random job and questions
        # jobs.view(random_job)
        # questions.view(random_3_questions)
        pass

    def practice_not_practiced(self):
        # Select from jobs not practiced
        pass

main = MainMenu()
    
def print_menu(selected_menu):
    # clear_screen()
    submenu = menus.get(selected_menu, 'main')
    for key, option in submenu.items():
        print(f'{key} : {option.name}')
        print()

def select_option(selected):
    choice = input('Choose')
    new_menu = menu[selected]
    return print_options(new_menu)


menus = {
'main': {
        '1': Option('Get a Random Job and Questions', main.practice, None), # TODO: Create get_random function
        'J': Option('View Jobs Options', print_menu, 'jobs'),
        'Q': Option('View Questions Options', 'questions', None),
        'A': Option('View Answers Options', 'answers', None),
        'T': Option('View Tips Options', 'tips', None),
        'N': Option('View Notes Options', 'notes', None),
    },
'jobs': {
    'A': Option('View Jobs Listing', jobs.view_all, None),
    'B': Option('View a Specific Job by ID', jobs.view, None),
    'C': Option('Add a Job', jobs.add, None),
    'D': Option('Edit a Job', jobs.edit, None),
    'E': Option('Delete a Job', jobs.delete, None),
    'F': Option('Delete All Jobs', jobs.delete_all, None),
    'G': Option('Reset Jobs to Default', jobs.reset, None),
    'M': Option('Return to Main Menu', print_menu, 'main'),
}
 }



def choose_command(submenu):
    choice = input('Choose command: ')
    new_menu = menus.get(submenu, 'main')
    return new_menu[choice].select()

# newmenu = menus.get('main')

# for key, option in newmenu.items():
#     print(key, option[0])

my_chosen_option = menus['main'].get('J')

my_chosen_option.select()

print_menu('jobs')