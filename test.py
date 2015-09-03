somestring = "ABC"
somestring2 = somestring + "D"
somestring2 += "EF"

assert somestring2 == "ABCDEF"
assert somestring == "ABC"
assert id(somestring) != id(somestring2)
