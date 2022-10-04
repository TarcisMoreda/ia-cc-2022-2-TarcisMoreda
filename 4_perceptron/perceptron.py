class perceptron:
	def __init__(self, quant_pesos:int) -> None:
		self.pesos = []
		self.taxa = 1

		for i in range(quant_pesos+1):
			self.pesos.append(0.0)

	def treinar(self, entradas:tuple, target:tuple):
		cond = True
		epoch = 0
		while(cond):
			diff = 0

			for i in range(len(entradas)):
				saida = self.mcculloch(entradas[i], target[i])
				if saida!=target[i]:
					for j in range(len(self.pesos)-1):
						self.pesos[j] += self.taxa*target[i]*entradas[i][j]
					self.pesos[-1] += target[i]*self.taxa
				else:
					diff += 1
			epoch += 1
			if diff==len(entradas):
				cond = False

		return epoch

	def mcculloch(self, entradas:tuple, target:int):
		saida = 0
		for i in range(len(entradas)):
			saida += entradas[i]*self.pesos[i]
		saida += self.pesos[-1]

		if saida>0:
			return 1
		elif saida<0:
			return -1
		else:
			return 0