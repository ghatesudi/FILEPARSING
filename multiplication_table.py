


# A simple script for Multiplication Table

while True:
	StartOrEnd = str(input('Start or End : ').lower())
	if StartOrEnd == 'start':
		whichTable = int(input('Which Table : '))
		for x in range(1, 11):
			table =  whichTable * x
			print(f'{whichTable} x {x} = {table}')
			print()
		continue
	else :
		print('Program Ended...')
		break	






