# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import asyncio
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_RSApp(object):
    def setupUi(self, RSApp):
        if not RSApp.objectName():
            RSApp.setObjectName(u"RSApp")
        RSApp.resize(800, 600)
        self.textEdit = QTextEdit(RSApp)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(570, 60, 160, 30))
        self.textEdit.setStyleSheet(u"")
        self.label = QLabel(RSApp)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 40, 141, 16))
        self.plainTextEdit = QPlainTextEdit(RSApp)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(60, 40, 480, 200))
        self.label_2 = QLabel(RSApp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 12, 171, 16))
        self.pushButton = QPushButton(RSApp)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(560, 100, 181, 24))

        self.retranslateUi(RSApp)
        self.pushButton.clicked.connect(lambda: asyncio.ensure_future(RSApp.generate()))

        QMetaObject.connectSlotsByName(RSApp)
    # setupUi
    
    async def test(self, t):
        await t
    def retranslateUi(self, RSApp):
        RSApp.setWindowTitle(QCoreApplication.translate("RSApp", u"RSApp", None))
#         self.textEdit.setHtml(QCoreApplication.translate("RSApp", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "hr { height: 1px; border-width: 0; }\n"
# "li.unchecked::marker { content: \"\\2610\"; }\n"
# "li.checked::marker { content: \"\\2612\"; }\n"
# "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">512</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("RSApp", u"Enter a bit size i =< 1024:", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("RSApp", u"1024", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("RSApp", u"1023", None))
        self.label_2.setText(QCoreApplication.translate("RSApp", u"Input your message to encrypt:", None))
        self.pushButton.setText(QCoreApplication.translate("RSApp", u"Generate public and private key", None))
    # retranslateUi

