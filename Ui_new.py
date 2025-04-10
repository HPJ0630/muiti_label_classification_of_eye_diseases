# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)
import ui_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1772, 1221)
        font = QFont()
        font.setFamilies([u"\u5e7c\u5706"])
        font.setPointSize(1)
        Form.setFont(font)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(160, 190, 1280, 770))
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:-0.5, y1:0.5, x2:1, y2:0, stop:0 rgba(100, 146, 230, 250), stop:1 rgba(220, 220, 223, 255));\n"
"border-radius: 15px;")
        self.titlebar = QWidget(self.widget)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setGeometry(QRect(0, 0, 1281, 41))
        self.titlebar.setStyleSheet(u"QWidget {\n"
"    border: 2px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #f0f0f0; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"")
        self.label_14 = QLabel(self.titlebar)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, -12, 151, 71))
        self.label_14.setStyleSheet(u"QLabel {\n"
"    background: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u672c */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    padding: 0px; /* \u65e0\u989d\u5916\u5185\u8fb9\u8ddd */\n"
"    font: inherit; /* \u7ee7\u627f\u7236\u7ea7\u5b57\u4f53 */\n"
"}\n"
"")
        self.label_14.setPixmap(QPixmap(u":/logo/touming_logo.png"))
        self.label_14.setScaledContents(True)
        self.mininum_button = QPushButton(self.titlebar)
        self.mininum_button.setObjectName(u"mininum_button")
        self.mininum_button.setGeometry(QRect(1130, 0, 75, 41))
        self.mininum_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #f0f0f0; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"	image: url(:/logo/minimize.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #969696;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #7f7f7f;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #969696;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #7f7f7f;\n"
"}\n"
"")
        self.close_button = QPushButton(self.titlebar)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(1206, 0, 75, 41))
        self.close_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #f0f0f0; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"	image: url(:/logo/close.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #969696;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #7f7f7f;\n"
"}\n"
"")
        self.label_7 = QLabel(self.titlebar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(360, 0, 571, 41))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    background: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    color: #4a556f; /* \u9ed1\u8272\u6587\u672c */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    padding: 0px; /* \u65e0\u989d\u5916\u5185\u8fb9\u8ddd */\n"
"    font: inherit; /* \u7ee7\u627f\u7236\u7ea7\u5b57\u4f53 */\n"
"}\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(880, 518, 391, 231))
        self.widget_6.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(135, 151, 255);\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    border: 2px solid #53a0ff;  /* 2px \u5bbd\u7684\u767d\u8272\u8fb9\u6846 */\n"
"    border-radius: 8px;  /* \u5706\u89d2\u8fb9\u6846\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"")
        self.pushButton_5 = QPushButton(self.widget_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(45, 30, 130, 70))
        font2 = QFont()
        font2.setFamilies([u"\u5e7c\u5706"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    border: 0px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #90aaff; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFC0CB;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #FFC0CB;\n"
"	color: #FFFFFF;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #FFC0CB;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #FFC0CB;\n"
"}\n"
"")
        self.pushButton_6 = QPushButton(self.widget_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(45, 130, 130, 70))
        font3 = QFont()
        font3.setFamilies([u"\u5e7c\u5706"])
        font3.setPointSize(14)
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    border: 0px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #90aaff; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFC0CB;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #FFC0CB;\n"
"	color: #FFFFFF;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #FFC0CB;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #FFC0CB;\n"
"}\n"
"")
        self.pushButton_8 = QPushButton(self.widget_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(215, 30, 130, 70))
        self.pushButton_8.setFont(font3)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    border: 0px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #90aaff; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFC0CB;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #FFC0CB;\n"
"	color: #FFFFFF;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #FFC0CB;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #FFC0CB;\n"
"}\n"
"")
        self.pushButton_7 = QPushButton(self.widget_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(215, 130, 130, 70))
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    border: 0px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 10px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #90aaff; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFC0CB;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #FFC0CB;\n"
"	color: #FFFFFF;\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #FFC0CB;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #FFC0CB;\n"
"}\n"
"")
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(880, 78, 391, 421))
        self.textBrowser.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(135, 151, 255);\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    border: 2px solid #53a0ff;  /* 2px \u5bbd\u7684\u767d\u8272\u8fb9\u6846 */\n"
