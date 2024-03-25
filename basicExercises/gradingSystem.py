print('\nHi!👋 Welcome to your school!!')

grade = int(input('\nPlease insert a grade!🧑‍🎓🧑‍: '))

if 0 <= grade < 6:
    print('Your grade is F')
elif 6 <= grade < 7:
    print('Your grade is D')
elif 7 <= grade < 8:
    print('Your grade is C')
elif 8 <= grade < 9:
    print('Your grade is B')
elif 9 <= grade <= 10:
    print('Your grade is A')
else:
    print('\nInsert a correct grade in number!!')
