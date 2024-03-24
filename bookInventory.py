print('\nHi!👋 Welcome to the Library!')

print('\nInsert the book\'s information!')

bookName = input('\nInsert the book\'s name: ')
bookAuthor = input('Insert the book\'s author: ')
bookID = int(input('Insert the book\'s ID: '))
bookPrice = float(input('Insert the book\'s price: '))
freeShip = input('Free ship included? (yes/no:) ').lower()

if freeShip == 'yes':
    freeShipmentN = True
else:
    freeShipmentN = False

print(f'''
Book name: {bookName}
Book author: {bookAuthor}
ID: {bookID}
Price: {bookPrice}
Free ship? {freeShipmentN}
''')
