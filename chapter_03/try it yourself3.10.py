rivers = ['ravi', 'chanab', 'indus','jehlam']
print(rivers)
#accessinng elements in a list
print(rivers[0])
print(rivers[1])
#
print(rivers[-1])

message = 'lahore is located at the bank of {rivers[0].title()}.'
print(message)
#modifing
rivers[0] = 'rachna'
print(rivers)
#appending
rivers.append('beyas')
print(rivers)
#inserting
rivers.insert(1, 'sutlag')
print(rivers)
#removing using del
del rivers[0]
print(rivers)
#removing using pop()
c = rivers.pop()
print(c)
print(rivers)
d = rivers.pop(0)
print(d)

rivers.remove('indus')
print(rivers)
