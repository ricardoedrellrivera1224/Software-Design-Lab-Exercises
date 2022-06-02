# Python program to reverse a string using recursion

# Function to print reverse of the passed string
def reverse(string):
    if len(string) == 0:
        return

    temp = string[0]
    reverse(string[1:])
    print(temp, end='')


# Driver program to test above function
string = "Geeks for Geeks"
reverse(string)

# A single line statement to reverse string in python
# string[::-1]