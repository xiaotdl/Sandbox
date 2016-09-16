import json

numbers = [2,3,5,7,11,13]
filename = 'numbers.json'

# write into file
try:
    with open(filename, 'w') as f:
        json.dump(numbers, f)
except FileNotFoundError:
    print 'File not found!'

# read from file
try:
    with open(filename) as f:
        nums = json.load(f)
except FileNotFoundError:
    print 'File not found!'

print nums
