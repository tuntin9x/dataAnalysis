from ast import literal_eval
mydict = {}
str_data = "{'foo': 1, 'quux': 1, 'labs': 1, 'bar': 1}"
res = literal_eval(str_data)
print(res["foo"])