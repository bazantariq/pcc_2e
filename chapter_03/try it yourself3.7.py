living = ['Ali', 'Ahamad', 'Sara']
for eachperson in living:
    print(eachperson+" you are invited to dinner.")

living.insert(0,'Khalid')
living.insert(1,'Sana')
living.append('Sabir')
print(living)
for eachperson in living:
    print(eachperson+" you are invited to  dinner.")
print('I have found a bigger dinner.')

print('I can invite only two people.')
a = living.pop()
print(a+", I am sorry, I can not invite you to dinner.")
b = living.pop()
print(b+", I am sorry, I can not invite you to dinner.")
c = living.pop()
print(c+", I am sorry, I can not invite you to dinner.")
d = living.pop()
print(d+", I am sorry, I can not invite you to dinner.")

print(living)
del living[0]
del living[0]
print(living)