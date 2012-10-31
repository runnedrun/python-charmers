import random

def trick_or_treater(name):
    return "hello " + name+  ", here's some candy for you"

Counts = {"David":0}

Locations = {"David":[0,10]}

Candies = ["kit-kat","hersheys","reeses","milkyway","pay-day"]

Houses = [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11]

def move_forward(name):
    if Locations[name][0] < len(Houses)-1:
        Locations[name][1] = Locations[name][0]
        Locations[name][0] = Locations[name][0]+1
        return Locations[name][0]
    else:
        return -1

def move_backward(name):
    if Locations[name][0] > 0:
        Locations[name][1] = Locations[name][0]
        Locations[name][0] = Locations[name][0]-1
        return Locations[name][0]
    else:
        return -1

def trick_or_treat(name):
    current_house = Locations[name][0]
    candy_left = Houses[current_house]
    previous_house = Locations[name][1]
    if candy_left == 1 and (previous_house != current_house):
        candy_given = "King Sized " + random.choice(Candies) + "!"
        Counts[name] += 10
        Houses[current_house] -= 1
    elif candy_left > 0 and (previous_house != current_house):
        candy_given = random.choice(Candies)
        Counts[name] += 1
        Houses[current_house] -= 1
    else:
        candy_given = "Sorry kid"
    
    Locations[name][1] = Locations[name][0]
    return candy_given

def print_scores():
    for name,count in Counts.iteritems():
        print name + " has " + str(count) + " pieces of candy"

 
    

