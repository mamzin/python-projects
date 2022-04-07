#author: avmamzin
from PyQt4 import QtCore, QtGui
import sys, random

class Bingo_Window(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 362)
        MainWindow.setMinimumSize(QtCore.QSize(600, 362))
        MainWindow.setMaximumSize(QtCore.QSize(600, 362))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowTitle("Russian Loto")

        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(3, 10, 381, 151))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Computer")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(3, 180, 381, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setTitle("Player")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 10, 201, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setTitle("Bag with number")

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 280, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Take the number\nout of the bag")
        self.pushButton.setEnabled(False)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 250, 121, 21))
        self.label.setObjectName("label")
        self.label.setText("Current number: ")

        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 361, 121))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(3)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        self.tableWidget_2 = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 20, 361, 121))
        self.tableWidget_2.setEnabled(False)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setAutoScroll(False)
        self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(3)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(40)

        self.tableWidget_3 = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidget_3.setEnabled(False)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 20, 181, 201))
        self.tableWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_3.setAutoScroll(False)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.setColumnCount(9)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(20)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(20)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.setText("New game")
        self.action.setShortcut("Ctrl+N")
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.setText("Exit")
        self.action_3.setShortcut("Esc")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menu.setTitle("Menu")


        QtCore.QObject.connect(self.action_3, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.action, QtCore.SIGNAL("triggered()"), self.Game_Generation)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.Take_Btn_Pressed)
        QtCore.QObject.connect(self.tableWidget, QtCore.SIGNAL("cellClicked(int,int)"), self.Paint_Cell)
        QtCore.QObject.connect(self.tableWidget_2, QtCore.SIGNAL("cellClicked(int,int)"), self.Paint_Cell2)


    def Paint_Cell(self, x, y):
        cell_Data = self.tableWidget.item(x, y).text()
        if len(cell_Data) > 0:
            item = QtGui.QTableWidgetItem()
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.Dense5Pattern)
            item.setText(cell_Data)
            item.setBackground(brush)
            self.tableWidget.setItem(x, y, item)

    def Paint_Cell2(self, x, y):
        cell_Data = self.tableWidget_2.item(x, y).text()
        if len(cell_Data) > 0:
            item = QtGui.QTableWidgetItem()
            brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
            brush.setStyle(QtCore.Qt.Dense5Pattern)
            item.setText(cell_Data)
            item.setBackground(brush)
            self.tableWidget_2.setItem(x, y, item)


    def Game_Generation(self):
        self.label.setText("Current number: ")
        self.pushButton.setEnabled(True)
        self.tableWidget.setEnabled(True)
        self.tableWidget_2.setEnabled(True)
        self.Clear_Table(self.tableWidget)
        self.Clear_Table(self.tableWidget_2)
        self.list_Bag = [ i + 1 for i in range(0, 90)]
        self.Fill_Table(self.list_Bag)
        self.Fill_Card(self.tableWidget)
        self.Fill_Card(self.tableWidget_2)



    def Fill_Table(self, list_Table):
        try:
            cell = 0
            for row_Count in range(0, 10):
                for column_Count in range(0, 9):
                    self.tableWidget_3.setItem(row_Count, column_Count, QtGui.QTableWidgetItem(str(list_Table[cell])))
                    cell +=1
        except:
            return


    def Clear_Table(self, which_Table):
        cell = 0
        for row_Count in range(0, 10):
            for column_Count in range(0, 9):
                which_Table.setItem(row_Count, column_Count, QtGui.QTableWidgetItem(""))
                cell +=1


    def Fill_Card(self, which_Card):
        play_Number = random.sample(self.list_Bag, 15)
        first_Line = play_Number[0:5]
        first_Line.sort()
        second_Line = play_Number[5:10]
        second_Line.sort()
        third_Line = play_Number[10:15]
        third_Line.sort()
        for i in range(0, 4):
            first_Line.insert(random.randrange(0, 5, 1), "")
            second_Line.insert(random.randrange(0, 5, 1), "")
            third_Line.insert(random.randrange(0, 5, 1), "")
        cell = 0
        for column_Count in range(0, 9):
            which_Card.setItem(0, column_Count, QtGui.QTableWidgetItem(str(first_Line[cell])))
            which_Card.setItem(1, column_Count, QtGui.QTableWidgetItem(str(second_Line[cell])))
            which_Card.setItem(2, column_Count, QtGui.QTableWidgetItem(str(third_Line[cell])))
            cell +=1



    def Take_Btn_Pressed(self):
        self.Clear_Table(self.tableWidget_3)
        if len(self.list_Bag) > 0:
            rand_Num = random.choice(self.list_Bag)
            self.label.setText("Current number: " + str(rand_Num))
            self.list_Bag.remove(rand_Num)
            self.Fill_Table(self.list_Bag)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Bingo_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())