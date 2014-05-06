import copy
a = [["bob", "peter", "igor"], ["new york", "boston", "chicago"]]
b = copy.copy(a)
print(b)
b[1][1]="braintree"
print(b)
#...[['bob', 'peter', 'igor'], ['new york', 'braintree', 'chicago']]
print(a)
#… [['bob', 'peter', 'igor'], ['new york', 'braintree', 'chicago']]

b = copy.deepcopy(a)
b[1][1] = "stockholm"
print(a)
#Out[32]: [['bob', 'peter', 'igor'], ['new york', 'braintree', 'chicago']]

print(b)
#Out[33]: [['bob', 'peter', 'igor'], ['new york', 'stockholm', 'chicago']]