"    border-radius: 8px;  /* \u5706\u89d2\u8fb9\u6846\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(880, 45, 111, 25))
        self.label_15.setStyleSheet(u"QLabel {\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    color: black;  /* \u9ed1\u8272\u5b57\u4f53 */\n"
"    font-size: 16px;  /* \u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold;  /* \u5b57\u4f53\u52a0\u7c97\uff0c\u53ef\u9009 */\n"
"    border: none;  /* \u65e0\u8fb9\u6846 */\n"
"}\n"
"")
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(1090, 45, 181, 25))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    color: black;  /* \u9ed1\u8272\u5b57\u4f53 */\n"
"    font-size: 16px;  /* \u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold;  /* \u5b57\u4f53\u52a0\u7c97\uff0c\u53ef\u9009 */\n"
"    border: none;  /* \u65e0\u8fb9\u6846 */\n"
"}\n"
"")
        self.time_label = QLabel(self.widget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(50, 45, 241, 25))
        self.time_label.setStyleSheet(u"QLabel {\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    color: black;  /* \u9ed1\u8272\u5b57\u4f53 */\n"
"    font-size: 16px;  /* \u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold;  /* \u5b57\u4f53\u52a0\u7c97\uff0c\u53ef\u9009 */\n"
"    border: none;  /* \u65e0\u8fb9\u6846 */\n"
"}\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 45, 25, 25))
        self.label.setStyleSheet(u"QLabel {\n"
"    background: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u672c */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    padding: 0px; /* \u65e0\u989d\u5916\u5185\u8fb9\u8ddd */\n"
"    font: inherit; /* \u7ee7\u627f\u7236\u7ea7\u5b57\u4f53 */\n"
"}\n"
"")
        self.label.setPixmap(QPixmap(u":/logo/clock.png"))
        self.label.setScaledContents(True)
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(360, 77, 500, 250))
        self.label_13.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(135, 151, 255);\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    border: 2px solid #b2cdff;  /* 2px \u5bbd\u7684\u767d\u8272\u8fb9\u6846 */\n"
"    border-radius: 8px;  /* \u5706\u89d2\u8fb9\u6846\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 368, 501, 131))
        font4 = QFont()
        font4.setFamilies([u"\u5e7c\u5706"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(135, 151, 255);\n"
"	color: #54ad39;\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    border: 2px solid #b2cdff;  /* 2px \u5bbd\u7684\u767d\u8272\u8fb9\u6846 */\n"
"    border-radius: 8px;  /* \u5706\u89d2\u8fb9\u6846\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(360, 333, 111, 31))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    color: black;  /* \u9ed1\u8272\u5b57\u4f53 */\n"
"    font-size: 16px;  /* \u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold;  /* \u5b57\u4f53\u52a0\u7c97\uff0c\u53ef\u9009 */\n"
"    border: none;  /* \u65e0\u8fb9\u6846 */\n"
"}\n"
"")
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(360, 45, 111, 25))
        self.label_18.setStyleSheet(u"QLabel {\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    color: black;  /* \u9ed1\u8272\u5b57\u4f53 */\n"
"    font-size: 16px;  /* \u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold;  /* \u5b57\u4f53\u52a0\u7c97\uff0c\u53ef\u9009 */\n"
"    border: none;  /* \u65e0\u8fb9\u6846 */\n"
"}\n"
"")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 77, 321, 251))
        self.widget_2.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(135, 151, 255);\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    border: 2px solid #ffffff;  /* 2px \u5bbd\u7684\u767d\u8272\u8fb9\u6846 */\n"
"    border-radius: 8px;  /* \u5706\u89d2\u8fb9\u6846\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 45, 31, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border: 0px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 0px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #f0f0f0; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"	image: url(:/logo/image.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #969696;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #7f7f7f;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #969696;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #7f7f7f;\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 155, 31, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 0px solid white; /* \u6574\u4f53\u8fb9\u6846\u767d\u8272 */\n"
"    border-radius: 0px; /* \u8bbe\u7f6e\u5012\u89d2\u7684\u534a\u5f84 */\n"
"    background-color: #f0f0f0; /* \u80cc\u666f\u8272\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"	image: url(:/logo/image.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #969696;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #7f7f7f;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #969696;  /* \u9f20\u6807\u60ac\u505c\u989c\u8272 */\n"
"    border: 2px solid #7f7f7f;\n"
"}\n"
"")
        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(52, 40, 261, 41))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    color: black;  /* \u9ed1\u8272\u5b57\u4f53 */\n"
"    font-size: 16px;  /* \u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold;  /* \u5b57\u4f53\u52a0\u7c97\uff08\u53ef\u9009\uff09 */\n"
"    border: none;  /* \u53d6\u6d88\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    border-bottom: 2px solid black;  /* \u9ed1\u8272\u5e95\u90e8\u8fb9\u6846 */\n"
"    border-top: 2px solid rgba(255, 255, 255, 150);  /* \u534a\u900f\u660e\u767d\u8272\u9876\u90e8\u8fb9\u6846 */\n"
"}\n"
"")
        self.lineEdit_4 = QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(52, 150, 261, 41))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    color: black;  /* \u9ed1\u8272\u5b57\u4f53 */\n"
