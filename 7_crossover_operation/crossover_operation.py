import random
import sys

from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
                             QPushButton)


def on_combobox_change():
    if method_combo_box.currentText() == "Corte Simples":
        father_line_edit.setInputMask("BBBBBBBBBB")
        mother_line_edit.setInputMask("BBBBBBBBBB")
        father_line_edit.setText("0000000000")
        mother_line_edit.setText("1111111111")
    else:
        father_line_edit.setInputMask("AAAAAAAAAA")
        mother_line_edit.setInputMask("AAAAAAAAAA")
        father_line_edit.setText("AAAAAAAAAA")
        mother_line_edit.setText("BBBBBBBBBB")


def on_cross_pushbutton_clicked():
    if method_combo_box.currentText() == "Corte Simples":
        offsprings = simple_cut_crossover()
        son1_label_3.setVisible(False)
        son2_label_3.setVisible(False)
    else:
        offsprings = pmx_crossover()
        son1_label_3.setVisible(True)
        son2_label_3.setVisible(True)

    son1_label_1.setText(offsprings[0])
    son1_label_2.setText(offsprings[1])
    son1_label_3.setText(offsprings[2])
    son2_label_1.setText(offsprings[3])
    son2_label_2.setText(offsprings[4])
    son2_label_3.setText(offsprings[5])


def pmx_crossover():
    corte1 = random.randint(0, 5)
    corte2 = random.randint(
        len(father_line_edit.text()) - corte1, len(father_line_edit.text()))

    mae = []
    pai = []
    res1 = []
    res2 = []

    for i in range(len(father_line_edit.text())):
        mae.append(mother_line_edit.text()[i])
        pai.append(father_line_edit.text()[i])
    
    count = 0
    for i in pai:
        if count==corte1:
            break
        if i not in mae[corte1:corte2]:
            res1.append(i)
            count += 1

    count = 0
    for i in mae:
        if count==corte1:
            break
        if i not in pai[corte1:corte2]:
            res2.append(i)
            count += 1

    res1.extend(mae[corte1:corte2])
    res1.extend([x for x in pai if x not in res1])
    
    res2.extend(pai[corte1:corte2])
    res2.extend([x for x in mae if x not in res2])
    
    res = ["", "", "", "", "", ""]

    for i in range(len(father_line_edit.text())):
        if i < corte1:
            res[0] += res1[i]
            res[3] += res2[i]
        elif i < corte2:
            res[1] += res1[i]
            res[4] += res2[i]
        else:
            res[2] += res1[i]
            res[5] += res2[i]


    return res


def simple_cut_crossover():
    corte = random.randint(0, len(father_line_edit.text()) - 1)
    res1 = []
    res2 = []

    for i in range(len(father_line_edit.text())):
        if i < corte:
            res1.append(str(father_line_edit.text()[i]))
            res2.append(str(mother_line_edit.text()[i]))
        else:
            res1.append(str(mother_line_edit.text()[i]))
            res2.append(str(father_line_edit.text()[i]))

    res = ["", "", "", "", "", ""]

    for i in range(len(res1)):
        if i < corte:
            res[0] += res1[i]
            res[3] += res2[i]
        else:
            res[1] += res1[i]
            res[4] += res2[i]

    return res


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    # Loading widgets elements from ui file
    window = uic.loadUi("crossover_operation.ui")
    window.show()

    # Getting widgets elements
    father_line_edit = window.findChild(QLineEdit, 'fatherLineEdit')
    mother_line_edit = window.findChild(QLineEdit, 'motherLineEdit')
    son1_label_1 = window.findChild(QLabel, 'son1Label1')
    son1_label_2 = window.findChild(QLabel, 'son1Label2')
    son1_label_3 = window.findChild(QLabel, 'son1Label3')
    son2_label_1 = window.findChild(QLabel, 'son2Label1')
    son2_label_2 = window.findChild(QLabel, 'son2Label2')
    son2_label_3 = window.findChild(QLabel, 'son2Label3')
    method_combo_box = window.findChild(QComboBox, 'methodComboBox')
    cross_push_button = window.findChild(QPushButton, 'crossPushButton')

    # Connecting
    cross_push_button.clicked.connect(on_cross_pushbutton_clicked)
    method_combo_box.currentTextChanged.connect(on_combobox_change)
    sys.exit(app.exec_())
