# Basics of Python
# sintax 
print ("Hello World")

# comments
def sum(a,b):
    return a+b # the comments are indicated by the symbol #
print(sum(1,2))

# variables --> a variable is a space in memory that stores a value
# the value of a variable can be changed during the execution of the program
variable3 = "3"
variable1 = "1"
variable2 = NotImplemented
print (variable2, variable1 + variable3)

# global variables
global_variable = "I am a global variable"
def function():
    print (global_variable)
    # modifying a global variable
global_variable = "The global variable has been modified"
function()