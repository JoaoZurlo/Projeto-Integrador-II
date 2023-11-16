# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 995)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFocusPolicy(Qt.NoFocus)
        self.frame.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame.setLayoutDirection(Qt.RightToLeft)
        self.frame.setStyleSheet(u"background-color: rgb(8, 8, 8);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(80, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout.addWidget(self.label_16)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(80, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.btn_pg_import = QPushButton(self.frame)
        self.btn_pg_import.setObjectName(u"btn_pg_import")
        self.btn_pg_import.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(80, 0, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_pg_import)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(80, 0, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"IMG/images-removebg-preview.png"))
        self.logo.setWordWrap(True)

        self.horizontalLayout.addWidget(self.logo)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.pg_table.setStyleSheet(u"background-color: rgb(141, 28, 30);")
        self.horizontalLayout_8 = QHBoxLayout(self.pg_table)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_3 = QVBoxLayout(self.tables)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_34 = QLabel(self.tables)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.label_34)

        self.tw_estoque = QTreeWidget(self.tables)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(9, font);
        __qtreewidgetitem.setFont(8, font);
        __qtreewidgetitem.setFont(7, font);
        __qtreewidgetitem.setFont(6, font);
        __qtreewidgetitem.setFont(5, font);
        __qtreewidgetitem.setFont(4, font);
        __qtreewidgetitem.setFont(3, font);
        __qtreewidgetitem.setFont(2, font);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setFont(0, font);
        self.tw_estoque.setHeaderItem(__qtreewidgetitem)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.tw_estoque)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_35 = QLabel(self.tables)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.label_35)

        self.tw_saida = QTreeWidget(self.tables)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setFont(9, font);
        __qtreewidgetitem1.setFont(8, font);
        __qtreewidgetitem1.setFont(7, font);
        __qtreewidgetitem1.setFont(6, font);
        __qtreewidgetitem1.setFont(5, font);
        __qtreewidgetitem1.setFont(4, font);
        __qtreewidgetitem1.setFont(3, font);
        __qtreewidgetitem1.setFont(2, font);
        __qtreewidgetitem1.setFont(1, font);
        __qtreewidgetitem1.setFont(0, font);
        self.tw_saida.setHeaderItem(__qtreewidgetitem1)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.tw_saida)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.frame_4 = QFrame(self.tables)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.btn_ = QPushButton(self.frame_4)
        self.btn_.setObjectName(u"btn_")
        self.btn_.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"\n"
"	\n"
"	background-color: rgb(21, 63, 30);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_)

        self.label_21 = QLabel(self.frame_4)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_6.addWidget(self.label_21)

        self.btn_gerar = QPushButton(self.frame_4)
        self.btn_gerar.setObjectName(u"btn_gerar")
        self.btn_gerar.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(100, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_gerar)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_6.addWidget(self.label_22)

        self.btn_estorno = QPushButton(self.frame_4)
        self.btn_estorno.setObjectName(u"btn_estorno")
        self.btn_estorno.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(136, 136, 0);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_estorno)

        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_6.addWidget(self.label_23)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_32 = QLabel(self.tab_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 60))
        self.label_32.setStyleSheet(u"color: rgb(80, 0, 0);")

        self.verticalLayout_7.addWidget(self.label_32)

        self.txt_search = QLineEdit(self.tab_2)
        self.txt_search.setObjectName(u"txt_search")
        self.txt_search.setMinimumSize(QSize(0, 20))
        self.txt_search.setFont(font)
        self.txt_search.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.txt_search.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.txt_search)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.btn_chart = QPushButton(self.tab_2)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setMinimumSize(QSize(0, 35))
        self.btn_chart.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"\n"
