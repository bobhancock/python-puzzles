import itertools

end_words = ("Sunday", "Monday", "Tuesday", "Wednesday",
       "Thursday", "Friday")

def contains(predicate, seq):
    return True in itertools.imap(predicate, seq)

def ends_with(s, *endings):
    return contains(s.endswith, endings)

for line in open("data/1_13.data", "r"):
    print(ends_with(line.strip("\n"), end_words))