# This Python file uses the following encoding: utf-8
import sys
import asyncio
from RSA_Algo import *
import PySide6.QtAsyncio as QtAsyncio
from PySide6.QtWidgets import QApplication, QWidget, QColormap
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor, QTextBlockFormat, QTextCharFormat

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_RSApp
import tracemalloc
tracemalloc.start()

class RSApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RSApp()
        self.ui.setupUi(self)
        self.bitsize = self.ui.plainTextEdit_2
        
        # Platzhalter für Schlüssel
        self.public_key = None
        self.private_key = None
        
    async def generate(self):
        # Beispielhafte Generierung (anpassen je nach RSA_Algo)
        self.public_key, self.private_key = await generate(int(self.bitsize.toPlainText()))  # Annahme: synchroner Funktionsaufruf
        self.ui.textBrowser.setText(f"e := {self.public_key[0]}")
        self.ui.textBrowser_2.setText(f"d := {self.private_key[0]}")
        self.ui.textBrowser_8.setText(f"N := {self.public_key[1]}")
        
    async def encrypt(self):
        if(self.public_key != None):
            self.cypher_text = await encrypt(self.ui.plainTextEdit.toPlainText(), self.public_key)
            c_text = ""
            for c in self.cypher_text:
                c_text += str(c)
                
            self.ui.encrypted_str.setText(c_text)
        
    async def decrypt(self):
        if(self.public_key != None):
            self.message = await decrypt(self.cypher_text, self.private_key)
            self.ui.encrypted_str_2.setText(f"Decrypted data := {self.message}")
    
    async def signMessage(self):
        if(self.public_key != None):
            self.sign = await sign(self.message, self.private_key)
            self.ui.encrypted_str_3.setText(str(self.sign))
        
        
    async def verifyMessage(self):
        if(self.public_key != None):
            self.isValid = await verify(self.message, self.sign, self.public_key)
        
            if self.isValid:
                self.ui.textBrowser_10.setStyleSheet('background-color: green;')
                self.ui.textBrowser_10.setHtml('<div style="text-align: center; color: white; font-size: 20px; font-weight: bold; margin-top: 40%;">VERIFIED!!</div>')
            else: 
                self.ui.textBrowser_11.setStyleSheet('background-color: red;')
                self.ui.textBrowser_11.setHtml('<div style="text-align: center; color: white; font-size: 20px; font-weight: bold; margin-top: 40%;">INVALID!!</div>')
        
    

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    widget = RSApp()
    widget.show()
    QtAsyncio.run(coro=None, keep_running=True, quit_qapp=True)
    sys.exit(app.exec())
