print('\nHi!👋 Check your generational age range!!')

age = int(input('\nPlease insert your age!!😉: '))

babyBoomer = 60 <= age <= 78
genX = 44 <= age <= 59
millennial = 28 <= age <= 43
genZ = 12 <= age <= 27

if millennial:
    print('\nYou are a millennial!!✅')
elif babyBoomer:
    print('\nYou are a Baby Boomer!!🧓')
elif genX:
    print('\nYou are a GenX!!🧑')
elif genZ:
    print('\nYou are a GenZ!!🧒')
else:
    print('\nYou are not a millennial at all!!👴')
