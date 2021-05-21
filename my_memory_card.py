#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QPushButton, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3  =wrong3

questions_list = []
questions_list.append(Question("Государственный язык Бразилии", "Португальский", "Бразильский", "Испанский", "Итальянский"))
questions_list.append(Question("Какого цвета нет на флаге России", "Жёлтый", "Красный", "Синий", "Белый"))
questions_list.append(Question("Кто я?", "Владос", "Не Владос", "Не Владос", "Не Владос"))

#создание приложения и главного окна
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Memory Card")
my_win.resize(400, 200)

linev = QVBoxLayout()
#создание вопроса 5-8
text = QLabel("Какой национальности не существует?")
line1 = QHBoxLayout()
line1.addWidget(text, alignment = Qt.AlignCenter)
linev.addLayout(line1)

#создание группы ответов 10 - 11
text2 = QGroupBox("Варианты ответов")
line2 = QHBoxLayout()
line2.addWidget(text2, alignment = Qt.AlignCenter)
linev.addLayout(line2)

#создание виджета "ответить" 12-13
knopka = QPushButton("Ответить")
line3 = QHBoxLayout()
line3.addWidget(knopka, alignment = Qt.AlignCenter)
linev.addLayout(line3)

#создание вариантов ответов 14-15
cnopka1 = QRadioButton("Энцы")
cnopka2 = QRadioButton("Смурфы")
cnopka3 = QRadioButton("Чулымцы")
cnopka4 = QRadioButton("Алеуты")

Group = QButtonGroup()
Group.addButton(cnopka1)
Group.addButton(cnopka2)
Group.addButton(cnopka3)
Group.addButton(cnopka4)

goriz = QHBoxLayout()
line5 = QVBoxLayout()
line6 = QVBoxLayout()

line5.addWidget(cnopka1)
line5.addWidget(cnopka2)
line6.addWidget(cnopka3)
line6.addWidget(cnopka4)

goriz.addLayout(line5)
goriz.addLayout(line6)
text2.setLayout(goriz)

Box = QGroupBox("Результат теста")
rez  = QLabel("Правильно/Неправильно")
rez2 = QLabel("Правильный ответ")
lineV = QVBoxLayout()
lineV.addWidget(rez)
lineV.addWidget(rez2)
Box.setLayout(lineV)
line2.addWidget(Box)
Box.hide()

def show_result():
    text2.hide()
    Box.show()
    knopka.setText("Следующий вопрос")

def show_question():
    Box.hide()
    text2.show
    knopka.setText("Ответить")
    Group.setExclusive(False)
    cnopka1.setChecked(False)
    cnopka2.setChecked(False)
    cnopka3.setChecked(False)
    cnopka4.setChecked(False)
    Group.setExclusive(True)

answer = [cnopka1, cnopka2, cnopka3, cnopka4]
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    rez2.setText(q.right_answer)
    show_question()
    
def check_answer():
    if answer[0].isChecked():
        rez.setText("Правильно!")
    else:
         rez.setText("Неправильно!")
    show_result()

def next_question():
    my_win.cur_question += 1
    if my_win.cur_question >= len(questions_list):
        my_win.cur_question = 0
    q = questions_list[my_win.cur_question]
    ask(q)

def click_OK():
    if knopka.text() == "Ответить":
        check_answer()
    else:
        next_question()

my_win.setLayout(linev)

q = Question("Государственный язык Бразилии", "Португальский", "Бразильский", "Испанский", "Итальянский")
ask(q)
my_win.cur_question = -1
knopka.clicked.connect(click_OK)
next_question()

#отображение окна приложения 
my_win.show()
app.exec_()