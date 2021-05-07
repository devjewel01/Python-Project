from PyQt5 import QtCore, QtGui
import cv2
from pyzbar import pyzbar

class CameraThread(QtCore.QThread):

    changePixmap = QtCore.pyqtSignal(QtGui.QImage)
    sendBarcode = QtCore.pyqtSignal(str)

    captureVid = True

    def run(self):
        cap = cv2.VideoCapture(0)

        while self.captureVid:
            captured, frame = cap.read()

            if captured:

                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QtGui.QImage(rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                cv2.waitKey(30)

                barcodes = pyzbar.decode(frame)

                for barcode in barcodes:
                    barcodeData = barcode.data.decode('utf-8')

                    self.sendBarcode.emit(barcodeData)

        cap.release()
        cv2.destroyAllWindows()