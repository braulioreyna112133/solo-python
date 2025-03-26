# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType

elementInput = 'test text'

list1 = ['list', 1, 2+3j, True]
tuple1 = (1.2, 'tuple', 2+3j, None)
list2 = ['segunda', 'lista', 'de', 'texto']

elements = [
    list1, tuple1, list2
            ]

# 1
for elementsIndex in elements:
     while True:
        if type (elementsIndex) is list:
            try:
                elementsIndex.append(elementInput)
                print (True, elementsIndex)
                break
            except TypeError:
                # print (False, elementsIndex)
                break
        break
