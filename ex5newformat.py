my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about {0}.".format(my_name)
print "He's {0} inches tall.".format(my_height)
print "He's {0} pounds heavy.".format(my_weight)
print "Actually that's not too heavy."
print "He's got {0} eyes and {1} hair.".format(my_eyes, my_hair)
print "His teeth are usually {0} depending on the coffee.".format(my_teeth)

# this line is tricky, try to get it exactly right
print "If I add {0}, {1}, and {2} I get {3}.".format(my_age, my_height, my_weight, my_age + my_height + my_weight)