"    font-size: 16px;  /* \u5b57\u4f53\u5927\u5c0f */\n"
"    font-weight: bold;  /* \u5b57\u4f53\u52a0\u7c97\uff08\u53ef\u9009\uff09 */\n"
"    border: none;  /* \u53d6\u6d88\u9ed8\u8ba4\u8fb9\u6846 */\n"
"    border-bottom: 2px solid black;  /* \u9ed1\u8272\u5e95\u90e8\u8fb9\u6846 */\n"
"    border-top: 2px solid rgba(255, 255, 255, 150);  /* \u534a\u900f\u660e\u767d\u8272\u9876\u90e8\u8fb9\u6846 */\n"
"}\n"
"")
        self.eye_image = QLabel(self.widget)
        self.eye_image.setObjectName(u"eye_image")
        self.eye_image.setGeometry(QRect(69, 339, 251, 161))
        self.eye_image.setStyleSheet(u"QLabel {\n"
"    background: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u672c */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    padding: 0px; /* \u65e0\u989d\u5916\u5185\u8fb9\u8ddd */\n"
"    font: inherit; /* \u7ee7\u627f\u7236\u7ea7\u5b57\u4f53 */\n"
"}\n"
"")
        self.eye_image.setPixmap(QPixmap(u":/logo/eye.png"))
        self.eye_image.setScaledContents(True)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 350, 54, 33))
        font5 = QFont()
        font5.setFamilies([u"SimSun"])
        font5.setPointSize(22)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    background: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u672c */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    padding: 0px; /* \u65e0\u989d\u5916\u5185\u8fb9\u8ddd */\n"
"    font: inherit; /* \u7ee7\u627f\u7236\u7ea7\u5b57\u4f53 */\n"
"}\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 389, 54, 33))
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    background: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u672c */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    padding: 0px; /* \u65e0\u989d\u5916\u5185\u8fb9\u8ddd */\n"
"    font: inherit; /* \u7ee7\u627f\u7236\u7ea7\u5b57\u4f53 */\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 466, 54, 33))
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"QLabel {\n"
"    background: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u672c */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    padding: 0px; /* \u65e0\u989d\u5916\u5185\u8fb9\u8ddd */\n"
"    font: inherit; /* \u7ee7\u627f\u7236\u7ea7\u5b57\u4f53 */\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 428, 54, 32))
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    background: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    color: black; /* \u9ed1\u8272\u6587\u672c */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    padding: 0px; /* \u65e0\u989d\u5916\u5185\u8fb9\u8ddd */\n"
"    font: inherit; /* \u7ee7\u627f\u7236\u7ea7\u5b57\u4f53 */\n"
"}\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        brush = QBrush(QColor(0, 0, 0, 250))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setBackground(brush);
        __qtablewidgetitem.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 520, 831, 231))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: transparent; /* \u900f\u660e\u80cc\u666f */\n"
"    gridline-color: white; /* \u7f51\u683c\u7ebf\u989c\u8272 */\n"
"    border: 1px solid white; /* \u6dfb\u52a0\u767d\u8272\u8fb9\u6846 */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"    text-align: center; /* \u5c45\u4e2d\u5bf9\u9f50 */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: transparent; /* \u900f\u660e\u8868\u5934 */\n"
"    border: none; /* \u53bb\u6389\u8fb9\u6846 */\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: transparent; /* \u900f\u660e\u5de6\u4e0a\u89d2 */\n"
"    border: none;\n"
"}\n"
"")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(40, 340, 56, 151))
        self.widget_3.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(135, 151, 255);\n"
"    background: transparent;  /* \u900f\u660e\u80cc\u666f */\n"
"    border: 0px solid #53a0ff;  /* 2px \u5bbd\u7684\u767d\u8272\u8fb9\u6846 */\n"
"    border-radius: 8px;  /* \u5706\u89d2\u8fb9\u6846\uff0c\u53ef\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_14.setText("")
        self.mininum_button.setText("")
        self.close_button.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u57fa\u4e8e\u773c\u5e95\u533b\u5b66\u5f71\u50cf\u7684\u773c\u79d1\u75be\u75c5\u667a\u80fd\u8bca\u65ad\u7cfb\u7edf", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u7ed3\u679c", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u6279\u91cf\u68c0\u6d4b", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e\u7cfb\u7edf", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u7cfb\u7edf\u65e5\u5fd7", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8bbe\u5907\uff1a", None))
        self.time_label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u65f6\u95f4", None))
        self.label.setText("")
        self.label_13.setText("")
        self.label_2.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"\u8bca\u65ad\u7ed3\u679c", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u53cc\u76ee\u56fe\u50cf", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"path to the left eye image", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"path to the right eye image", None))
        self.eye_image.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u795d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u60a8", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5eb7", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5065", None))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem = self.tableWidget.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u5de6\u773c\u8def\u5f84", None));
        ___qtablewidgetitem3 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u53f3\u773c\u8def\u5f84", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u7ed3\u679c", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

