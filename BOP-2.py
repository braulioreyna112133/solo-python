# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType

element = 'text'

list1 = ['list', 1, 2+3j, True]
tuple1 = (1.2, 'tuple', 2+3j, None)
list2 = ['segunda', 'lista', 'de', 'texto']

elements = [
    list1, tuple1, list2
            ]


for elementsIndex in elements:
    while True:
        if type(elementsIndex) is list:
            print (True, 'Is a list')
            break
        else:
            print (False)
            break