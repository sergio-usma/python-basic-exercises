print('\nHi!👋 Welcome to Could go to the game!!')

print('\nThere is a bowl match tomorrow!! Could you go to the game? 🤔')

vacation = input('\nAre you on vacation 🏖️ (yes/no): ').capitalize()
restDay = input('Are you on a rest-day 🩴 for tomorrow(yes/no): ').capitalize()

if vacation == 'Yes' or restDay == 'Yes':
    print('\nYou can go to the game!! 🎳')
else:
    print('\nSorry buddy, but you must work tomorrow! 🕺')
