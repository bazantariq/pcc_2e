living = ['Ali', 'Ahamad', 'Sara']
for eachperson in living:
    print(eachperson+" you are invited to dinner.")

c = living.pop()

living.append('Aimen')
print(living)

for eachperson in living:
    print(eachperson+" you are invited to dinner.")

print(c + " can not come to dinner.")