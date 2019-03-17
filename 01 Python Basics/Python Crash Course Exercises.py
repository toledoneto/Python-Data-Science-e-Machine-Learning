# --------- # EXC 1 : What is 7 to the power of 4?
print(7**4)

# --------- # EXC 2 : Split this string 's' into a list
s = "Hi there Sam!"
print(s.split(sep=' '))

# --------- # EXC 3 : Given the variables below, use .format() to print the following string
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet, diameter))

# --------- # EXC 4 : Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

# --------- # EXC 5 : Given this nested dictionary grab the word "hello".
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

# --------- # EXC 6 : Create a function that grabs the email website domain from a string in the form
def get_domain(email):
    parts = email.split(sep='@')
    return parts[1]

print(get_domain('user@domain.com'))

# --------- # EXC 7 : Create a basic function that returns True if the word 'dog' is contained in the input string
def findDog(str):
    found = str.find('dog')
    # print(found)
    if found > 0:
        return True
    else:
        return False

print(findDog('Is there a dog here?'))
print(findDog('Is there a cat here?'))

# --------- # EXC 8 : Create a function that counts the number of times the word "dog" occurs in a string
def countDog(str):
    return print(str.count('dog'))

countDog('This dog runs faster than the other dog dude!')
countDog('This dog runs faster than the other cat dude!')

# --------- # EXC 9 : Use lambda expressions and filter() to filter out words that don't start with the letter 's'
seq = ['soup','dog','salad','cat','great']

print(list(filter(lambda x:x[0] == 's', seq)))

# --------- # EXC 10 :
# Write a function to return one of 3 possible results:
# * "No ticket",
# * "Small ticket", or
# * "Big Ticket".
# - If your speed is 60 or less, the result is "No Ticket".
# - If speed is between 61 and 80 inclusive, the result is "Small Ticket".
# - If speed is 81 or more, the result is "Big Ticket".
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday,
# your speed can be 5 higher in all cases
def caught_speeding(speed, is_birthday):
    min_speed = 60
    max_speed = 80

    if is_birthday:
        min_speed = min_speed+5
        max_speed = max_speed+5

    if speed <= min_speed:
        return 'No Ticket'
    if speed > min_speed and speed <= max_speed:
        return 'Small Ticket'
    if speed > max_speed:
        return "Big Ticket"

print(caught_speeding(81,True))
print(caught_speeding(81,False))