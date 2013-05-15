# there are 10 people in this example
x = "There are %d types of people." % 10
# this is the variable for binary 
binary = "binary"
# this is the variable for don't
do_not = "don't"
# comparison statement
y = "Those who know %s and those who %s." % (binary, do_not)

# print x and y but not my notes
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# this is not funny at all
hilarious = False
joke_evaluation = "Isn't that joke so funny?!  %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e