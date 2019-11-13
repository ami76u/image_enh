# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Brent\Desktop\MainWindowAdvanced.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PIL import ImageEnhance
import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # select image button

        self.selectImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageBtn.setGeometry(QtCore.QRect(200, 500, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.selectImageBtn.setFont(font)
        self.selectImageBtn.setObjectName("selectImageBtn")

       
        # remove noise button

        self.rvnoise = QtWidgets.QPushButton(self.centralwidget)
        self.rvnoise.setGeometry(QtCore.QRect(500, 500, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.rvnoise.setFont(font)
        self.rvnoise.setObjectName("brightBtn")
        self.rvnoise.setText("RemoveNoise")
        
        #blur button

        self.blurBtn = QtWidgets.QPushButton(self.centralwidget)
        self.blurBtn.setGeometry(QtCore.QRect(650, 500, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.blurBtn.setFont(font)
        self.blurBtn.setObjectName("blurBtn")
        self.blurBtn.setText("EnhanceBlur")

        # main image label
        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(50, 50, 700, 400))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")

        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(500, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menufilters = QtWidgets.QMenu(self.menubar)
        self.menufilters.setObjectName("menufilters")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actioncrop = QtWidgets.QAction(MainWindow)
        self.actioncrop.setObjectName("actioncrop")
        self.actionzoom = QtWidgets.QAction(MainWindow)
        self.actionzoom.setObjectName("actionzoom")
        self.actionundo = QtWidgets.QAction(MainWindow)
        self.actionundo.setObjectName("actionundo")
        self.actionredo = QtWidgets.QAction(MainWindow)
        self.actionredo.setObjectName("actionredo")
        self.actionmax = QtWidgets.QAction(MainWindow)
        self.actionmax.setObjectName("actionmax")
        self.actionmin = QtWidgets.QAction(MainWindow)
        self.actionmin.setObjectName("actionmin")
        self.actionmedian = QtWidgets.QAction(MainWindow)
        self.actionmedian.setObjectName("actionmedian")
        self.actionhistogram = QtWidgets.QAction(MainWindow)
        self.actionhistogram.setObjectName("actionhistogram")
        self.actionlaplace = QtWidgets.QAction(MainWindow)
        self.actionlaplace.setObjectName("actionlaplace")
        self.actioninvert = QtWidgets.QAction(MainWindow)
        self.actioninvert.setObjectName("actioninvert")
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionexit)
        self.menuedit.addSeparator()
        self.menuedit.addSeparator()
        self.menuedit.addAction(self.actioncrop)
        self.menuedit.addAction(self.actionzoom)
        self.menuedit.addAction(self.actionundo)
        self.menuedit.addAction(self.actionredo)
        self.menufilters.addAction(self.actionmax)
        self.menufilters.addAction(self.actionmin)
        self.menufilters.addAction(self.actionmedian)
        self.menufilters.addAction(self.actionhistogram)
        self.menufilters.addAction(self.actionlaplace)
        #self.actionlaplace.triggered.connect(self.setBright)
        self.menufilters.addAction(self.actioninvert)
        #self.actioninvert.triggered.connect(self.invert)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menufilters.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # button click action

        self.selectImageBtn.clicked.connect(self.setImage)
        self.rvnoise.clicked.connect(self.setBright)
        self.blurBtn.clicked.connect(self.setblur)
       
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectImageBtn.setText(_translate("MainWindow", "Select Image"))
        #self.enhanceBtn.setText(_translate("MainWindow", "enhance"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.menufilters.setTitle(_translate("MainWindow", "filters"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actioncrop.setText(_translate("MainWindow", "crop"))
        self.actionzoom.setText(_translate("MainWindow", "zoom "))
        self.actionundo.setText(_translate("MainWindow", "undo"))
        self.actionredo.setText(_translate("MainWindow", "redo"))
        self.actionmax.setText(_translate("MainWindow", "max"))
        self.actionmin.setText(_translate("MainWindow", "min"))
        self.actionmedian.setText(_translate("MainWindow", "median"))
        self.actionhistogram.setText(_translate("MainWindow", "histogram"))
        self.actionlaplace.setText(_translate("MainWindow", "laplace"))
        self.actioninvert.setText(_translate("MainWindow", "invert"))

    def setImage(self):
        global fileName
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            # Setup pixmap with the provided image
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(
            ), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.imageLbl.setPixmap(pixmap)  # Set the pixmap onto the label
            # Align the label to center
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)

    def setBright(self):
       # Reading image from folder where it is stored
        image = Image.open(fileName) 
        image.save("a.png")
        img = cv2.imread("a.png") 
       
        median = cv2.medianBlur(img, 5)
        cv2.imshow("Median", median)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def setblur(self):
        black = (0,0,0)
        white = (255,255,255)
        threshold = (160,160,160)

        # Open input image in grayscale mode and get its pixels.
        img = Image.open(fileName).convert()
        pixels = img.getdata()

        newPixels = []

        # Compare each pixel 
        for pixel in pixels:
            if pixel < threshold:
               newPixels.append(black)
            else:
               newPixels.append(white)

         # Create and save new image.
        newImg = Image.new("RGB",img.size)
        newImg.putdata(newPixels)
        newImg.save("newImage.jpg")
        pixmap = QtGui.QPixmap("newImage.jpg")
        pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio)
        self.imageLbl.setPixmap(pixmap)
        self.imageLbl.setAlignment(QtCore.Qt.AlignCenter)


   

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
