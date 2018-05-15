formatter = "{} {} {} {}"

# Replaces each of the individiual values below with each {} above.
# So 1 will replace the first {} and so on
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

#For each formatter value below it adds {} {} {} {}
#So you should see 16 of those when you print
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
