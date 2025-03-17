#amstrong number
#153==1*3+5*3+3*3==153

number = int(input('Enter any number: '))

toString = str(number)
sum = 0

for i in toString:
    i = int(i)
    sum = sum + pow(i, len(toString))
    # print(i, sum)
	
if(number==sum):
	print('it is a amstrong')
else:
	print('it is not a amstrong')


'reverse value of {} is {}'.format(n,reverse)