print('Hello, world!')
name = input('What is your name?\n')

# This still works but is pretty archaic
# for simple stuff use f-strings, for more complex look at the sting method format()
#print ('Hi, %s.' % name)
print(f"Hi, {name}.")

# Also, no spaces between function name and its parens  
# NO:  print ()        YES: print()
