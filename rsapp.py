# This Python file uses the following encoding: utf-8
import sys
import asyncio
from RSA_Algo import *
import PySide6.QtAsyncio as QtAsyncio
from PySide6.QtWidgets import QApplication, QWidget

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
        self.bitsize = self.ui.label

        # Stelle sicher, dass wir async aufrufen, wenn der Event-Loop läuft
        # asyncio.get_event_loop().create_task(self.main())

        # Platzhalter für Schlüssel
        self.public_key = None
        self.private_key = None

    # async def main(self):
    #     # Schlüsselgenerierung im Thread auslagern, da sie evtl. blockierend ist
    #     self.public_key, self.private_key = await asyncio.to_thread(self.gen)

    async def generate(self):
        # Beispielhafte Generierung (anpassen je nach RSA_Algo)
        keys = await generate(int(self.bitsize.text()))  # Annahme: synchroner Funktionsaufruf
        # print(self.bitsize)
        return keys


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    widget = RSApp()
    widget.show()
    QtAsyncio.run(coro=None, keep_running=True, quit_qapp=True)
    sys.exit(app.exec())

    # QtAsyncio.run() ist wichtig, damit asyncio + Qt funktioniert

