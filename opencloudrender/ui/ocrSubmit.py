# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrSubmit.ui'
#
# Created: Sat Apr  4 23:12:32 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OpenCloudRenderSubmit(object):
    def setupUi(self, OpenCloudRenderSubmit):
        OpenCloudRenderSubmit.setObjectName("OpenCloudRenderSubmit")
        OpenCloudRenderSubmit.resize(1400, 305)
        OpenCloudRenderSubmit.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(OpenCloudRenderSubmit)
        self.centralwidget.setObjectName("centralwidget")
        self.scenesTableView = QtGui.QTableView(self.centralwidget)
        self.scenesTableView.setGeometry(QtCore.QRect(40, 20, 1161, 160))
        self.scenesTableView.setAcceptDrops(True)
        self.scenesTableView.setObjectName("scenesTableView")
        self.submitScenesButton = QtGui.QPushButton(self.centralwidget)
        self.submitScenesButton.setGeometry(QtCore.QRect(1210, 110, 170, 30))
        self.submitScenesButton.setObjectName("submitScenesButton")
        self.syncAssetsButton = QtGui.QPushButton(self.centralwidget)
        self.syncAssetsButton.setGeometry(QtCore.QRect(1210, 70, 170, 30))
        self.syncAssetsButton.setObjectName("syncAssetsButton")
        self.syncImagesButton = QtGui.QPushButton(self.centralwidget)
        self.syncImagesButton.setGeometry(QtCore.QRect(1210, 150, 170, 30))
        self.syncImagesButton.setObjectName("syncImagesButton")
        self.addScenesButton = QtGui.QPushButton(self.centralwidget)
        self.addScenesButton.setEnabled(False)
        self.addScenesButton.setGeometry(QtCore.QRect(1210, 20, 170, 30))
        self.addScenesButton.setObjectName("addScenesButton")
        self.dataBucketName = QtGui.QLineEdit(self.centralwidget)
        self.dataBucketName.setGeometry(QtCore.QRect(140, 190, 341, 20))
        self.dataBucketName.setObjectName("dataBucketName")
        self.repoBucketName = QtGui.QLineEdit(self.centralwidget)
        self.repoBucketName.setGeometry(QtCore.QRect(630, 190, 341, 20))
        self.repoBucketName.setObjectName("repoBucketName")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 225, 1161, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.dataBucketNameLabel = QtGui.QLabel(self.centralwidget)
        self.dataBucketNameLabel.setGeometry(QtCore.QRect(41, 190, 100, 20))
        self.dataBucketNameLabel.setObjectName("dataBucketNameLabel")
        self.repoBucketNameLabel = QtGui.QLabel(self.centralwidget)
        self.repoBucketNameLabel.setGeometry(QtCore.QRect(490, 190, 140, 20))
        self.repoBucketNameLabel.setObjectName("repoBucketNameLabel")
        self.dragDropOnlyLabel = QtGui.QLabel(self.centralwidget)
        self.dragDropOnlyLabel.setGeometry(QtCore.QRect(1220, 50, 151, 20))
        self.dragDropOnlyLabel.setObjectName("dragDropOnlyLabel")
        self.vrayVersionComboBox = QtGui.QComboBox(self.centralwidget)
        self.vrayVersionComboBox.setGeometry(QtCore.QRect(1080, 185, 121, 26))
        self.vrayVersionComboBox.setObjectName("vrayVersionComboBox")
        self.vrayVersionLabel = QtGui.QLabel(self.centralwidget)
        self.vrayVersionLabel.setGeometry(QtCore.QRect(980, 190, 91, 20))
        self.vrayVersionLabel.setObjectName("vrayVersionLabel")
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setEnabled(False)
        self.cancelButton.setGeometry(QtCore.QRect(1210, 220, 170, 30))
        self.cancelButton.setObjectName("cancelButton")
        self.progressMessagelabel = QtGui.QLabel(self.centralwidget)
        self.progressMessagelabel.setGeometry(QtCore.QRect(40, 250, 1161, 20))
        self.progressMessagelabel.setObjectName("progressMessagelabel")
        OpenCloudRenderSubmit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(OpenCloudRenderSubmit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 20))
        self.menubar.setObjectName("menubar")
        OpenCloudRenderSubmit.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OpenCloudRenderSubmit)
        self.statusbar.setObjectName("statusbar")
        OpenCloudRenderSubmit.setStatusBar(self.statusbar)

        self.retranslateUi(OpenCloudRenderSubmit)
        QtCore.QMetaObject.connectSlotsByName(OpenCloudRenderSubmit)

    def retranslateUi(self, OpenCloudRenderSubmit):
        OpenCloudRenderSubmit.setWindowTitle(QtGui.QApplication.translate("OpenCloudRenderSubmit", "OpenCloudRender", None, QtGui.QApplication.UnicodeUTF8))
        self.submitScenesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "submit scenes", None, QtGui.QApplication.UnicodeUTF8))
        self.syncAssetsButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync assets", None, QtGui.QApplication.UnicodeUTF8))
        self.syncImagesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync images", None, QtGui.QApplication.UnicodeUTF8))
        self.addScenesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "add .vrscene/.ass files", None, QtGui.QApplication.UnicodeUTF8))
        self.dataBucketNameLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "S3 Data Bucket", None, QtGui.QApplication.UnicodeUTF8))
        self.repoBucketNameLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "S3 Repository Bucket", None, QtGui.QApplication.UnicodeUTF8))
        self.dragDropOnlyLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "drag&drop only for now", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "V-Ray Version", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.progressMessagelabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "progressMessageLabel", None, QtGui.QApplication.UnicodeUTF8))

