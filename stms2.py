#author: avmamzin
from PyQt4 import QtCore, QtGui
import sys, os, subprocess, win32com.client

class FormSTMS(object):

    def Setup_Form(self, MainWindow):
        MainWindow.setMinimumSize(QtCore.QSize(190, 50))
        MainWindow.setMaximumSize(QtCore.QSize(190, 50))
        MainWindow.setWindowTitle("STMS 2.0")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.png"), QtGui.QIcon.Normal)
        MainWindow.setWindowIcon(icon)

        self.text_Pass = QtGui.QLineEdit(MainWindow)
        self.text_Pass.setGeometry(QtCore.QRect(10, 20, 115, 25))
        self.text_Pass.setEchoMode(QtGui.QLineEdit.Password)

        self.pushButton_Pass = QtGui.QPushButton(MainWindow)
        self.pushButton_Pass.setGeometry(QtCore.QRect(130, 20, 50, 25))
        self.pushButton_Pass.setText("Ok")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Pass.setFont(font)

        self.textEdit_Req = QtGui.QLineEdit(MainWindow)
        self.textEdit_Req.setGeometry(QtCore.QRect(15, 20, 85, 23))
        self.textEdit_Req.setMaxLength(10)
        self.textEdit_Req.setVisible(False)

        self.comboBox_SID = QtGui.QComboBox(MainWindow)
        self.comboBox_SID.setGeometry(QtCore.QRect(110, 20, 50, 22))
        self.comboBox_SID.addItem("")
        self.comboBox_SID.setVisible(False)

        self.comboBox_MNDT = QtGui.QComboBox(MainWindow)
        self.comboBox_MNDT.setGeometry(QtCore.QRect(175, 20, 50, 22))
        self.comboBox_MNDT.setVisible(False)

        self.radioButton_Copy = QtGui.QRadioButton(MainWindow)
        self.radioButton_Copy.setGeometry(QtCore.QRect(245, 10, 82, 17))
        self.radioButton_Copy.setChecked(True)
        self.radioButton_Copy.setText("Only copy")
        self.radioButton_Copy.setToolTip("Copy file, run chmod 664, add to buffer")
        self.radioButton_Copy.setVisible(False)

        self.radioButton_Import = QtGui.QRadioButton(MainWindow)
        self.radioButton_Import.setGeometry(QtCore.QRect(245, 28, 82, 17))
        self.radioButton_Import.setText("With import")
        self.radioButton_Import.setToolTip("Copy file, run chmod 664, add to buffer, import request")
        self.radioButton_Import.setVisible(False)

        self.pushButton_Go = QtGui.QPushButton(MainWindow)
        self.pushButton_Go.setGeometry(QtCore.QRect(335, 12, 50, 30))
        self.pushButton_Go.setText("START")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Go.setFont(font)

        self.Browser_Log = QtGui.QTextBrowser(MainWindow)
        self.Browser_Log.setGeometry(QtCore.QRect(10, 50, 380, 360))
        self.Browser_Log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Browser_Log.setReadOnly(True)
        self.Browser_Log.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(15, 4, 215, 13))
        self.label.setText("Input tp request:    Target SID and mandant:")
        self.label.setVisible(False)

        self.label_Pass = QtGui.QLabel(MainWindow)
        self.label_Pass.setGeometry(QtCore.QRect(10, 4, 150, 16))
        self.label_Pass.setText("Input password for config file:")

        self.groupBox = QtGui.QGroupBox(MainWindow)
        self.groupBox.setGeometry(QtCore.QRect(10, 410, 380, 100))
        self.groupBox.setTitle("Import options")
        self.groupBox.setEnabled(False)

        self.checkBox_Key0 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Key0.setGeometry(QtCore.QRect(5, 15, 170, 17))
        self.checkBox_Key0.setChecked(True)
        self.checkBox_Key0.setText("Leave request for later import")

        self.checkBox_Key1 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Key1.setGeometry(QtCore.QRect(5, 35, 170, 17))
        self.checkBox_Key1.setText("Import request again")

        self.checkBox_Key2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Key2.setGeometry(QtCore.QRect(5, 55, 170, 17))
        self.checkBox_Key2.setText("Overwrite originals")

        self.checkBox_Key6 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Key6.setGeometry(QtCore.QRect(5, 75, 220, 17))
        self.checkBox_Key6.setText("Overwrite objects in unconfirmed repairs")

        self.checkBox_Key9 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Key9.setGeometry(QtCore.QRect(180, 15, 345, 17))
        self.checkBox_Key9.setText("Ignore non-permitted transport type")

        self.checkBox_Key8 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Key8.setGeometry(QtCore.QRect(180, 35, 345, 17))
        self.checkBox_Key8.setText("Ignore non-permitted table class")

        self.checkBox_Key3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_Key3.setGeometry(QtCore.QRect(180, 55, 345, 17))
        self.checkBox_Key3.setText("Ignore predecessor relations")

        QtCore.QObject.connect(self.pushButton_Go, QtCore.SIGNAL("clicked()"), self.Go_Btn_Pressed)
        QtCore.QObject.connect(self.pushButton_Pass, QtCore.SIGNAL("clicked()"), self.Pass_Btn_Pressed)
        QtCore.QObject.connect(self.comboBox_SID, QtCore.SIGNAL("currentIndexChanged(int)"), self.Update_ComboBox_SID)
        QtCore.QObject.connect(self.text_Pass, QtCore.SIGNAL("returnPressed()"), self.Pass_Btn_Pressed)
        QtCore.QObject.connect(self.radioButton_Import, QtCore.SIGNAL("toggled(bool)"), self.groupBox.setEnabled)

    def Check_Rec_Files(self):
        self.cur_Dir = os.getcwd()
        if not os.path.exists(self.cur_Dir + "\\plink.exe"):
            self.Add_Browser_Log("<font color=red>Not found plink.exe in current folder! Please, check it, put plink.exe in current folder with stms2.bat!</font>")
        if not os.path.exists(self.cur_Dir + "\\pscp.exe"):
            self.Add_Browser_Log("<font color=red>Not found pscp.exe in current folder! Please, check it, put pscp.exe in current folder with stms2.bat!</font>")
        if not os.path.exists(self.cur_Dir + "\\Temp"):
            self.Add_Browser_Log("<font color=red>Not found directory Temp in current folder! Please, check it, create directory Temp in current folder with stms2.bat!</font>")
        if not os.path.exists(self.cur_Dir + "\\config.xlsx"):
            self.Add_Browser_Log("<font color=red>Not found config.xlsx in current folder! Please, check it, put config.txt in current folder with stms2.bat!</font>")
            return "not_Conf"

    def Update_ComboBox_SID(self):
        self.comboBox_MNDT.clear()
        temp_SID = self.comboBox_SID.currentText()
        if temp_SID != "":
            mndts_String = self.list_Mndts_Hash[temp_SID]
            temp_Split = mndts_String.split(",")
            self.comboBox_MNDT.addItems(temp_Split)

    def Read_Config(self):
        self.list_Sids = []
        self.list_Config = {}
        self.list_Hosts_Hash = {}
        self.list_Mndts_Hash = {}
        self.list_Path_Hash = {}
        self.list_Controlers_Hash = {}
        self.list_Password_Hash = {}
        count_line = 0
        row = 0
        filename = self.cur_Dir + "\\config.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        xlWb = xlApp.Workbooks.Open(filename, 0, True, None, self.pass_Admin)
        xlSht = xlWb.WorkSheets("conf")
        while xlSht.Cells(row + 1, 1).value != None:
            self.list_Config[row] = xlSht.Cells(row + 1, 1).value
            row += 1
        for line in self.list_Config.values():
            temp_Split = line.split(" ")
            self.list_Sids.append(temp_Split[0])
            self.list_Hosts_Hash[self.list_Sids[count_line]] = temp_Split[1]
            self.list_Mndts_Hash[self.list_Sids[count_line]] = temp_Split[2]
            self.list_Path_Hash[self.list_Sids[count_line]] = temp_Split[3]
            self.list_Controlers_Hash[self.list_Sids[count_line]] = temp_Split[4]
            self.list_Password_Hash[self.list_Sids[count_line]] = temp_Split[5]
            count_line += 1
        self.comboBox_SID.addItems(self.list_Sids)
        xlWb.Close()

    def Pass_Btn_Pressed(self):
        if len(self.text_Pass.text()) > 1:
            self.pass_Admin = self.text_Pass.text()
            self.text_Pass.setVisible(False)
            self.label_Pass.setVisible(False)
            self.pushButton_Pass.setVisible(False)
            MainWindow.setMinimumSize(QtCore.QSize(400, 515))
            MainWindow.setMaximumSize(QtCore.QSize(400, 515))
            self.textEdit_Req.setVisible(True)
            self.comboBox_SID.setVisible(True)
            self.comboBox_MNDT.setVisible(True)
            self.radioButton_Copy.setVisible(True)
            self.radioButton_Import.setVisible(True)
            self.label.setVisible(True)
            if self.Check_Rec_Files() != "not_Conf":
                self.Read_Config()

    def Go_Btn_Pressed(self):
        if self.textEdit_Req.text() == "":
            self.Add_Browser_Log("<font color=red>Need to fill in all the data! Please, input name of request!</font>")
        elif len(self.textEdit_Req.text()) != 10:
            self.Add_Browser_Log("<font color=red>Short name of request! Please, check request field!</font>")
        elif self.comboBox_SID.currentText() == "":
            self.Add_Browser_Log("<font color=red>Need to fill in all the data! Please, input name of target system!</font>")
        else:
            req_Text = self.textEdit_Req.text()
            source_Sid = req_Text[0:3].upper()
            req_file = req_Text[4:10].upper()
            target_Sid = self.comboBox_SID.currentText()
            target_Mndt = self.comboBox_MNDT.currentText()
            source_Host = self.Which_Server(source_Sid)
            target_Host = self.Which_Server(target_Sid)
            user_Source = source_Sid.lower() + "adm"
            user_Target = target_Sid.lower() + "adm"

            if source_Host == "not_Host":
                self.Add_Browser_Log("<font color=red>Host with SID " + source_Sid + " not found! Please, check request field!</font>")
                raise

            pass_Source_Sid = self.Which_Password(source_Sid)
            pass_Target_Sid = self.Which_Password(target_Sid)
            source_Path = self.Which_Path(source_Sid)
            target_Path = self.Which_Path(target_Sid)
            target_Controler = self.list_Controlers_Hash[target_Sid]
            self.Add_Browser_Log("<font color=blue>Start task for request " + req_Text + " from " + source_Sid + " to " + target_Sid + "/" + target_Mndt)

            self.Add_Browser_Log("<font color=green>Copying files to local computer(in Temp)...</font>")
            command_Connect_Source_CopyR = "pscp.exe -scp -pw " + pass_Source_Sid + " " + user_Source + "@" + source_Host + ":" + source_Path + "data/R" + req_file + "." + source_Sid + " .\\Temp\\R" + req_file + "." + source_Sid
            answer_Connect_Source_CopyR = self.Connect_Host(command_Connect_Source_CopyR)
            self.Add_Browser_Log(answer_Connect_Source_CopyR)
            command_Connect_Source_CopyK = "pscp.exe -scp -pw " + pass_Source_Sid + " " + user_Source + "@" + source_Host + ":" + source_Path + "cofiles/K" + req_file + "." + source_Sid + " .\\Temp\\K" + req_file + "." + source_Sid
            answer_Connect_Source_CopyK = self.Connect_Host(command_Connect_Source_CopyK)
            self.Add_Browser_Log(answer_Connect_Source_CopyK)

            self.Add_Browser_Log("<font color=green>Copying files to " + target_Sid + "(" + target_Host + ")...</font>")
            command_Connect_Target_CopyR = "pscp.exe -scp -pw " + pass_Target_Sid + " .\\Temp\\R" + req_file + "." + source_Sid + " " + user_Target + "@" + target_Host + ":" + target_Path + "data/R" + req_file + "." + source_Sid
            answer_Connect_Target_CopyR = self.Connect_Host(command_Connect_Target_CopyR)
            self.Add_Browser_Log(answer_Connect_Target_CopyR)
            command_Connect_Target_CopyK = "pscp.exe -scp -pw " + pass_Target_Sid + " .\\Temp\\K" + req_file + "." + source_Sid + " " + user_Target + "@" + target_Host + ":" + target_Path + "cofiles/K" + req_file + "." + source_Sid
            answer_Connect_Target_CopyK = self.Connect_Host(command_Connect_Target_CopyK)
            self.Add_Browser_Log(answer_Connect_Target_CopyK)

            self.Add_Browser_Log("<font color=green>Chmod 664 for files on " + target_Sid + "(" + target_Host + ")...</font>")
            command_Connect_Chmod = "plink.exe -ssh -pw " + pass_Target_Sid + " " + user_Target + "@" + target_Host + " sudo chmod 664 " + target_Path + "cofiles/K" + req_file + "." + source_Sid
            answer_Connect_Chmod = self.Connect_Host(command_Connect_Chmod)
            self.Add_Browser_Log(answer_Connect_Chmod)
            command_Connect_Chmod = "plink.exe -ssh -pw " + pass_Target_Sid + " " + user_Target + "@" + target_Host + " sudo chmod 664 " + target_Path + "data/R" + req_file + "." + source_Sid
            answer_Connect_Chmod = self.Connect_Host(command_Connect_Chmod)
            self.Add_Browser_Log(answer_Connect_Chmod)

            command_Connect_AddBuffer_Tp = " tp addtobuffer " + req_Text + " " + target_Sid + " pf=" + target_Path + "bin/" + target_Controler
            command_Connect_AddBuffer = "plink.exe -ssh -pw " + pass_Target_Sid + " " + user_Target + "@" + target_Host + command_Connect_AddBuffer_Tp
            self.Add_Browser_Log("<font color=green>Command for adding file to buffer: " + command_Connect_AddBuffer_Tp + "</font>")
            answer_Connect_AddBuffer = self.Connect_Host(command_Connect_AddBuffer)
            self.Add_Browser_Log(answer_Connect_AddBuffer)

            if self.radioButton_Import.isChecked():
                import_Options = self.Which_Options()
                if import_Options != "":
                    import_Options = ' u' + import_Options
                command_Connect_Import_Tp = " tp import " + req_Text + " " + target_Sid + " client" + target_Mndt + import_Options + " pf=" + target_Path + "bin/" + target_Controler
                command_Connect_Import = "plink.exe -ssh -pw " + pass_Target_Sid + " " + user_Target + "@" + target_Host + command_Connect_Import_Tp
                self.Add_Browser_Log("<font color=green>Command for importation file: " + command_Connect_Import_Tp + "</font>")
                answer_Connect_Import = self.Connect_Host(command_Connect_Import)
                self.Add_Browser_Log(answer_Connect_Import)
                self.Add_Browser_Log("<font color=blue>Task for request " + req_Text + " from " + source_Sid + " to " + target_Sid + "/" + target_Mndt + " completed!</font>")
            else:
                self.Add_Browser_Log("<font color=blue>Task for request " + req_Text + " from " + source_Sid + " to " + target_Sid + "/" + target_Mndt + " completed!</font>")

    def Connect_Host(self, command):
        connect_query = subprocess.Popen(command, stdout=subprocess.PIPE)
        out = str(connect_query.stdout.read())
        return out

    def Which_Server(self, sid):
        try:
            name_Host = self.list_Hosts_Hash[sid]
            return name_Host
        except:
            return "not_Host"

    def Which_Path(self, sid):
        name_Path = self.list_Path_Hash[sid]
        return name_Path

    def Which_Password(self, sid):
        name_Password = self.list_Password_Hash[sid]
        return name_Password

    def Which_Options(self):
        u_Param = ""
        if self.checkBox_Key0.isChecked():
            u_Param = u_Param + "0"
        if self.checkBox_Key1.isChecked():
            u_Param = u_Param + "1"
        if self.checkBox_Key2.isChecked():
            u_Param = u_Param + "2"
        if self.checkBox_Key3.isChecked():
            u_Param = u_Param + "3"
        if self.checkBox_Key6.isChecked():
            u_Param = u_Param + "6"
        if self.checkBox_Key8.isChecked():
            u_Param = u_Param + "8"
        if self.checkBox_Key9.isChecked():
            u_Param = u_Param + "9"
        return u_Param

    def Add_Browser_Log(self, log_text):
        log_text = log_text.replace('b\'', '')
        log_text = log_text.replace('\'', '')
        log_text = log_text.replace('\\r', '')
        log_text = log_text.replace('\\n', '')
        self.Browser_Log.append(log_text)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = FormSTMS()
    ui.Setup_Form(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())