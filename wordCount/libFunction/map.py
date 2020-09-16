import base64
addValue = []
data = 'foo foo quux labs foo bar quux'
words = data.split()
for word in words:
    addValue.append(word+','+'1')
str_data = ""
for i in range(0, len(addValue)-1):
    str_data = str_data + addValue[i] + ";"
str_data = str_data + addValue[-1]
encodSender = base64.b64encode(bytes(str_data, "utf-8"))
#print(str(encodSender,"utf-8"))