print "Let's practice everything ."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print "-*10"
print poem
print "-*10"

five = 10-2+3-6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars /100
    return jelly_beans, jars, cartes



start_point = 1000
beans, jars ,cartes = secret_formula(start_point)

print "With a starting point of : %d" % start_point
print "We'd have %d beans ,%d jars, and %d cartes." % (beans,jars,cartes)

start_point = start_point / 10

print "We can also do that this way :"
print "We'd have %d beans ,%d jars , and %d cartes." % secret_formula(start_point)
