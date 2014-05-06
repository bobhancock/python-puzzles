dow = ("Sunday", "Monday", "Tuesday", "Wednesday",
       "Thursday", "Friday")

def starts_dow(s):
    return s.startswith(dow)

i = 1
for line in open("data/1_7.data"):
    print("{} {}".format(i, starts_dow(line)))
    i += 1