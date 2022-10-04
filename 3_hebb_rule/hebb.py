from mimetypes import init


class hebb:
	def __init__(self, quant_pesos:int) -> None:
		self.pesos = []
		for i in range(quant_pesos+1):
			self.pesos.append(0.0)

	def treinar(self, entradas:tuple, target:int) -> tuple:
		for i in range(len(self.pesos)-1):
			self.pesos[i] = self.pesos[i]+(entradas[i]*target)
		self.pesos[-1] = self.pesos[-1]+target
		return self.pesos