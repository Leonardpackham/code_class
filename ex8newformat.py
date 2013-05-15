formatter = "{0!r} {1!r} {2!r} {3!r}"

print formatter.format(1, 2, 3, 4)
print formatter.format("one", "two", "three", "four")
print formatter.format(True, False, False, True)
print formatter.format(formatter, formatter, formatter, formatter)
print formatter.format(
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)