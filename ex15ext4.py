from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file {0}:".format(filename)
print txt.read()
