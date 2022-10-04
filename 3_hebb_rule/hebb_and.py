from hebb import *

inputs = [
	[1,1],
	[1,-1],
	[-1,1],
	[-1,-1]
]
target = [
	1,
	-1,
	-1,
	-1
]

hebb_var = hebb(2)
for i in range(len(inputs)):
	hebb_var.treinar(inputs[i], target[i])

print('===HEBB RULE===\n')
print('Weights:')
for i in range(len(hebb_var.pesos)-1):
	print('\tw{}: {}'.format(i, hebb_var.pesos[i]))
print('\twb: {}'.format(hebb_var.pesos[-1]))