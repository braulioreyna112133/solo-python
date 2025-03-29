# usar prefijo bytes para covertir ints en bytes
b1 = bytes ([77, 13])
print (b1)

# usar prefijo b para convertir texto en bytes
b2 = b'game changer'
print (b2)

# bytearrays: You can create a bytearray using various methods, 
# including by passing an iterable of integers representing byte values, 
# by encoding a string, or by converting an existing bytes or bytearray object.
# Are mutable
# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])  
print(value)  

# Creating a bytearray by encoding a string
val = bytearray("Hello - utf-8", 'utf-8')  
print(val)  