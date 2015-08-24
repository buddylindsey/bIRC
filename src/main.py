import logging
import os
import sys

from PySide import QtGui, QtCore, QtNetwork

from gui.widgets import CentralWidget

logger = logging.getLogger(__name__)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.container = CentralWidget(parent=self)
        self.setCentralWidget(self.container)
        self.statusBar().showMessage('Ready!', 2000)

        self.container.connect_button.clicked.connect(self.connect_to_server)
        self.container.disconnect_button.clicked.connect(self.disconnect)
        self.container.message.send_message.connect(self.send)

        self.setWindowTitle('irc')
        self.resize(1280, 800)

        self.tcp = QtNetwork.QTcpSocket()
        self.tcp.connected.connect(self.connected)
        self.tcp.disconnected.connect(self.disconnected)
        self.tcp.error.connect(self.error)
        self.tcp.stateChanged.connect(self.state_changed)
        self.tcp.readyRead.connect(self.ready_read)

        self.connect_to_server()

    def connect_to_server(self):
        self.tcp.connectToHost('localhost', 6667)

    def connected(self):
        self.statusBar().showMessage('Connected', 1000)
        self.write_data('NICK percent22\n')
        self.write_data('USER buddyl 0 * :buddyl@localhost\n')
        self.write_data('JOIN #tulsawebdevs\n')

    def disconnect(self):
        self.write_data('QUIT :running away.\n')

    def write_data(self, msg):
        if self.tcp.state() == QtNetwork.QAbstractSocket.ConnectedState:
            self.write_messaage(msg)
            self.tcp.writeData(msg, len(msg))

    def write_messaage(self, msg):
        self.container.text_area.append(str(msg))

    def disconnected(self):
        self.write_messaage("Disconnected")

    def error(self, arg):
        self.write_messaage("error: {}".format(arg))

    def state_changed(self, arg):
        pass

    def ready_read(self):
        data = self.tcp.readAll()
        self.write_messaage(data)

    def send(self):
        text = self.container.message.text()
        self.write_data("{}\n".format(text))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
