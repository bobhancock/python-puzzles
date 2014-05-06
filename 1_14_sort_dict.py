from collections import namedtuple

def dict_to_namedtuple(adict):
    valdict = dict( (v,k) for k,v in adict.iteritems() )
    keys = valdict.keys()
    keys.sort()
    nt = namedtuple("nt", ",".join(str(k) for k in keys))
    return nt._make([valdict[k] for k in keys])
    
dic = {1:"one", 2:"two", 3:"three"}
t = dict_to_namedtuple(dic)
print(t)
    
    