from perceptron import *

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

per = perceptron(2)
epochs = per.treinar(inputs, target)

print('===PERCEPTRON===\n')
print('Weights:')
for i in range(len(per.pesos)-1):
	print('\tw{}: {}'.format(i, per.pesos[i]))
print('\twb: {}'.format(per.pesos[-1]))
print('epochs: {}'.format(epochs))