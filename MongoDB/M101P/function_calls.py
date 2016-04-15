fruit = [ 'apple', 'orange', 'kiwi', 'grape', 'lime', 'orange', 'amrood', 'apple', 'pear' ] # init the array or list

# reports the frequency of every item in the list
def analyse_list (l):
    counts = {}
    for item in l:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
#        counts[item] = counts.get(item, 0) + 1    # This can replace previous FOUR lines

    return counts


# let's analyze a list

print fruit

con = analyse_list(fruit)

print con
