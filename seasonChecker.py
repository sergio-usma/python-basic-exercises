print('\nHi!👋 Check the month and their season!!')

month = input('\nPlease insert a month or the year!😀: ').lower()

if (month == 'march') or (month == 'april') or (month == 'may'):
    print(f'\nIn {month} it\'s Spring!🌳')
elif (month == 'june') or (month == 'july') or (month == 'august'):
    print(f'\nIn {month} it\'s Summer!🏖️')
elif (month == 'september') or (month == 'october') or (month == 'november'):
    print(f'\nIn {month} it\'s Fall!🍃')
elif (month == 'december') or (month == 'january') or (month == 'february'):
    print(f'\nIn {month} it\'s Winter!☃️')
else:
    print('\nPlease insert a valid month! Ex:March😉')
