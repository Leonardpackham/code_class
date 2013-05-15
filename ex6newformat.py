x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: {0!r}.".format(x)
print "I also said: '{0}'.".format(y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?!  {0!r}"

print joke_evaluation.format(hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print w + e