"	\n"
"	border-radius: 13px;\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_chart)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 35))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius: 13px;\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.horizontalLayout_16.addWidget(self.btn_excel)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.tb_geral = QTableView(self.tab_2)
        self.tb_geral.setObjectName(u"tb_geral")

        self.verticalLayout_7.addWidget(self.tb_geral)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_table)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.pg_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_2)

        self.label_33 = QLabel(self.pg_home)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setPixmap(QPixmap(u":/Imagens/19632223305.jpg"))
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_33)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.btn_pg_cadastro.setFont(font1)
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.494, radius:0.5, fx:0.5, fy:0.5, stop:0.40796 rgba(134, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.btn_pg_cadastro)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.pg_cadastro.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_17 = QLabel(self.pg_cadastro)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(80, 0, 0);")

        self.verticalLayout_8.addWidget(self.label_17)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_29 = QLabel(self.pg_cadastro)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_12.addWidget(self.label_29)

        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.label_7)

        self.label_28 = QLabel(self.pg_cadastro)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_12.addWidget(self.label_28)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setMaximumSize(QSize(60, 28))
        self.label_8.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMaximumSize(QSize(16777215, 27))
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")

        self.horizontalLayout_9.addWidget(self.txt_nome)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(60, 28))
        self.label_12.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_12)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setMaximumSize(QSize(16777215, 27))
        self.txt_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")

        self.horizontalLayout_15.addWidget(self.txt_usuario)


        self.verticalLayout_8.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(60, 28))
        self.label_9.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_9)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMaximumSize(QSize(16777215, 27))
        self.txt_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_13.addWidget(self.txt_senha)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(60, 28))
        self.label_10.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_10)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setMaximumSize(QSize(16777215, 27))
        self.txt_senha_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_14.addWidget(self.txt_senha_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_25 = QLabel(self.pg_cadastro)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_10.addWidget(self.label_25)

        self.label_18 = QLabel(self.pg_cadastro)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color:rgb(103, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_10.addWidget(self.label_13, 0, Qt.AlignVCenter)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.cb_perfil)

        self.label_26 = QLabel(self.pg_cadastro)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_10.addWidget(self.label_26)

        self.label_19 = QLabel(self.pg_cadastro)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setLayoutDirection(Qt.LeftToRight)
        self.btn_cadastrar.setAutoFillBackground(False)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(122, 0, 0);\n"
"	border-radius: 15px;\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(98, 98, 98);\n"
"	\n"
"\n"
"}")
        self.btn_cadastrar.setAutoExclusive(False)

        self.horizontalLayout_11.addWidget(self.btn_cadastrar)

        self.label_15 = QLabel(self.pg_cadastro)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.pg_sobre.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_9 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_30 = QLabel(self.pg_sobre)
        self.label_30.setObjectName(u"label_30")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_30.setFont(font3)
        self.label_30.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.label_30)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.verticalLayout_10 = QVBoxLayout(self.pg_import)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.pg_import)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_file = QLineEdit(self.pg_import)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setPointSize(12)
        self.txt_file.setFont(font4)
        self.txt_file.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.pg_import)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(120, 30))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	font: 9pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(122, 0, 0);\n"
