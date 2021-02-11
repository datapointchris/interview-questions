import random

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

try:
    with open('answered.txt', 'r') as ans:
        answered = ans.read().splitlines()
except Exception as e:
    print(e)
    answered = []

not_answered = [q for q in questions.keys() if q not in answered]

try:
    selected = random.choice(not_answered)
    print(selected + ':')
    print(questions[selected])

    with open('answered.txt', 'a') as ans:
        ans.write(f'\n{selected}')
except IndexError:
    print('CONGRATULATIONS!!!')
    print('Answered All Questions!!')
    print('Are you employed yet???')

options_menu = {
    1: 'get_a_new_question',
    2: 'get_a_new_question',
}