import random
from capitals import capitals #imports file containing capitals

for quizNum in range(35): # Generate 35 quiz files.
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'Country Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    countries = list(capitals.keys()) # get all states in a list
    random.shuffle(countries) # randomize the order of the states

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):

        # Get right and wrong answers.
        correctAnswer = capitals[countries[questionNum]]
        wrongAnswers = list(capitals.values()) # get a complete list of answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # remove the right answer
        wrongAnswers = random.sample(wrongAnswers, 3) # pick 3 random ones

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions) # randomize the order of the answers

        # Write out the question and answer options.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, countries[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write out the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
