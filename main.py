import pyodbc
import win32com.client
import sys



from windowNDFL import Ui_NDFForm
from PyQt5 import QtWidgets


#def printallfolder():  # печатает номера и списки папок в Outlook
#    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
 #   for i in range(50):
  #      try:
   #         box = outlook.GetDefaultFolder(i)
    #        name = box.Name
     #       print(i, name)
      #  except:
       #     pass


def myRuleForWriеt(subject, senername, body):  # правило для записи в базу данных
    if (('Cлужебная записка') in subject) and (('Сергей Черный') in senername):
        listOfsubject = subject.split()
        WriteToBD(listOfsubject[3], listOfsubject[5], body)
    return None


def readMail():  # берет последнее письмо из Входящих
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 папка можно изменить на другую
    print(inbox)
    messages = inbox.Items
    message = messages.GetLast()
    myRuleForWriеt(message.subject, message.SenderName, message.body)


def WriteToBD(Number_of_SZ, Date_of_SZ, Body_of_SZ):
    try:
        connection_to_db = pyodbc.connect(
            r'Driver={SQL Server};Server=DESKTOP-EPARK0G\SQLEXPRESS;Database=AkBarsOutlookPars;Trusted_Connection=yes;')
        W_code = 3
        cursor = connection_to_db.cursor()
        cursor.execute("INSERT into List_of_SZ([Number_of_SZ],[Date_of_SZ],[Body_of_SZ],[W_code]) VALUES (?,?,?,?)",
                       Number_of_SZ, Date_of_SZ, Body_of_SZ, W_code)
        cursor.commit()
    except:
        print("Что-то пошло не так в БД при записи письма")
    connection_to_db.close()


readMail()


class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NDFForm()  # Экземпляр класса Ui_NDFForm, в нем конструктор всего GUI.
        self.ui.setupUi(self)  # Инициализация GUI


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())
