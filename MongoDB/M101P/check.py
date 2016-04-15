fruit = [ 'apple', 'orange', 'pear', 'lime', 'kiwi' ] # fruit_list

'kiwi' in fruit     #  in operator to check if an item is in list/dict

person = { 'name' : 'First LastName', 'age' : 100, 'place_of_birth' : 'CityName' } # dictionary_person
colors = { 'sky' : 'blue', 'sea' : 'blue', 'earth' : 'brown' }
things = { "animals":["dog", "cat", "zebra"]}


##### Quiz: Python: for Loops, with Lists
##### What does the following code print? 
sum = 0
numbers = [1, 2, 3, 5, 8]
for i in numbers:
    sum = sum + i
print i


##### Quiz: Python: for Loops with Dicts 
people = {'name': 'Bob', 'hometown': "Palo Alto", 'favorite_color': 'red'}
for item in people:
    if (item == 'favorite_color'):
        print people[item]
