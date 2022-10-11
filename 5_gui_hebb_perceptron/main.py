from pickletools import read_stringnl_noescape_pair
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QComboBox, QTextEdit
from hebb import *
from perceptron import *

def on_treino_clicked():
	entradas = []
	target = []

	for i in txtEntradas.toPlainText().split('\n'):
		temp = []
		for j in i.split(' '):
			temp.append(int(j))
		entradas.append(temp)

	for i in txtSaida.toPlainText().split('\n'):
		target.append(int(i))

	if cbAlg.currentIndex()==0:
		rede_hebb = hebb(2)
		for i in range(len(entradas)):
			rede_hebb.treinar(entradas[i], target[i])
		lblPesos.setText('<html><head/><body><p>{}</p><p>{}</p><p>{}</p></body></html>'.format(rede_hebb.pesos[0], rede_hebb.pesos[1], rede_hebb.pesos[2]))
	else:
		rede_perceptron = perceptron(2)
		rede_perceptron.treinar(entradas, target)
		lblPesos.setText('<html><head/><body><p>{}</p><p>{}</p><p>{}</p></body></html>'.format(rede_perceptron.pesos[0], rede_perceptron.pesos[1], rede_perceptron.pesos[2]))

def on_executar_clicked():
	entrada = []
	for i in txtEntrada.toPlainText().split('\n'):
		entrada.append(int(i))
	
	if cbAlg.currentIndex()==0:
		rede_hebb = hebb(2)
		pesos = lblPesos.text().replace('<html><head/><body><p>', '').replace('</p><p>', ' ').replace('</p></body></html>', '').split(' ')
		rede_hebb.pesos[0] = float(pesos[0])
		rede_hebb.pesos[1] = float(pesos[1])
		rede_hebb.pesos[2] = float(pesos[2])
		lblSaida.setText('{}'.format(rede_hebb.run(entrada)))
	else:
		rede_perceptron = perceptron(2)
		pesos = lblPesos.text().replace('<html><head/><body><p>', '').replace('</p><p>', ' ').replace('</p></body></html>', '').split(' ')
		rede_perceptron.pesos[0] = float(pesos[0])
		rede_perceptron.pesos[1] = float(pesos[1])
		rede_perceptron.pesos[2] = float(pesos[2])
		lblSaida.setText('{}'.format(rede_perceptron.run(entrada)))

if __name__ == "__main__":
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
	app = QApplication([])

	window = uic.loadUi("./hebb_perceptron.ui")
	cbAlg = window.findChild(QComboBox, 'cbAlg')
	cbAlg.addItem('Hebb')
	cbAlg.addItem('Perceptron')

	txtEntradas = window.findChild(QTextEdit, 'txtEntradas')
	txtSaida = window.findChild(QTextEdit, 'txtSaida')
	btnTreino = window.findChild(QPushButton, 'btnTreino')
	lblPesos = window.findChild(QLabel, 'lblPesos')
    
	txtEntrada = window.findChild(QTextEdit, 'txtEntrada')
	btnExecutar = window.findChild(QPushButton, 'btnExecutar')
	lblSaida = window.findChild(QLabel, 'lblSaida')

	btnTreino.clicked.connect(on_treino_clicked)
	btnExecutar.clicked.connect(on_executar_clicked)

	window.show()
	app.exec_()