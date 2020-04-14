import sys
from time import sleep

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtWidgets import QColorDialog, QMessageBox

import settings_gui
from model_gui import Ui_MainWindow


# Диалог настройки плагина
from plugins.uploaded_sentences import UploadedSentences


class Thread(QThread):
    def __init__(self, uploaded_sentences):
        super().__init__()
        self.uploaded_sentences = uploaded_sentences
        self.result = None
        self.text = None
        self.settings = None

    def set_param(self, text, settings):
        self.text = text
        self.settings = settings

    def run(self):
        self.result = self.uploaded_sentences.text_analysis({
            "text": self.text,
            "options": self.settings
        })

        print(self.result)


class Dialog(QtWidgets.QDialog):

    def __init__(self, mainWindow):
        super().__init__()
        self.settings = dict()
        self.text = ""

        self.mainWindow = mainWindow
        self.ui = settings_gui.Ui_Dialog()
        self.ui.setupUi(self)

        self.uploaded_sentences = UploadedSentences()

        self.is_started = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.get_process_handler)
        self.timer.start(1000)

    def get_process_handler(self):
        if self.is_started:
            self.ui.progressBar.setValue(self.uploaded_sentences.processing)

    def get_text_main_window(self):
        return self.mainWindow.textEdit.toPlainText()

    def set_color_text(self, result_analisys):
        # Массив  "indexes": {
        #                             "start": 0,
        #                             "end": 0
        #                         },
        #                         "color": #fffffff
        cursor = self.mainWindow.textEdit.textCursor()
        format = QtGui.QTextCharFormat()
        for item in result_analisys:
            format.setBackground(QtGui.QBrush(QtGui.QColor(item["color"])))
            cursor.setPosition(item["indexes"]["start"])
            for i in range(item["indexes"]["start"], item["indexes"]["end"]):
                cursor.movePosition(QtGui.QTextCursor.Right, 1)
                cursor.mergeCharFormat(format)

    def start_analisys(self):
        if self.get_text_main_window():
            flag = True
            keys = [
                "word_count",
                "number of commas",
                "number of punctuation marks",
                "number of nouns",
                "number of verbs",
                "number of adjectives",
                "number of pronouns",
                "number of adverbs",
                "number of participles",
                "quantity of participles",
                "number of unions",
                "number of particles",
                "number of prepositions",
                "number of interjections",
                "number of comparatives",
                "number of numerals",
                "amount of numbers",
                "number of grammatical bases",
            ]

            temp_mass_priority = []
            i = 0
            while i < 18 and flag:
                if self.ui.spinBox_list[i].value() == 0:
                    self.settings.update({
                        keys[i]: None
                    })
                else:
                    self.settings.update({
                        keys[i]: {
                            "priority": self.ui.combo_list[i].currentText(),
                            "count": self.ui.spinBox_list[i].value(),
                            "color": self.ui.color_font_list["{}".format(i)]
                        }
                    })

                if self.ui.combo_list[i].currentText() not in temp_mass_priority:
                    temp_mass_priority.append(self.ui.combo_list[i].currentText())
                else:
                    flag = False
                i += 1

            if flag:
                # Массив  "indexes": {
                #                             "start": 0,
                #                             "end": 0
                #                         },
                #                         "color": #fffffff
                self.is_started = True
                self.ui.progressBar.setVisible(True)
                self.ui.progressBar.setValue(0)

                self.thread = Thread(self.uploaded_sentences)
                self.thread.set_param(self.get_text_main_window(), self.settings)
                self.thread.start()
                self.thread.finished.connect(self.on_finished)
                # self.is_started = False

            else:
                # Вызвать предупреждение, что не все приоритеты расставлены правильно
                self.show_dialog("Несколько полей не может иметь одинаковые приоритеты. Измените приоритеты")
        else:
            self.show_dialog("Поле для текста пустое")

    def on_finished(self):
        if self.thread.result is not None:
            if "error" in self.thread.result[-1].keys():
                self.set_color_text(self.thread.result[:len(self.thread.result) - 1])
                self.show_error_dialog(
                    "Ошибка работы плагина, попробуйте позже. Отработанный результат выведен на экран")
            else:
                self.set_color_text(self.thread.result)
                self.show_succes_dialog("Поиск успешно завершен")
        else:
            self.show_dialog("Ни одно предложение не подходит под данные настройки")


    def openColorDialog(self, btn):
        color = QColorDialog.getColor()
        if color.isValid():
            index = btn.objectName()[6:]
            self.ui.color_font_list[index] = color.name()
            pal = self.ui.label_list[int(index)].palette()
            pal.setColor(QtGui.QPalette.Window, QtGui.QColor(self.ui.color_font_list[index]))
            self.ui.label_list[int(index)].setPalette(pal)


    def show_dialog(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText(message)
        msg.setWindowTitle("Предупреждение")
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()

    def show_succes_dialog(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(message)
        msg.setWindowTitle("Поиск завершен")
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()

    def show_error_dialog(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText(message)
        msg.setWindowTitle("Ошибка")
        msg.setStandardButtons(QMessageBox.Ok)

        retval = msg.exec_()


    def exit(self):
        self.close()


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings_dialog = Dialog(self.ui)

    def open_settings_dialog(self):
        self.settings_dialog.show()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = mainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    # и запускаем приложение
    app.exec_()
    sys.exit()



# Если мы запускаем файл напрямую, а не импортируем
if __name__ == '__main__':
    main()  # то запускаем функцию main()
