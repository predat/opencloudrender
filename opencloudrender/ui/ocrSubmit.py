# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrSubmit.ui'
#
# Created: Sat May  2 20:28:39 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OpenCloudRenderSubmit(object):
    def setupUi(self, OpenCloudRenderSubmit):
        OpenCloudRenderSubmit.setObjectName("OpenCloudRenderSubmit")
        OpenCloudRenderSubmit.resize(1370, 330)
        OpenCloudRenderSubmit.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(OpenCloudRenderSubmit)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 1370, 211))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.submissionTab = QtGui.QWidget()
        self.submissionTab.setObjectName("submissionTab")
        self.arnoldVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.arnoldVersionComboBox.setEnabled(False)
        self.arnoldVersionComboBox.setGeometry(QtCore.QRect(910, 0, 100, 21))
        self.arnoldVersionComboBox.setObjectName("arnoldVersionComboBox")
        self.vrayVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.vrayVersionComboBox.setGeometry(QtCore.QRect(740, 0, 100, 21))
        self.vrayVersionComboBox.setObjectName("vrayVersionComboBox")
        self.submitScenesButton = QtGui.QPushButton(self.submissionTab)
        self.submitScenesButton.setGeometry(QtCore.QRect(1175, 110, 170, 30))
        self.submitScenesButton.setObjectName("submitScenesButton")
        self.mantraVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.mantraVersionComboBox.setEnabled(False)
        self.mantraVersionComboBox.setGeometry(QtCore.QRect(1070, 0, 100, 21))
        self.mantraVersionComboBox.setObjectName("mantraVersionComboBox")
        self.syncAssetsButton = QtGui.QPushButton(self.submissionTab)
        self.syncAssetsButton.setGeometry(QtCore.QRect(1175, 70, 170, 30))
        self.syncAssetsButton.setObjectName("syncAssetsButton")
        self.scenesTableView = QtGui.QTableView(self.submissionTab)
        self.scenesTableView.setGeometry(QtCore.QRect(5, 29, 1161, 151))
        self.scenesTableView.setAcceptDrops(True)
        self.scenesTableView.setObjectName("scenesTableView")
        self.addScenesButton = QtGui.QPushButton(self.submissionTab)
        self.addScenesButton.setEnabled(False)
        self.addScenesButton.setGeometry(QtCore.QRect(1175, 30, 170, 30))
        self.addScenesButton.setObjectName("addScenesButton")
        self.arnoldVersionLabel = QtGui.QLabel(self.submissionTab)
        self.arnoldVersionLabel.setEnabled(False)
        self.arnoldVersionLabel.setGeometry(QtCore.QRect(860, 0, 45, 20))
        self.arnoldVersionLabel.setObjectName("arnoldVersionLabel")
        self.dragDropOnlyLabel = QtGui.QLabel(self.submissionTab)
        self.dragDropOnlyLabel.setGeometry(QtCore.QRect(10, 0, 531, 20))
        self.dragDropOnlyLabel.setObjectName("dragDropOnlyLabel")
        self.vrayVersionLabel = QtGui.QLabel(self.submissionTab)
        self.vrayVersionLabel.setGeometry(QtCore.QRect(700, 0, 40, 20))
        self.vrayVersionLabel.setObjectName("vrayVersionLabel")
        self.syncImagesButton = QtGui.QPushButton(self.submissionTab)
        self.syncImagesButton.setGeometry(QtCore.QRect(1175, 150, 170, 30))
        self.syncImagesButton.setObjectName("syncImagesButton")
        self.mantraVersionLabel = QtGui.QLabel(self.submissionTab)
        self.mantraVersionLabel.setEnabled(False)
        self.mantraVersionLabel.setGeometry(QtCore.QRect(1020, 0, 45, 20))
        self.mantraVersionLabel.setObjectName("mantraVersionLabel")
        self.defaultVersionLabel = QtGui.QLabel(self.submissionTab)
        self.defaultVersionLabel.setEnabled(True)
        self.defaultVersionLabel.setGeometry(QtCore.QRect(560, 0, 111, 20))
        self.defaultVersionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.defaultVersionLabel.setObjectName("defaultVersionLabel")
        self.tabWidget.addTab(self.submissionTab, "")
        self.repoTab = QtGui.QWidget()
        self.repoTab.setObjectName("repoTab")
        self.vrayRepoSyncButton = QtGui.QPushButton(self.repoTab)
        self.vrayRepoSyncButton.setGeometry(QtCore.QRect(1250, 30, 101, 20))
        self.vrayRepoSyncButton.setObjectName("vrayRepoSyncButton")
        self.vrayRepoPathGlobLineEdit = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoPathGlobLineEdit.setGeometry(QtCore.QRect(100, 30, 231, 20))
        self.vrayRepoPathGlobLineEdit.setObjectName("vrayRepoPathGlobLineEdit")
        self.vrayRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoPathGlobLabel.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.vrayRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vrayRepoPathGlobLabel.setObjectName("vrayRepoPathGlobLabel")
        self.houdiniRepoPathGlobLineEdit = QtGui.QLineEdit(self.repoTab)
        self.houdiniRepoPathGlobLineEdit.setEnabled(False)
        self.houdiniRepoPathGlobLineEdit.setGeometry(QtCore.QRect(100, 60, 231, 20))
        self.houdiniRepoPathGlobLineEdit.setObjectName("houdiniRepoPathGlobLineEdit")
        self.syncHoudiniRepoButton = QtGui.QPushButton(self.repoTab)
        self.syncHoudiniRepoButton.setEnabled(False)
        self.syncHoudiniRepoButton.setGeometry(QtCore.QRect(1250, 60, 101, 20))
        self.syncHoudiniRepoButton.setObjectName("syncHoudiniRepoButton")
        self.houdiniRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.houdiniRepoPathGlobLabel.setEnabled(False)
        self.houdiniRepoPathGlobLabel.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.houdiniRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.houdiniRepoPathGlobLabel.setObjectName("houdiniRepoPathGlobLabel")
        self.arnoldRepoPathGlobLineEdit = QtGui.QLineEdit(self.repoTab)
        self.arnoldRepoPathGlobLineEdit.setEnabled(False)
        self.arnoldRepoPathGlobLineEdit.setGeometry(QtCore.QRect(100, 90, 231, 20))
        self.arnoldRepoPathGlobLineEdit.setObjectName("arnoldRepoPathGlobLineEdit")
        self.syncArnoldRepoButton = QtGui.QPushButton(self.repoTab)
        self.syncArnoldRepoButton.setEnabled(False)
        self.syncArnoldRepoButton.setGeometry(QtCore.QRect(1250, 90, 101, 20))
        self.syncArnoldRepoButton.setObjectName("syncArnoldRepoButton")
        self.arnoldRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.arnoldRepoPathGlobLabel.setEnabled(False)
        self.arnoldRepoPathGlobLabel.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.arnoldRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.arnoldRepoPathGlobLabel.setObjectName("arnoldRepoPathGlobLabel")
        self.vrayRepoExcludesLineEdit = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoExcludesLineEdit.setGeometry(QtCore.QRect(835, 30, 261, 20))
        self.vrayRepoExcludesLineEdit.setObjectName("vrayRepoExcludesLineEdit")
        self.vrayRepoExcludesLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoExcludesLabel.setGeometry(QtCore.QRect(835, 5, 241, 20))
        self.vrayRepoExcludesLabel.setObjectName("vrayRepoExcludesLabel")
        self.houdiniRepoExcludesLineEdit = QtGui.QLineEdit(self.repoTab)
        self.houdiniRepoExcludesLineEdit.setGeometry(QtCore.QRect(835, 60, 261, 20))
        self.houdiniRepoExcludesLineEdit.setObjectName("houdiniRepoExcludesLineEdit")
        self.arnoldRepoExcludesLineEdit = QtGui.QLineEdit(self.repoTab)
        self.arnoldRepoExcludesLineEdit.setGeometry(QtCore.QRect(835, 90, 261, 20))
        self.arnoldRepoExcludesLineEdit.setText("")
        self.arnoldRepoExcludesLineEdit.setObjectName("arnoldRepoExcludesLineEdit")
        self.vrayRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.vrayRepoVersionComboBox.setGeometry(QtCore.QRect(690, 30, 100, 21))
        self.vrayRepoVersionComboBox.setObjectName("vrayRepoVersionComboBox")
        self.vrayRepoVersionComboBox.addItem("")
        self.vrayRepoVersionComboBox.addItem("")
        self.localVersionLabel = QtGui.QLabel(self.repoTab)
        self.localVersionLabel.setGeometry(QtCore.QRect(700, 5, 91, 20))
        self.localVersionLabel.setObjectName("localVersionLabel")
        self.vrayRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.vrayRepoBrowseButton.setGeometry(QtCore.QRect(340, 30, 61, 20))
        self.vrayRepoBrowseButton.setObjectName("vrayRepoBrowseButton")
        self.houdiniRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.houdiniRepoBrowseButton.setEnabled(False)
        self.houdiniRepoBrowseButton.setGeometry(QtCore.QRect(340, 60, 61, 20))
        self.houdiniRepoBrowseButton.setObjectName("houdiniRepoBrowseButton")
        self.houdiniRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.houdiniRepoVersionComboBox.setEnabled(False)
        self.houdiniRepoVersionComboBox.setGeometry(QtCore.QRect(690, 60, 100, 21))
        self.houdiniRepoVersionComboBox.setObjectName("houdiniRepoVersionComboBox")
        self.houdiniRepoVersionComboBox.addItem("")
        self.houdiniRepoVersionComboBox.addItem("")
        self.arnoldRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.arnoldRepoBrowseButton.setEnabled(False)
        self.arnoldRepoBrowseButton.setGeometry(QtCore.QRect(340, 90, 61, 20))
        self.arnoldRepoBrowseButton.setObjectName("arnoldRepoBrowseButton")
        self.arnoldRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.arnoldRepoVersionComboBox.setEnabled(False)
        self.arnoldRepoVersionComboBox.setGeometry(QtCore.QRect(690, 90, 100, 21))
        self.arnoldRepoVersionComboBox.setObjectName("arnoldRepoVersionComboBox")
        self.arnoldRepoVersionComboBox.addItem("")
        self.arnoldRepoVersionComboBox.addItem("")
        self.localRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.localRepoPathGlobLabel.setGeometry(QtCore.QRect(100, 5, 131, 20))
        self.localRepoPathGlobLabel.setObjectName("localRepoPathGlobLabel")
        self.vrayRepoStripPathPrefixLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoStripPathPrefixLabel.setGeometry(QtCore.QRect(420, 5, 131, 20))
        self.vrayRepoStripPathPrefixLabel.setObjectName("vrayRepoStripPathPrefixLabel")
        self.vrayRepoStripPathPrefixLineEdit = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoStripPathPrefixLineEdit.setGeometry(QtCore.QRect(420, 30, 231, 20))
        self.vrayRepoStripPathPrefixLineEdit.setObjectName("vrayRepoStripPathPrefixLineEdit")
        self.tabWidget.addTab(self.repoTab, "")
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setEnabled(False)
        self.cancelButton.setGeometry(QtCore.QRect(1175, 255, 170, 25))
        self.cancelButton.setObjectName("cancelButton")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(5, 260, 1161, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.dataBucketNameLabel = QtGui.QLabel(self.centralwidget)
        self.dataBucketNameLabel.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.dataBucketNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dataBucketNameLabel.setObjectName("dataBucketNameLabel")
        self.dataBucketName = QtGui.QLineEdit(self.centralwidget)
        self.dataBucketName.setGeometry(QtCore.QRect(140, 10, 530, 20))
        self.dataBucketName.setObjectName("dataBucketName")
        self.repoBucketNameLabel = QtGui.QLabel(self.centralwidget)
        self.repoBucketNameLabel.setGeometry(QtCore.QRect(710, 10, 121, 20))
        self.repoBucketNameLabel.setObjectName("repoBucketNameLabel")
        self.repoBucketName = QtGui.QLineEdit(self.centralwidget)
        self.repoBucketName.setGeometry(QtCore.QRect(835, 10, 521, 20))
        self.repoBucketName.setObjectName("repoBucketName")
        OpenCloudRenderSubmit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1370, 22))
        self.menubar.setObjectName("menubar")
        OpenCloudRenderSubmit.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OpenCloudRenderSubmit)
        self.statusbar.setObjectName("statusbar")
        OpenCloudRenderSubmit.setStatusBar(self.statusbar)

        self.retranslateUi(OpenCloudRenderSubmit)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(OpenCloudRenderSubmit)

    def retranslateUi(self, OpenCloudRenderSubmit):
        OpenCloudRenderSubmit.setWindowTitle(QtGui.QApplication.translate("OpenCloudRenderSubmit", "OpenCloudRender", None, QtGui.QApplication.UnicodeUTF8))
        self.submitScenesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "submit synced scenes", None, QtGui.QApplication.UnicodeUTF8))
        self.syncAssetsButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync assets", None, QtGui.QApplication.UnicodeUTF8))
        self.addScenesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "add .vrscene/.ass files", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.dragDropOnlyLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Scenes list - just drag&drop your .vrscene .ifd .hip .ass", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "V-Ray", None, QtGui.QApplication.UnicodeUTF8))
        self.syncImagesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync rendered images", None, QtGui.QApplication.UnicodeUTF8))
        self.mantraVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Mantra", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "default versions:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.submissionTab), QtGui.QApplication.translate("OpenCloudRenderSubmit", "Submission", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoSyncButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Vray", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoPathGlobLineEdit.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/opt/vray/*", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Vray", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoPathGlobLineEdit.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/opt/hfs*", None, QtGui.QApplication.UnicodeUTF8))
        self.syncHoudiniRepoButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Houdini", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Houdini", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoPathGlobLineEdit.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/opt/arnold/*", None, QtGui.QApplication.UnicodeUTF8))
        self.syncArnoldRepoButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoExcludesLineEdit.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "docs,include,opensl,samples,scenes", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoExcludesLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Exclude directories:", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoExcludesLineEdit.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "toolkit", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoVersionComboBox.setItemText(0, QtGui.QApplication.translate("OpenCloudRenderSubmit", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoVersionComboBox.setItemText(1, QtGui.QApplication.translate("OpenCloudRenderSubmit", "scan...", None, QtGui.QApplication.UnicodeUTF8))
        self.localVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "local version", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoBrowseButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "browse", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoBrowseButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "browse", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoVersionComboBox.setItemText(0, QtGui.QApplication.translate("OpenCloudRenderSubmit", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoVersionComboBox.setItemText(1, QtGui.QApplication.translate("OpenCloudRenderSubmit", "scan...", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoBrowseButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "browse", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoVersionComboBox.setItemText(0, QtGui.QApplication.translate("OpenCloudRenderSubmit", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoVersionComboBox.setItemText(1, QtGui.QApplication.translate("OpenCloudRenderSubmit", "scan...", None, QtGui.QApplication.UnicodeUTF8))
        self.localRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "local Repo path glob", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoStripPathPrefixLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "strip path prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoStripPathPrefixLineEdit.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/opt/vray", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.repoTab), QtGui.QApplication.translate("OpenCloudRenderSubmit", "Repositories", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.dataBucketNameLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Data Bucket", None, QtGui.QApplication.UnicodeUTF8))
        self.repoBucketNameLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Repository Bucket", None, QtGui.QApplication.UnicodeUTF8))

