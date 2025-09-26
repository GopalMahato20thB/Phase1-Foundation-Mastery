#print("Hello, Arch!) # This will return this error: SyntaxError: unterminated string literal
# without an error
print("Hello, Arch!")

# x = int(input("What's x? "))
# print(f"x is {x}") # If we pass string in this program will throw this error: ValueError: invalid literal for int() with base 10: 'cat'

# We can catch errors using python's error handling
"""
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
        print("x is not an integer")
"""

#This will throw an error
"""
try:
    x = int(input("What's x? "))

except ValueError:
        print("x is not an integer")
print(f"x is {x}")


"""


#To solve above  We can do this way or inside the try block
"""
try:
    x = int(input("What's x? "))

except ValueError:
        print("x is not an integer")

else:
    print(f"x is {x}")
"""
def main():
    x = get_int()
    print(f"x is {x}")




def get_int():
    while True:
        try:
            return  int(input("what's x? "))
        except ValueError:
            pass


main()
