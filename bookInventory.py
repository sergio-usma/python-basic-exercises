print('\nHi!👋 Welcome to the Library!')

print('\nInsert the book\'s information!😉')

bookName = input('\n1️⃣ Insert the book\'s name: ')
bookAuthor = input('2️⃣ Insert the book\'s author: ')
bookID = int(input('3️⃣ Insert the book\'s ID: '))
bookPrice = float(input('4️⃣ Insert the book\'s price: '))
freeShip = input('5️⃣ Free ship included? (yes/no:) ').lower()

if freeShip == 'yes':
    freeShipmentN = True
else:
    freeShipmentN = False

print(f'''
This is the Book's information:📖
1️⃣ Book name: {bookName}
2️⃣ Book author: {bookAuthor}
3️⃣ ID: {bookID}
4️⃣ Price: {bookPrice}
5️⃣ Free ship?: {freeShipmentN}
''')
