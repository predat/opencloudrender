# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrSubmit.ui'
#
# Created: Sat May 16 18:46:27 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OpenCloudRenderSubmit(object):
    def setupUi(self, OpenCloudRenderSubmit):
        OpenCloudRenderSubmit.setObjectName("OpenCloudRenderSubmit")
        OpenCloudRenderSubmit.resize(1370, 339)
        OpenCloudRenderSubmit.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(OpenCloudRenderSubmit)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 1370, 251))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.submissionTab = QtGui.QWidget()
        self.submissionTab.setObjectName("submissionTab")
        self.arnoldVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.arnoldVersionComboBox.setEnabled(False)
        self.arnoldVersionComboBox.setGeometry(QtCore.QRect(910, 5, 100, 21))
        self.arnoldVersionComboBox.setObjectName("arnoldVersionComboBox")
        self.vrayVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.vrayVersionComboBox.setGeometry(QtCore.QRect(740, 5, 100, 21))
        self.vrayVersionComboBox.setObjectName("vrayVersionComboBox")
        self.submitScenesButton = QtGui.QPushButton(self.submissionTab)
        self.submitScenesButton.setGeometry(QtCore.QRect(1175, 110, 170, 30))
        self.submitScenesButton.setObjectName("submitScenesButton")
        self.mantraVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.mantraVersionComboBox.setEnabled(False)
        self.mantraVersionComboBox.setGeometry(QtCore.QRect(1070, 5, 100, 21))
        self.mantraVersionComboBox.setObjectName("mantraVersionComboBox")
        self.syncAssetsButton = QtGui.QPushButton(self.submissionTab)
        self.syncAssetsButton.setGeometry(QtCore.QRect(1175, 70, 170, 30))
        self.syncAssetsButton.setObjectName("syncAssetsButton")
        self.scenesTableView = QtGui.QTableView(self.submissionTab)
        self.scenesTableView.setGeometry(QtCore.QRect(5, 30, 1160, 160))
        self.scenesTableView.setAcceptDrops(True)
        self.scenesTableView.setObjectName("scenesTableView")
        self.addScenesButton = QtGui.QPushButton(self.submissionTab)
        self.addScenesButton.setGeometry(QtCore.QRect(1175, 30, 170, 30))
        self.addScenesButton.setObjectName("addScenesButton")
        self.arnoldVersionLabel = QtGui.QLabel(self.submissionTab)
        self.arnoldVersionLabel.setEnabled(False)
        self.arnoldVersionLabel.setGeometry(QtCore.QRect(860, 5, 45, 20))
        self.arnoldVersionLabel.setObjectName("arnoldVersionLabel")
        self.dragDropOnlyLabel = QtGui.QLabel(self.submissionTab)
        self.dragDropOnlyLabel.setGeometry(QtCore.QRect(10, 5, 531, 20))
        self.dragDropOnlyLabel.setObjectName("dragDropOnlyLabel")
        self.vrayVersionLabel = QtGui.QLabel(self.submissionTab)
        self.vrayVersionLabel.setGeometry(QtCore.QRect(700, 5, 40, 20))
        self.vrayVersionLabel.setObjectName("vrayVersionLabel")
        self.syncImagesButton = QtGui.QPushButton(self.submissionTab)
        self.syncImagesButton.setGeometry(QtCore.QRect(1175, 150, 170, 30))
        self.syncImagesButton.setObjectName("syncImagesButton")
        self.mantraVersionLabel = QtGui.QLabel(self.submissionTab)
        self.mantraVersionLabel.setEnabled(False)
        self.mantraVersionLabel.setGeometry(QtCore.QRect(1020, 5, 45, 20))
        self.mantraVersionLabel.setObjectName("mantraVersionLabel")
        self.defaultVersionLabel = QtGui.QLabel(self.submissionTab)
        self.defaultVersionLabel.setEnabled(True)
        self.defaultVersionLabel.setGeometry(QtCore.QRect(560, 5, 111, 20))
        self.defaultVersionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.defaultVersionLabel.setObjectName("defaultVersionLabel")
        self.pathStartsWithsLabel = QtGui.QLabel(self.submissionTab)
        self.pathStartsWithsLabel.setGeometry(QtCore.QRect(10, 195, 141, 20))
        self.pathStartsWithsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathStartsWithsLabel.setObjectName("pathStartsWithsLabel")
        self.pathStartsWiths = QtGui.QLineEdit(self.submissionTab)
        self.pathStartsWiths.setGeometry(QtCore.QRect(160, 195, 871, 20))
        self.pathStartsWiths.setObjectName("pathStartsWiths")
        self.commaSeparatedLabel = QtGui.QLabel(self.submissionTab)
        self.commaSeparatedLabel.setGeometry(QtCore.QRect(1040, 195, 121, 20))
        self.commaSeparatedLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.commaSeparatedLabel.setObjectName("commaSeparatedLabel")
        self.clearTableButton = QtGui.QPushButton(self.submissionTab)
        self.clearTableButton.setEnabled(False)
        self.clearTableButton.setGeometry(QtCore.QRect(1175, 190, 170, 30))
        self.clearTableButton.setObjectName("clearTableButton")
        self.tabWidget.addTab(self.submissionTab, "")
        self.repoTab = QtGui.QWidget()
        self.repoTab.setObjectName("repoTab")
        self.vrayRepoSyncButton = QtGui.QPushButton(self.repoTab)
        self.vrayRepoSyncButton.setGeometry(QtCore.QRect(1175, 30, 170, 30))
        self.vrayRepoSyncButton.setObjectName("vrayRepoSyncButton")
        self.vrayRepoPathGlob = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoPathGlob.setGeometry(QtCore.QRect(100, 34, 271, 20))
        self.vrayRepoPathGlob.setObjectName("vrayRepoPathGlob")
        self.vrayRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoPathGlobLabel.setGeometry(QtCore.QRect(10, 30, 81, 30))
        self.vrayRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vrayRepoPathGlobLabel.setObjectName("vrayRepoPathGlobLabel")
        self.houdiniRepoPathGlobL = QtGui.QLineEdit(self.repoTab)
        self.houdiniRepoPathGlobL.setEnabled(False)
        self.houdiniRepoPathGlobL.setGeometry(QtCore.QRect(100, 74, 271, 20))
        self.houdiniRepoPathGlobL.setObjectName("houdiniRepoPathGlobL")
        self.syncHoudiniRepoButton = QtGui.QPushButton(self.repoTab)
        self.syncHoudiniRepoButton.setEnabled(False)
        self.syncHoudiniRepoButton.setGeometry(QtCore.QRect(1175, 70, 170, 30))
        self.syncHoudiniRepoButton.setObjectName("syncHoudiniRepoButton")
        self.houdiniRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.houdiniRepoPathGlobLabel.setEnabled(False)
        self.houdiniRepoPathGlobLabel.setGeometry(QtCore.QRect(10, 70, 81, 30))
        self.houdiniRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.houdiniRepoPathGlobLabel.setObjectName("houdiniRepoPathGlobLabel")
        self.arnoldRepoPathGlob = QtGui.QLineEdit(self.repoTab)
        self.arnoldRepoPathGlob.setEnabled(False)
        self.arnoldRepoPathGlob.setGeometry(QtCore.QRect(100, 114, 271, 20))
        self.arnoldRepoPathGlob.setObjectName("arnoldRepoPathGlob")
        self.syncArnoldRepoButton = QtGui.QPushButton(self.repoTab)
        self.syncArnoldRepoButton.setEnabled(False)
        self.syncArnoldRepoButton.setGeometry(QtCore.QRect(1175, 110, 170, 30))
        self.syncArnoldRepoButton.setObjectName("syncArnoldRepoButton")
        self.arnoldRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.arnoldRepoPathGlobLabel.setEnabled(False)
        self.arnoldRepoPathGlobLabel.setGeometry(QtCore.QRect(10, 110, 81, 30))
        self.arnoldRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.arnoldRepoPathGlobLabel.setObjectName("arnoldRepoPathGlobLabel")
        self.vrayRepoExcludes = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoExcludes.setGeometry(QtCore.QRect(850, 34, 315, 20))
        self.vrayRepoExcludes.setObjectName("vrayRepoExcludes")
        self.vrayRepoExcludesLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoExcludesLabel.setGeometry(QtCore.QRect(850, 5, 241, 20))
        self.vrayRepoExcludesLabel.setObjectName("vrayRepoExcludesLabel")
        self.houdiniRepoExcludes = QtGui.QLineEdit(self.repoTab)
        self.houdiniRepoExcludes.setGeometry(QtCore.QRect(850, 74, 315, 20))
        self.houdiniRepoExcludes.setObjectName("houdiniRepoExcludes")
        self.arnoldRepoExcludes = QtGui.QLineEdit(self.repoTab)
        self.arnoldRepoExcludes.setGeometry(QtCore.QRect(850, 114, 315, 20))
        self.arnoldRepoExcludes.setText("")
        self.arnoldRepoExcludes.setObjectName("arnoldRepoExcludes")
        self.vrayRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.vrayRepoVersionComboBox.setGeometry(QtCore.QRect(740, 34, 100, 21))
        self.vrayRepoVersionComboBox.setObjectName("vrayRepoVersionComboBox")
        self.vrayRepoVersionComboBox.addItem("")
        self.vrayRepoVersionComboBox.addItem("")
        self.localVersionLabel = QtGui.QLabel(self.repoTab)
        self.localVersionLabel.setGeometry(QtCore.QRect(740, 5, 100, 20))
        self.localVersionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.localVersionLabel.setObjectName("localVersionLabel")
        self.vrayRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.vrayRepoBrowseButton.setGeometry(QtCore.QRect(380, 30, 70, 30))
        self.vrayRepoBrowseButton.setObjectName("vrayRepoBrowseButton")
        self.houdiniRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.houdiniRepoBrowseButton.setEnabled(False)
        self.houdiniRepoBrowseButton.setGeometry(QtCore.QRect(380, 70, 70, 30))
        self.houdiniRepoBrowseButton.setObjectName("houdiniRepoBrowseButton")
        self.houdiniRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.houdiniRepoVersionComboBox.setEnabled(False)
        self.houdiniRepoVersionComboBox.setGeometry(QtCore.QRect(740, 74, 100, 21))
        self.houdiniRepoVersionComboBox.setObjectName("houdiniRepoVersionComboBox")
        self.houdiniRepoVersionComboBox.addItem("")
        self.houdiniRepoVersionComboBox.addItem("")
        self.arnoldRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.arnoldRepoBrowseButton.setEnabled(False)
        self.arnoldRepoBrowseButton.setGeometry(QtCore.QRect(380, 110, 70, 30))
        self.arnoldRepoBrowseButton.setObjectName("arnoldRepoBrowseButton")
        self.arnoldRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.arnoldRepoVersionComboBox.setEnabled(False)
        self.arnoldRepoVersionComboBox.setGeometry(QtCore.QRect(740, 114, 100, 21))
        self.arnoldRepoVersionComboBox.setObjectName("arnoldRepoVersionComboBox")
        self.arnoldRepoVersionComboBox.addItem("")
        self.arnoldRepoVersionComboBox.addItem("")
        self.localRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.localRepoPathGlobLabel.setGeometry(QtCore.QRect(100, 5, 231, 20))
        self.localRepoPathGlobLabel.setObjectName("localRepoPathGlobLabel")
        self.vrayRepoStripPathPrefixLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoStripPathPrefixLabel.setGeometry(QtCore.QRect(500, 5, 181, 20))
        self.vrayRepoStripPathPrefixLabel.setObjectName("vrayRepoStripPathPrefixLabel")
        self.vrayRepoStripPathPrefix = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoStripPathPrefix.setGeometry(QtCore.QRect(460, 34, 271, 20))
        self.vrayRepoStripPathPrefix.setText("")
        self.vrayRepoStripPathPrefix.setObjectName("vrayRepoStripPathPrefix")
        self.houdiniRepoStripPathPrefix = QtGui.QLineEdit(self.repoTab)
        self.houdiniRepoStripPathPrefix.setGeometry(QtCore.QRect(460, 74, 271, 20))
        self.houdiniRepoStripPathPrefix.setText("")
        self.houdiniRepoStripPathPrefix.setObjectName("houdiniRepoStripPathPrefix")
        self.arnoldRepoStripPathPrefix = QtGui.QLineEdit(self.repoTab)
        self.arnoldRepoStripPathPrefix.setGeometry(QtCore.QRect(460, 114, 271, 20))
        self.arnoldRepoStripPathPrefix.setText("")
        self.arnoldRepoStripPathPrefix.setObjectName("arnoldRepoStripPathPrefix")
        self.tabWidget.addTab(self.repoTab, "")
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setEnabled(False)
        self.cancelButton.setGeometry(QtCore.QRect(1175, 290, 170, 25))
        self.cancelButton.setObjectName("cancelButton")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(5, 295, 1161, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.dataBucketNameLabel = QtGui.QLabel(self.centralwidget)
        self.dataBucketNameLabel.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.dataBucketNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dataBucketNameLabel.setObjectName("dataBucketNameLabel")
        self.dataBucketName = QtGui.QLineEdit(self.centralwidget)
        self.dataBucketName.setGeometry(QtCore.QRect(140, 10, 530, 20))
        self.dataBucketName.setObjectName("dataBucketName")
        self.repoBucketName = QtGui.QLineEdit(self.centralwidget)
        self.repoBucketName.setEnabled(True)
        self.repoBucketName.setGeometry(QtCore.QRect(835, 10, 521, 20))
        self.repoBucketName.setObjectName("repoBucketName")
        self.repoBucketCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.repoBucketCheckBox.setGeometry(QtCore.QRect(690, 10, 140, 20))
        self.repoBucketCheckBox.setObjectName("repoBucketCheckBox")
        OpenCloudRenderSubmit.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(OpenCloudRenderSubmit)
        self.statusbar.setObjectName("statusbar")
        OpenCloudRenderSubmit.setStatusBar(self.statusbar)

        self.retranslateUi(OpenCloudRenderSubmit)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.repoBucketCheckBox, QtCore.SIGNAL("toggled(bool)"), self.repoBucketName.setEnabled)
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
        self.pathStartsWithsLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "paths must start with:", None, QtGui.QApplication.UnicodeUTF8))
        self.pathStartsWiths.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/localhost,/Users,/home", None, QtGui.QApplication.UnicodeUTF8))
        self.commaSeparatedLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "(comma separated)", None, QtGui.QApplication.UnicodeUTF8))
        self.clearTableButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "clear table", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.submissionTab), QtGui.QApplication.translate("OpenCloudRenderSubmit", "Submission", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoSyncButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Vray", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoPathGlob.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/localhost/opt/vray/*", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Vray", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoPathGlobL.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/localhost/opt/hfs*", None, QtGui.QApplication.UnicodeUTF8))
        self.syncHoudiniRepoButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Houdini", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Houdini", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoPathGlob.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/localhost/opt/arnold/*", None, QtGui.QApplication.UnicodeUTF8))
        self.syncArnoldRepoButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoExcludes.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "docs,include,opensl,samples,scenes", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoExcludesLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Exclude directories:", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoExcludes.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "toolkit", None, QtGui.QApplication.UnicodeUTF8))
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
        self.localRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Local Linux Repository paths (glob)", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoStripPathPrefixLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "strip path prefix - optional", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.repoTab), QtGui.QApplication.translate("OpenCloudRenderSubmit", "Repositories", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.dataBucketNameLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Data Bucket", None, QtGui.QApplication.UnicodeUTF8))
        self.repoBucketName.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "optional", None, QtGui.QApplication.UnicodeUTF8))
        self.repoBucketCheckBox.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Repository Bucket", None, QtGui.QApplication.UnicodeUTF8))

