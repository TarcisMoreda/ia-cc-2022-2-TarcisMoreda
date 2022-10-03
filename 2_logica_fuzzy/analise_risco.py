from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, QSpinBox, QDoubleSpinBox, QPushButton

def calc_risco(lbl_risco, sb_dinheiro, sb_pessoas, sb_passos):
	dinheiro:float = float(sb_dinheiro.value())
	pessoas:int = int(sb_pessoas.value())
	passos:int = int(sb_passos.value())

	risco_bp = []
	risco_mp = []
	risco_ap = []

	risco_bg = []
	risco_mg = []
	risco_ag = []


	dinheiro_p = 0
	if dinheiro<30:
		dinheiro_p = 1
	elif dinheiro>50:
		dinheiro_p = 0
	else:
		dinheiro_p = (dinheiro-30)/(50-30)
	
	dinheiro_r = 0
	if dinheiro<50 and dinheiro>30:
		dinheiro_r = (dinheiro-30)/(50-30)
	elif dinheiro>50 and dinheiro<70:
		dinheiro_r = (dinheiro-50)/(70-50)
	elif dinheiro==50:
		dinheiro_r = 1
	else:
		dinheiro_r = 0

	dinheiro_a = 0
	if dinheiro<50:
		dinheiro_a = 0
	elif dinheiro>70:
		dinheiro_a = 1
	else:
		dinheiro_a = (dinheiro-50)/(70-50)

	pessoas_i = 0
	if pessoas<30:
		pessoas_i = 1
	elif pessoas>70:
		pessoas_i = 0
	else:
		pessoas_i = (pessoas-30)/(70-30)

	pessoas_s = 0
	if pessoas<30:
		pessoas_s = 0
	elif pessoas>70:
		pessoas_s = 1
	else:
		pessoas_s = (pessoas-30)/(70-30)

	valor_global_g=0
	for i in range(0, 41, passos):
		if i<=30:
			risco_bp.append(1)
		else:
			risco_bp.append(1-((i-30)/10))
		risco_bg.append(valor_global_g)
		valor_global_g+=passos

	valor_global_g=30
	for i in range(0, 41, passos):
		if i<10:
			risco_mp.append(i/10)
		elif i>30:
			risco_mp.append(1-((i-30)/10))
		else:
			risco_mp.append(1)
		risco_mg.append(valor_global_g)
		valor_global_g+=passos

	valor_global_g=60
	for i in range(0, 41, passos):
		if i<10:
			risco_ap.append(i/10)
		else:
			risco_ap.append(1)
		risco_ag.append(valor_global_g)
		valor_global_g+=passos

	deffuz_a1 = 0
	if dinheiro_p>=pessoas_i:
		deffuz_a1=dinheiro_p
	else:
		deffuz_a1=pessoas_i

	deffuz_a2 = 0
	if dinheiro_p>=pessoas_s:
		deffuz_a2=pessoas_s
	else:
		deffuz_a2=dinheiro_p

	deffuz_a = 0
	if deffuz_a1>=deffuz_a2:
		deffuz_a=deffuz_a1
	else:
		deffuz_a=deffuz_a2

	deffuz_m = 0
	if dinheiro_r>=pessoas_s:
		deffuz_m=pessoas_s
	else:
		deffuz_m=dinheiro_r

	deffuz_b = 0
	if dinheiro_a>=pessoas_s:
		deffuz_b=pessoas_s
	else:
		deffuz_b=dinheiro_a

	quant_risco_ap = 0
	res_risco_ap = 0
	for i in range(len(risco_ap)):
		if risco_ap[i]>=deffuz_a:
			res_risco_ap+=risco_ag[i]
			quant_risco_ap+=1
	res_risco_ap*=deffuz_a

	quant_risco_mp = 0
	res_risco_mp = 0
	for i in range(len(risco_mp)):
		if risco_mp[i]>=deffuz_m:
			res_risco_mp+=risco_mg[i]
			quant_risco_mp+=1
	res_risco_mp*=deffuz_m

	quant_risco_bp = 0
	res_risco_bp = 0
	for i in range(len(risco_bp)):
		if risco_bp[i]>=deffuz_b:
			res_risco_bp+=risco_bg[i]
			quant_risco_bp+=1
	res_risco_bp*=deffuz_b

	res = res_risco_ap+res_risco_mp+res_risco_bp
	res /= (quant_risco_ap*deffuz_a)+(quant_risco_mp*deffuz_m)+(quant_risco_bp*deffuz_b)

	res = "Risco: "+str(res)
	lbl_risco.setText(res)

if __name__ == "__main__":
	QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
	app = QApplication([])
	
	window = uic.loadUi("./analise_risco.ui")
	sb_dinheiro = window.findChild(QDoubleSpinBox, 'sbDinheiro')
	sb_pessoas = window.findChild(QSpinBox, 'sbPessoas')
	sb_passos = window.findChild(QSpinBox, 'sbPassos')
	lbl_risco = window.findChild(QLabel, 'lblRisco')
	btn_calc = window.findChild(QPushButton, 'btnCalcular')

	btn_calc.clicked.connect(lambda: calc_risco(lbl_risco, sb_dinheiro, sb_pessoas, sb_passos))
	
	window.show()
	app.exec_()