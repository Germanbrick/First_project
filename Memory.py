
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)

center=Qt.AlignCenter
app = QApplication([])



class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def ask(q: Question):
    q = Question('В каком году была основана Москва?')
    ask(q)
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setWindowTitle(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

    def check_answer():
        if answers[0].isChecked():
            show_correct('Правильно')
        else:
            show_correct('Неверно')
    



def show_result(): 
    main_win.hide() 
    res_window.show() 
    
def show_question(): 
    res_window.hide() 
    main_win.show() 
    buttonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    buttonGroup.setExclusive(True)


    
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400,200)

res_window=QWidget()
res_window.setWindowTitle('Memory Card')
res_window.resize(400,200)

'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
res_button=QPushButton('Следующий вопрос')
lb_Question = QLabel('В каком году была основана Москва?') # текст вопроса
lb_Question_answ= QLabel('В каком году была основана Москва?') # текст вопроса в окне результата
groupbox=QGroupBox("выберите ответ")
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')
buttonGroup = QButtonGroup()
buttonGroup.addButton(rbtn_1)
buttonGroup.addButton(rbtn_2)
buttonGroup.addButton(rbtn_3)
buttonGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1,alignment=center) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2,alignment=center)
layout_ans3.addWidget(rbtn_3,alignment=center) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4,alignment=center)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
groupbox.setLayout(layout_ans1)
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addWidget(lb_Question,alignment=center)
layout_card.addWidget(groupbox)
layout_card.addWidget(btn_OK,stretch=2)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_result=QVBoxLayout()
layout_result.addWidget(lb_Question_answ,alignment=Qt.AlignHCenter)
layout_result.addWidget(AnsGroupBox)
layout_result.addWidget(res_button,stretch=2)



res_window.setLayout(layout_result)


window.setLayout(layout_card)
window.show()
res_window.show()
app.exec()
