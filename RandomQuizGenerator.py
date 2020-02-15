#this programme creates 35 different quizzes
#must use text files
#50 multi choice questions in each quiz in random order
#provides one correct and 3 incorrect options
#writes the answer form and the answer key to a text file

import random as rand
import copy
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', '''New
Mexico''': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', '''West
Virginia''': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


qs      =50 #50
tests   =35 #35

for iter in range(1,tests,1):
    qitems = rand.sample(list(capitals.items()), 50)
    qquest = qitems[0:50][1]
    answers = []
    questions = []
    options = []

    quizqFile = open("Quiz%s.txt" %iter,'w')
    ansFile   = open("Ans%s.txt" %iter, 'w')
    quizqFile.write('Name: \nDate: \nPeriod: \n\n\n ')
    quizqFile.write((' ' * 20) + 'Quiz!\nform number: %s\n\n' % iter)

    for question in range(1,qs,1):
        answers.append(qitems[question-1][1])
        questions.append(qitems[question-1][0])

    for ques in range(0,qs-1,1):
        options = []
        options.append(answers[ques])
        wrong =[]
        ansops = copy.copy(answers)
        del ansops[ansops.index(answers[ques])]

        wrong = rand.sample(ansops,3)

        while answers[ques] in wrong:
            wrong = rand.sample(ansops, 3)

        for i in range(0,3,1):
            options.append(wrong[i])


        print('question %s what is the capital of %s: ' % ((ques+1),questions[ques]))
        rand.shuffle(options)

        for i in range(0,4,1):
            disp = ''
            disp += options[i]
            print('%s. %s' % ('ABCD'[i], disp))
        print('the answer is %s' % 'ABCD'[options.index(answers[ques])])

        quizqFile.write('%s. what is the capital of %s?\n' % ((ques+1), questions[ques]))
        for i in range(4):
            quizqFile.write('%s. %s\n' % ('ABCD'[i], options[i]))
        ansFile.write('%s.%s\n' % ((ques+1),'ABCD'[options.index(answers[ques])]))


