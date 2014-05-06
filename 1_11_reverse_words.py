def rev_words(rec):
    return " ".join(rec.strip("\n").split(",")[::-1])
                    
for line in open("data/1_11.data", "r"):
    print(rev_words(line))
                    