n = int(input('enter any value: '))
print('entered value is :', n)

sum = 0
for i in range(1,n+1):
	sum = sum + i
print('sum fo number :', i)
print('total sum from 1 to {} is {}'.format(n,sum))
print('total sum from 1 to {1} is {0} = {1} {1}'.format(n,sum))
print('total sum from 1 to {value1} is {value2}'.format(value1=n,value2=sum))

welcome_msg = "Hi {}, Welcome to Learning page".format("Anil")
print(f'total sum from 1 to {n} is {sum}')
# name = "Anil"
# country = "India"

# print('total sum from 1 to {0} is {1}'.format(name,country))

# Lab challenge
# try this
# print float value using f'strings with only two decimal points
# 99.987654 = > 99.99 => 99.987
