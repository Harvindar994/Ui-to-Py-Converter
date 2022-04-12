import os
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys
from pickle import load, dump
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser


class File(QtWidgets.QFrame):
    def __init__(self, file_name):
        super(File, self).__init__()

        self.setMinimumSize(QtCore.QSize(0, 22))
        self.setMaximumSize(QtCore.QSize(16777215, 22))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setStyleSheet("background-color:rgb(185, 210, 214) ;\n"
                                           "border-radius: 11px;")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("file_containner")
        self.file_containner_HLayout = QtWidgets.QHBoxLayout(self)
        self.file_containner_HLayout.setContentsMargins(9, 0, 0, 0)
        self.file_containner_HLayout.setSpacing(6)
        self.file_containner_HLayout.setObjectName("file_containner_HLayout")
        self.file_name = QtWidgets.QLabel(self)
        self.file_name.setStyleSheet("QLabel{\n"
                                     "    color:rgb(25, 25, 25);\n"
                                     "background: none;\n"
                                     "}")
        self.file_name.setObjectName("file_name")
        self.file_name.setText(file_name)
        self.file_containner_HLayout.addWidget(self.file_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.file_containner_HLayout.addItem(spacerItem)
        self.remove = QtWidgets.QPushButton(self)
        self.remove.setMinimumSize(QtCore.QSize(25, 0))
        self.remove.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remove.setStyleSheet("background-color: none;\n"
                                  "color: black;\n"
                                  "border-style: none;")
        self.remove.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon)
        self.remove.setIconSize(QtCore.QSize(11, 11))
        self.remove.setShortcut("")
        self.remove.setObjectName("remove")
        self.file_containner_HLayout.addWidget(self.remove)
        self.retranslateUi()

    def retranslateUi(self):
        self.remove.setToolTip('Remove')
        self.remove.setStatusTip("Remove")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UI to PY")
        MainWindow.resize(449, 263)
        self.setMaximumSize(449, 263)
        self.setMinimumSize(449, 263)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.83, y2:0.648, stop:0.00568182 rgba(114, 138, 143, 255), stop:0.494318 rgba(124, 208, 221, 255), stop:1 rgba(185, 225, 233, 255));")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.LogoContainner = QtWidgets.QFrame(self.MainFrame)
        self.LogoContainner.setGeometry(QtCore.QRect(-20, 14, 271, 47))
        self.LogoContainner.setMinimumSize(QtCore.QSize(20, 31))
        self.LogoContainner.setMaximumSize(QtCore.QSize(500, 160))
        self.LogoContainner.setStyleSheet("background:rgb(209, 238, 243);\n"
                                          "border-radius: 23px;")
        self.LogoContainner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogoContainner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogoContainner.setLineWidth(0)
        self.LogoContainner.setObjectName("LogoContainner")
        self.brightgoal = QtWidgets.QLabel(self.LogoContainner)
        self.brightgoal.setGeometry(QtCore.QRect(72, 8, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.brightgoal.setFont(font)
        self.brightgoal.setStyleSheet("background: none;\n"
                                      "")
        self.brightgoal.setText("")
        self.brightgoal.setPixmap(QtGui.QPixmap("icon/Brightgoal logo.png"))
        self.brightgoal.setScaledContents(True)
        self.brightgoal.setObjectName("brightgoal")
        self.label_brightgoal = QtWidgets.QLabel(self.LogoContainner)
        self.label_brightgoal.setGeometry(QtCore.QRect(110, 6, 97, 27))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_brightgoal.setFont(font)
        self.label_brightgoal.setStyleSheet("QLabel{\n"
                                            "    color: rgb(19, 112, 143);\n"
                                            "background: none;\n"
                                            "}")
        self.label_brightgoal.setObjectName("label_brightgoal")
        self.ui_file_path = QtWidgets.QLineEdit(self.MainFrame)
        self.ui_file_path.setGeometry(QtCore.QRect(86, 94, 299, 25))
        self.ui_file_path.setStyleSheet("background-color: rgb(255, 255, 255, 150);\n"
                                        "border-style: none;\n"
                                        "border-radius: 3px;")
        self.ui_file_path.setObjectName("ui_file_path")
        self.browse_ui_file_button = QtWidgets.QPushButton(self.MainFrame)
        self.browse_ui_file_button.setGeometry(QtCore.QRect(388, 94, 49, 25))
        self.browse_ui_file_button.setStyleSheet("background-color: none;\n"
                                                 "color: black;\n"
                                                 "border-style: none;\n"
                                                 "border-radius: 3px;")
        self.browse_ui_file_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/folder.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.browse_ui_file_button.setIcon(icon)
        self.browse_ui_file_button.setIconSize(QtCore.QSize(22, 22))
        self.browse_ui_file_button.setObjectName("browse_ui_file_button")
        self.select_output_folder_button = QtWidgets.QPushButton(self.MainFrame)
        self.select_output_folder_button.setGeometry(QtCore.QRect(388, 172, 49, 25))
        self.select_output_folder_button.setStyleSheet("background-color: none;\n"
                                                       "color: black;\n"
                                                       "border-style: none;\n"
                                                       "border-radius: 3px;")
        self.select_output_folder_button.setText("")
        self.select_output_folder_button.setIcon(icon)
        self.select_output_folder_button.setIconSize(QtCore.QSize(22, 22))
        self.select_output_folder_button.setObjectName("select_output_folder_button")
        self.python_file_path = QtWidgets.QLineEdit(self.MainFrame)
        self.python_file_path.setGeometry(QtCore.QRect(86, 172, 299, 25))
        self.python_file_path.setStyleSheet("background-color: rgb(255, 255, 255, 150);\n"
                                            "border-style: none;\n"
                                            "border-radius: 3px;")
        self.python_file_path.setObjectName("python_file_path")
        self.export_button = QtWidgets.QPushButton(self.MainFrame)
        self.export_button.setGeometry(QtCore.QRect(390, 220, 49, 25))
        self.export_button.setStyleSheet("background-color:none;\n"
                                         "color: black;\n"
                                         "border-style: none;\n"
                                         "border-radius: 3px;")
        self.export_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_button.setIcon(icon1)
        self.export_button.setIconSize(QtCore.QSize(22, 22))
        self.export_button.setObjectName("export_button")
        self.ui_file_label = QtWidgets.QLabel(self.MainFrame)
        self.ui_file_label.setGeometry(QtCore.QRect(18, 92, 57, 27))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.ui_file_label.setFont(font)
        self.ui_file_label.setStyleSheet("QLabel{\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background: none;\n"
                                         "}")
        self.ui_file_label.setObjectName("ui_file_label")
        self.python_file_label = QtWidgets.QLabel(self.MainFrame)
        self.python_file_label.setGeometry(QtCore.QRect(18, 170, 57, 27))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.python_file_label.setFont(font)
        self.python_file_label.setStyleSheet("QLabel{\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background: none;\n"
                                             "}")
        self.python_file_label.setObjectName("python_file_label")
        self.UI_to_Py_containner = QtWidgets.QFrame(self.MainFrame)
        self.UI_to_Py_containner.setGeometry(QtCore.QRect(238, 216, 147, 31))
        self.UI_to_Py_containner.setMinimumSize(QtCore.QSize(20, 31))
        self.UI_to_Py_containner.setMaximumSize(QtCore.QSize(500, 160))
        self.UI_to_Py_containner.setStyleSheet("background:rgb(209, 238, 243);\n"
                                               "border-radius: 15px;")
        self.UI_to_Py_containner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UI_to_Py_containner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UI_to_Py_containner.setLineWidth(0)
        self.UI_to_Py_containner.setObjectName("UI_to_Py_containner")
        self.qt_logo = QtWidgets.QLabel(self.UI_to_Py_containner)
        self.qt_logo.setGeometry(QtCore.QRect(20, 6, 28, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.qt_logo.setFont(font)
        self.qt_logo.setStyleSheet("background: none;")
        self.qt_logo.setText("")
        self.qt_logo.setPixmap(QtGui.QPixmap("icon/Qt.png"))
        self.qt_logo.setScaledContents(True)
        self.qt_logo.setObjectName("qt_logo")
        self.python_logo = QtWidgets.QLabel(self.UI_to_Py_containner)
        self.python_logo.setEnabled(True)
        self.python_logo.setGeometry(QtCore.QRect(108, 6, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.python_logo.setFont(font)
        self.python_logo.setStyleSheet("background: none;")
        self.python_logo.setText("")
        self.python_logo.setPixmap(QtGui.QPixmap("icon/python.png"))
        self.python_logo.setScaledContents(True)
        self.python_logo.setObjectName("python_logo")
        self.right_arrow = QtWidgets.QLabel(self.UI_to_Py_containner)
        self.right_arrow.setEnabled(True)
        self.right_arrow.setGeometry(QtCore.QRect(66, 4, 23, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.right_arrow.setFont(font)
        self.right_arrow.setStyleSheet("background: none;")
        self.right_arrow.setText("")
        self.right_arrow.setPixmap(QtGui.QPixmap("icon/right-arrow.png"))
        self.right_arrow.setScaledContents(True)
        self.right_arrow.setObjectName("right_arrow")
        self.author_containner = QtWidgets.QFrame(self.MainFrame)
        self.author_containner.setGeometry(QtCore.QRect(4, 234, 139, 27))
        self.author_containner.setStyleSheet("background: none;")
        self.author_containner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.author_containner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.author_containner.setObjectName("author_containner")
        self.author_name = QtWidgets.QLabel(self.author_containner)
        self.author_name.setGeometry(QtCore.QRect(30, 0, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Quicksand Medium")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.author_name.setFont(font)
        self.author_name.setStyleSheet("QLabel{\n"
                                       "    color:rgb(19, 112, 143);\n"
                                       "background: none;\n"
                                       "}")
        self.author_name.setObjectName("author_name")
        self.github_logo = QtWidgets.QLabel(self.author_containner)
        self.github_logo.setGeometry(QtCore.QRect(4, 2, 22, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.github_logo.setFont(font)
        self.github_logo.setStyleSheet("background: none;")
        self.github_logo.setText("")
        self.github_logo.setPixmap(QtGui.QPixmap("icon/github.png"))
        self.github_logo.setScaledContents(True)
        self.github_logo.setObjectName("github_logo")

        self.files_containner = QtWidgets.QScrollArea(self.MainFrame)
        self.files_containner.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.files_containner.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.files_containner.setGeometry(QtCore.QRect(86, 126, 299, 37))
        self.files_containner.setStyleSheet("background: rgb(214, 239, 243);\n"
                                            "border-radius: 3px;")
        self.files_containner.setWidgetResizable(True)
        self.files_containner.setAlignment(QtCore.Qt.AlignCenter)
        self.files_containner.setObjectName("files_containner")

        self.horizontalScrollbar = QtWidgets.QScrollBar()
        self.horizontalScrollbar.setMaximumHeight(4)
        self.horizontalScrollbar.setStyleSheet("""
        QScrollBar{
        background : rgb(209, 238, 243);
        height: 4px;
        }
        
        QScrollBar::handle{
        background : rgb(24, 144, 184);
        }
        
        QScrollBar::handle::pressed{
        background : rgb(25, 157, 255);
        }
        """)
        self.files_containner.setHorizontalScrollBar(self.horizontalScrollbar)

        self.files_containner_contents = QtWidgets.QWidget()
        self.files_containner_contents.setGeometry(QtCore.QRect(0, 0, 299, 37))
        self.files_containner_contents.setObjectName("files_containner_contents")
        self.files_containner_HLayout = QtWidgets.QHBoxLayout(self.files_containner_contents)
        self.files_containner_HLayout.setContentsMargins(5, 4, 5, 4)
        self.files_containner_HLayout.setSpacing(7)
        self.files_containner_HLayout.setObjectName("files_containner_HLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.files_containner_HLayout.addItem(spacerItem)
        self.files_containner.setWidget(self.files_containner_contents)
        self.horizontalLayout.addWidget(self.MainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UI to Py"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon/Brightgoal logo.png'))
        self.label_brightgoal.setText(_translate("MainWindow", "Brightgoal"))
        self.ui_file_path.setPlaceholderText(_translate("MainWindow", "Input Path ( Example.ui )"))
        self.browse_ui_file_button.setToolTip(_translate("MainWindow", "Select UI File"))
        self.browse_ui_file_button.setStatusTip(_translate("MainWindow", "Browser ui file"))
        self.select_output_folder_button.setToolTip(_translate("MainWindow", "Select Output Folder"))
        self.select_output_folder_button.setStatusTip(_translate("MainWindow", "Selelct Output Path"))
        self.python_file_path.setPlaceholderText(_translate("MainWindow", "Output Path for (Example.py)"))
        self.export_button.setToolTip(_translate("MainWindow", "Export"))
        self.export_button.setStatusTip(_translate("MainWindow", "Export"))
        self.ui_file_label.setText(_translate("MainWindow", "UI File"))
        self.python_file_label.setText(_translate("MainWindow", "Output"))
        self.UI_to_Py_containner.setToolTip(_translate("MainWindow", "UI to Py"))
        self.author_name.setText(_translate("MainWindow", "Harvindar singh"))


class Log:
    def __init__(self, log_file):
        self.file_name = log_file
        self.logs = None

    def update_logs(self, logs: object = dict) -> object:
        if type(logs) != dict:
            raise ValueError('log should be in dict type, invalid type')

        prev_log = self.get_logs()
        if prev_log is not None:
            for key, value in logs.items():
                prev_log[key] = value
        try:
            file = open(self.file_name, 'wb')
            if prev_log is not None:
                dump(prev_log, file)
            else:
                dump(logs, file)
            file.close()
        except:
            return False
        return True

    def get_logs(self):
        try:
            file = open(self.file_name, 'rb')
            self.logs = load(file)
            file.close()
        except FileNotFoundError:
            self.logs = None

        return self.logs


class Converter(QApplication):
    def __init__(self, argv=sys.argv):
        super(Converter, self).__init__(argv)
        self.window = MainWindow()
        self.window.show()

        # let's create Log object to save and Retrieve logs.
        self.log = Log('converter.log')
        self.log.get_logs()

        # Here setting up default path
        self.ui_files = []
        if self.log.logs is not None:
            if 'ui_file_dir' in self.log.logs:
                self.window.ui_file_path.setText(self.log.logs['ui_file_dir'])
                for file in self.log.logs['ui_files']:
                    self.add_file(file)

            if 'output_dir' in self.log.logs:
                self.window.python_file_path.setText(self.log.logs['output_dir'])
            else:
                self.window.python_file_path.setText(QtCore.QDir.rootPath())

        # here connecting button
        self.connect_button()

        # here disabling the text fields.
        self.disable_fields()

    def remove_file(self, file):
        if len(self.ui_files) > 0:
            self.ui_files.remove(file)
            file.hide()
            self.window.files_containner_HLayout.removeWidget(file)

    def add_file(self, file_name):
        file = File(file_name)
        self.clickable(file.remove, self.remove_file, file)
        self.ui_files.append(file)
        self.window.files_containner_HLayout.insertWidget(0, file)

    @staticmethod
    def open_url(url):
        try:
            webbrowser.get('chrome').open_new(url)
        except:
            try:
                webbrowser.get('firefox').open_new_tab(url)
            except:
                try:
                    webbrowser.open(url, new=1)
                except:
                    return False
        return True

    def connect_button(self):
        self.window.browse_ui_file_button.clicked.connect(self.browse_ui_file)
        self.window.select_output_folder_button.clicked.connect(self.select_output_path)
        self.window.export_button.clicked.connect(self.convert)
        self.clickable(self.window.author_containner, self.open_url, '"https://github.com/Harvindar994"')

    def clickable(self, widget, function, argument=None):
        class Filter(QtCore.QObject):
            def setFunctionAndValues(self, Widget, Function, Argument=None):
                self.ObjData = [Widget, Function, Argument]

            def eventFilter(self, obj, event):
                if obj == self.ObjData[0]:
                    if event.type() == QtCore.QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.ObjData[1](self.ObjData[2]) if self.ObjData[2] is not None else self.ObjData[1]()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True
                return False

        filter = Filter(widget)
        filter.setFunctionAndValues(widget, function, argument)
        widget.installEventFilter(filter)

    def open_github(self):
        self.open_url("https://github.com/Harvindar994")

    def disable_fields(self):
        self.window.python_file_path.setDisabled(True)
        self.window.ui_file_path.setDisabled(True)

    def select_output_path(self):
        # fetching logs from file.
        self.log.get_logs()
        if self.log.logs is not None and "output_dir" in self.log.logs:
            root_path = self.log.logs['output_dir']
        else:
            root_path = QtCore.QDir.rootPath()
        output_dir = str(QFileDialog.getExistingDirectory(self.window, "Select Directory", root_path))

        # Here updating los for ui file dir.
        if output_dir != "":
            self.log.update_logs({'output_dir': output_dir})
            self.window.python_file_path.setText(output_dir)

    def browse_ui_file(self):
        self.log.get_logs()
        if self.log.logs is not None and "ui_file_dir" in self.log.logs:
            root_path = self.log.logs['ui_file_dir']
        else:
            root_path = QtCore.QDir.rootPath()

        # opening window explorer.
        ui_file, _ = QFileDialog.getOpenFileNames(self.window, 'Single File', root_path, '*.ui')

        if len(ui_file) != 0:
            for file in self.ui_files:
                file.hide()
                self.window.files_containner_HLayout.removeWidget(file)

            self.ui_files = []

            for file in ui_file:
                name = os.path.basename(file)
                self.add_file(name)

            ui_file_dir = os.path.dirname(os.path.abspath(ui_file[0]))

            # Here updating los for ui file dir.
            self.log.update_logs({'ui_file_dir': ui_file_dir, 'ui_files': [os.path.basename(path) for path in ui_file]})
            self.window.ui_file_path.setText(ui_file_dir)

    def convert(self):
        ui_files_base_path = self.window.ui_file_path.text()
        for ui_file in self.ui_files:
            python_file = ui_file.file_name.text().split('.')[0]
            python_file = os.path.join(self.window.python_file_path.text(), python_file)

            # Here checking that if output file is already exist then change the name.
            if os.path.exists(os.path.join(self.window.python_file_path.text(), f"{python_file}.py")):
                count = 1
                while True:
                    if os.path.exists(os.path.join(self.window.python_file_path.text(), f"{python_file}_{count}.py")):
                        count += 1
                    else:
                        break

                python_file = os.path.join(self.window.python_file_path.text(), f"{python_file}_{count}.py")
            else:
                python_file = os.path.join(self.window.python_file_path.text(), f"{python_file}.py")

            status = subprocess.call(r'pyuic/pyuic5.exe -x ' + ('"' + os.path.join(ui_files_base_path, ui_file.file_name.text()) + '"') + ' -o ' +
                                     ('"' + python_file + '"'),
                                     stdin=None, stdout=None, stderr=None, shell=False)


if __name__ == '__main__':
    app = Converter(sys.argv)
    sys.exit(app.exec_())