"	\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(98, 98, 98);\n"
"	\n"
"\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_open)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.pg_import)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.btn_import = QPushButton(self.pg_import)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setLayoutDirection(Qt.LeftToRight)
        self.btn_import.setAutoFillBackground(False)
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(122, 0, 0);\n"
"	border-radius: 15px;\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(98, 98, 98);\n"
"	\n"
"\n"
"}")
        self.btn_import.setAutoExclusive(False)

        self.horizontalLayout_5.addWidget(self.btn_import)

        self.label_31 = QLabel(self.pg_import)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_5.addWidget(self.label_31)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.progressBar = QProgressBar(self.pg_import)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{	background-color: rgba(0, 0, 0,0.1);\n"
"                    	color: rgb(255, 255, 255);\n"
"                		border-style: none;\n"
"                		text-align: center;\n"
"                		border-radius:10px;\n"
"                \n"
"                }\n"
" \n"
"               \n"
"QProgressBar::chunk{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 75, 149, 255), stop:1 rgba(72, 130, 157, 255));\n"
"                				border-radius:10px;\n"
"                                }")
        self.progressBar.setValue(0)

        self.verticalLayout_10.addWidget(self.progressBar)

        self.Pages.addWidget(self.pg_import)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.tw_estoque, self.tw_saida)
        QWidget.setTabOrder(self.tw_saida, self.btn_)
        QWidget.setTabOrder(self.btn_, self.btn_gerar)
        QWidget.setTabOrder(self.btn_gerar, self.btn_estorno)
        QWidget.setTabOrder(self.btn_estorno, self.txt_nome)
        QWidget.setTabOrder(self.txt_nome, self.cb_perfil)
        QWidget.setTabOrder(self.cb_perfil, self.txt_usuario)
        QWidget.setTabOrder(self.txt_usuario, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.txt_senha_2)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label_16.setText("")
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"TABELAS", None))
        self.label_6.setText("")
        self.btn_pg_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_11.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label_5.setText("")
        self.logo.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#00aa00;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"data_saida", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"usuario", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"data_importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"qntd", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"cod", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"nome_emitente", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"chave", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"data_emiss\u00e3o", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#aa0000;\">SA\u00cdDA</span></p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(9, QCoreApplication.translate("MainWindow", u"data_saida", None));
        ___qtreewidgetitem1.setText(8, QCoreApplication.translate("MainWindow", u"usuario", None));
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("MainWindow", u"data_importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"descri\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"qntd", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"cod", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"nome_emitente", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"chave", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"data_emissao", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_20.setText("")
        self.btn_.setText(QCoreApplication.translate("MainWindow", u"GERAR ENTRADA", None))
        self.label_21.setText("")
        self.btn_gerar.setText(QCoreApplication.translate("MainWindow", u"GERAR SA\u00cdDA", None))
        self.label_22.setText("")
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"ESTORNO", None))
        self.label_23.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"BASE", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#000000;\">ESTOQUE</span><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#000000;\">:</span></p></body></html>", None))
        self.txt_search.setText(QCoreApplication.translate("MainWindow", u"FILTRO", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"GERAR GR\u00e1FICO", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"GERAR EXCEL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">PROJETO INTEGRADOR II:</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Sistema de Gerenciamento de Estoque</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">( LEANDRO E JO\u00c3O )</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_33.setText("")
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#670000;\">TELA DE CADASTRO:</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastrar Usu\u00e1rio</p></body></html>", None))
        self.label_28.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"  NOME:   ", None))
        self.txt_nome.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u" USU\u00c1RIO:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"  SENHA:  ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"  SENHA:  ", None))
        self.label_25.setText("")
        self.label_18.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">PERFIL:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Adiministrador", None))

        self.label_26.setText("")
        self.label_19.setText("")
        self.label_14.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_15.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">SOBRE:</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:10pt; font-style:italic; text-decoration: underline; color:#ffffff;\">DESENVOLVEDORES: </span></p><p align=\"center\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline; color:#ffffff;\">Jo\u00e3o Paulo Zurlo e Leandro Feitosa Rodrigues</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">Este trabalho prop\u00f5e a cria\u00e7\u00e3o de uma aplica\u00e7\u00e3o web para solucionar um problema identificado pelos estudantes na </span></p><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">prefeitura de Porangaba relacionado ao controle de estoquede pe\u00e7as para a manuten\u00e7\u00e3o da frota publica da divis\u00e3"
                        "o de </span></p><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">transportes. A solu\u00e7\u00e3o idealizada se baseia na cria\u00e7\u00e3o de umsistema de banco de dados, utilizando MySQL, baseado </span></p><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">em nuvem, que tem por objetivo proporcionar um controle eficiente, com f\u00e1cil manuten\u00e7\u00e3o e que evitar\u00e1 compras </span></p><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">desnecess\u00e1rias de produtos, permitir\u00e1 uma otimiza\u00e7\u00e3o no tempo do processo, assim evitando compras emerg\u00eancias, </span></p><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">isto \u00e9 que n\u00e3o seguem as melhores pr\u00e1ticas impostas pela Lei 8666, gerando menor indisponibilidade de ve\u00edculos, </span></p><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">promovendo incremento na qualidade dos servi\u00e7os prestadospela divis\u00e3o de transportes do m"
                        "unic\u00edpio. A metodologia </span></p><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">utilizou entrevistas e foi seguidade prototipagem.<br/></span></p><p align=\"center\"><span style=\" color:#000000;\"><br/></span></p><p align=\"center\"><span style=\" color:#000000;\"><br/></span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">IMPORTAR XML:</span></p><p align=\"center\"><br/><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML --->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

