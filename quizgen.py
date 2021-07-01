#! python3
# This random quiz generator creates quizzes/answers in a random order
# This quiz is based on Countries and Capitals but different data may be inserted into the capitals file

import random
from capitals import capitals #imports file containing capitals

#generate 35 quiz and answer files
for quizNum in range(35):
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    #write header for quiz file with Name and Date
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write(('' * 20) + f'Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    #shuffle order of states
    countries = list(capitals.keys())
    random.shuffle(countries)

    #loop through states and create question for each
    for questionNum in range(50):
        #get right and wrong answers
        correctAnswer = capitals[countries[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #write question and answer options to quiz files
        quizFile.write(f'{questionNum + 1}. What is the capital of {countries[questionNum]}? \n\n')
        for i in range(4):
            quizFile.write(f" {'ABCD' [i]}. {answerOptions[i]}\n")
            quizFile.write('\n')

        #write the answer key to a file
            answerKeyFile.write(f"{questionNum + 1}. {'ABCD' [answerOptions.index(correctAnswer)]}")

    quizFile.close()
    answerKeyFile.close()
