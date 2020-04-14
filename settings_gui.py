# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QButtonGroup, QProgressBar, QScrollArea


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 600)
        Dialog.setMinimumSize(QtCore.QSize(720, 0))
        Dialog.setMaximumSize(QtCore.QSize(720, 16777215))
        self.verticalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        scroll = QScrollArea(Dialog)
        # scroll.setLayout(self.verticalLayout)
        scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 211, 215))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_33 = QtWidgets.QFrame(Dialog)
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.verticalLayout.addWidget(self.line_33)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Генерация шаблона
        # Генерируем комбобоксы в лейаут 2
        count_settings = 18
        font = QtGui.QFont()
        font.setPointSize(10)
        items = [str(i + 1) for i in range(count_settings)]
        settings_name_list = (
            'Длина предложения',
            'Количество запятых',
            'Количество других знаков препинания',
            'Количество существительных',
            'Количество глаголов',
            'Количество пригательных',
            'Количество местоимений',
            'Количество наречий',
            'Количество причастий',
            'Количество деепричастий',
            'Количество союзов',
            'Количество частиц',
            'Количество предлогов',
            'Количество междометий',
            'Количество компаративов',
            'Количество числительных',
            'Количество чисел',
            'Количество грамматических основ'
        )

        self.color_font_list = {
            "0": "#aa5557",
            "1": "#aa5794",
            "2": "#aa5794",
            "3": "#5f99aa",
            "4": "#5f99aa",
            "5": "#5f99aa",
            "6": "#5f99aa",
            "7": "#5f99aa",
            "8": "#61aa82",
            "9": "#61aa82",
            "10": "#aa8463",
            "11": "#aa8463",
            "12": "#aa8463",
            "13": "#aa8463",
            "14": "#5f99aa",
            "15": "#ababab",
            "16": "#ababab",
            "17": "#aaaa7f"
        }

        self.combo_list = []
        self.spinBox_list = []
        self.label_list = []
        self.button_list = []

        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)

        i = 0
        while i < count_settings:
            horizontal_layout = QtWidgets.QHBoxLayout()

            # Спейсер
            spacerItem = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
            horizontal_layout.addItem(spacerItem)

            # Приоритет
            combo = QComboBox()
            combo.setMaximumSize(QtCore.QSize(50, 16777215))
            combo.setFont(font)
            combo.addItems(items)
            combo.setCurrentText(items[i])
            combo.setObjectName("comboBox{}".format(i))
            self.combo_list.append(combo)
            horizontal_layout.addWidget(combo)

            #Спейсер
            spacerItem = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
            horizontal_layout.addItem(spacerItem)

            # Название настройки
            label = QtWidgets.QLabel()
            label.setMaximumSize(QtCore.QSize(150, 16777215))
            label.setMinimumSize(QtCore.QSize(150, 16777215))
            label.setFont(font)
            label.setWordWrap(True)
            label.setText(settings_name_list[i])
            horizontal_layout.addWidget(label)

            # Спейсер
            spacerItem = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
            horizontal_layout.addItem(spacerItem)

            # Количество
            spinBox = QtWidgets.QSpinBox()
            spinBox.setMaximumSize(QtCore.QSize(50, 16777215))
            if i == 0:
                spinBox.setValue(11)
            spinBox.setFont(font)
            # spinBox.setAlignment(QtCore.Qt.AlignCenter)
            spinBox.setReadOnly(False)
            spinBox.setObjectName("spinBox{}".format(i))
            self.spinBox_list.append(spinBox)
            horizontal_layout.addWidget(spinBox)

            # Спейсер
            spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            horizontal_layout.addItem(spacerItem)


            # Цвета
            label = QtWidgets.QLabel()
            label.setMaximumSize(QtCore.QSize(100, 16777215))
            label.setMinimumSize(QtCore.QSize(100, 16777215))
            label.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
            label.setFont(font)
            label.setWordWrap(True)
            label.setText("текущий цвет")
            label.setAutoFillBackground(True)
            pal = label.palette()
            pal.setColor(QtGui.QPalette.Window, QtGui.QColor(self.color_font_list["{}".format(i)]))
            label.setPalette(pal)
            label.setObjectName("label{}".format(i))
            self.label_list.append(label)
            horizontal_layout.addWidget(label)

            button = QtWidgets.QPushButton()
            button.setMaximumSize(QtCore.QSize(100, 16777215))
            button.setMinimumSize(QtCore.QSize(100, 16777215))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            button.setFont(font)
            button.setText("Изменить цвет")
            # button.clicked.connect(Dialog.openColorDialog)
            button.setObjectName("button{}".format(i))
            self.button_list.append(button)
            self.btn_grp.addButton(button)
            horizontal_layout.addWidget(button)

            self.verticalLayout.addLayout(horizontal_layout)
            i += 1

        self.btn_grp.buttonClicked.connect(Dialog.openColorDialog)

        line = QtWidgets.QFrame(Dialog)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(line)

        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        self.pushButtonStart = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStart.sizePolicy().hasHeightForWidth())
        self.pushButtonStart.setSizePolicy(sizePolicy)
        self.pushButtonStart.setMinimumSize(150, 30)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName("pushButtonStart")

        self.pushButtonStart.clicked.connect(Dialog.start_analisys)
        self.horizontalLayout_3.addWidget(self.pushButtonStart)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setTextVisible(True)
        self.progressBar.setVisible(False)

        self.verticalLayout.addWidget(self.progressBar)
        #self.verticalLayout_2.addLayout(self.verticalLayout)


        scroll.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(scroll)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки плагина"))
        self.label.setText(_translate("Dialog", "Выберете подходящие настройки (1 - высокий приоритет; 16 - низкий; количество 0 - поле не учитывается):"))
        self.label_3.setText(_translate("Dialog", '<html><head/><body><p align="center">Приоритет</p><p align="center"> выделения</p><p align="center"> цветом</p><p align="center">1- высокий</p><p align="center">18 - низкий</p></body></html>'))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>Название настройки</p><p>для предложения</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Количество "))
        self.label_5.setText(_translate("Dialog", "Цвета выделений предложений"))
        self.pushButtonStart.setText(_translate("Dialog", "Начать анализ"))