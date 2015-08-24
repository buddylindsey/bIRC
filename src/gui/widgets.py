from PySide import QtCore, QtGui


class MessageTextArea(QtGui.QLineEdit):
    send_message = QtCore.Signal()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.send_message.emit()
        super().keyPressEvent(event)


class CentralWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.text_area = QtGui.QTextEdit()
        self.message = MessageTextArea()
        self.connect_button = QtGui.QPushButton('Connect', self)
        self.disconnect_button = QtGui.QPushButton('Disconnect', self)

        self.text_area.setReadOnly(True)

        message_layout = QtGui.QHBoxLayout()
        message_layout.setContentsMargins(5, 5, 5, 5)
        message_layout.addWidget(self.message)
        message_layout.addWidget(self.connect_button)
        message_layout.addWidget(self.disconnect_button)

        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(self.text_area)

        main_layout = QtGui.QVBoxLayout(self)
        main_layout.addLayout(layout)
        main_layout.addLayout(message_layout)

