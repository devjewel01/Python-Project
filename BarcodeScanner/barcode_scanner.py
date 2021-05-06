import sys
from camera import CameraThread
from PyQt5 import Qt, QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(640, 500)

        self.cameraThread = CameraThread(self)

        # Subscribe to CameraThread signals
        self.cameraThread.changePixmap.connect(self.set_image)
        self.cameraThread.sendBarcode.connect(self.receive_barcode)

        # Create Widgets
        self.mainWidget = QtWidgets.QWidget(self)
        self.imageView = QtWidgets.QLabel('Loading...')
        self.barcodeLabel = QtWidgets.QLabel()

        # Setup layouot
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.imageView)
        layout.addWidget(self.barcodeLabel)
        self.barcodeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView.setAlignment(QtCore.Qt.AlignCenter)
        self.mainWidget.setLayout(layout)

        self.setCentralWidget(self.mainWidget)
        

    def start_camera(self):
        self.cameraThread.captureVid = True
        self.cameraThread.start()

    @QtCore.pyqtSlot(QtGui.QImage)
    def set_image(self, image):
        self.imageView.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.pyqtSlot(str)
    def receive_barcode(self, barcode):
        self.barcodeLabel.setText('Barcode: ' + barcode)


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()

    window.start_camera()

    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()