# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrSubmit.ui'
#
# Created: Tue May 26 11:28:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OpenCloudRenderSubmit(object):
    def setupUi(self, OpenCloudRenderSubmit):
        OpenCloudRenderSubmit.setObjectName("OpenCloudRenderSubmit")
        OpenCloudRenderSubmit.resize(992, 466)
        OpenCloudRenderSubmit.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(OpenCloudRenderSubmit)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dataBucketNameLabel = QtGui.QLabel(self.centralwidget)
        self.dataBucketNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dataBucketNameLabel.setObjectName("dataBucketNameLabel")
        self.horizontalLayout.addWidget(self.dataBucketNameLabel)
        self.dataBucketName = QtGui.QLineEdit(self.centralwidget)
        self.dataBucketName.setObjectName("dataBucketName")
        self.horizontalLayout.addWidget(self.dataBucketName)
        self.repoBucketCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.repoBucketCheckBox.setObjectName("repoBucketCheckBox")
        self.horizontalLayout.addWidget(self.repoBucketCheckBox)
        self.repoBucketName = QtGui.QLineEdit(self.centralwidget)
        self.repoBucketName.setEnabled(True)
        self.repoBucketName.setObjectName("repoBucketName")
        self.horizontalLayout.addWidget(self.repoBucketName)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.submissionTab = QtGui.QWidget()
        self.submissionTab.setObjectName("submissionTab")
        self.gridLayout = QtGui.QGridLayout(self.submissionTab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dragDropOnlyLabel = QtGui.QLabel(self.submissionTab)
        self.dragDropOnlyLabel.setObjectName("dragDropOnlyLabel")
        self.horizontalLayout_3.addWidget(self.dragDropOnlyLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.defaultVersionLabel = QtGui.QLabel(self.submissionTab)
        self.defaultVersionLabel.setEnabled(True)
        self.defaultVersionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.defaultVersionLabel.setObjectName("defaultVersionLabel")
        self.horizontalLayout_3.addWidget(self.defaultVersionLabel)
        self.vrayVersionLabel = QtGui.QLabel(self.submissionTab)
        self.vrayVersionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.vrayVersionLabel.setObjectName("vrayVersionLabel")
        self.horizontalLayout_3.addWidget(self.vrayVersionLabel)
        self.vrayVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.vrayVersionComboBox.setObjectName("vrayVersionComboBox")
        self.horizontalLayout_3.addWidget(self.vrayVersionComboBox)
        self.arnoldVersionLabel = QtGui.QLabel(self.submissionTab)
        self.arnoldVersionLabel.setEnabled(False)
        self.arnoldVersionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.arnoldVersionLabel.setObjectName("arnoldVersionLabel")
        self.horizontalLayout_3.addWidget(self.arnoldVersionLabel)
        self.arnoldVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.arnoldVersionComboBox.setEnabled(False)
        self.arnoldVersionComboBox.setObjectName("arnoldVersionComboBox")
        self.horizontalLayout_3.addWidget(self.arnoldVersionComboBox)
        self.mantraVersionLabel = QtGui.QLabel(self.submissionTab)
        self.mantraVersionLabel.setEnabled(False)
        self.mantraVersionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mantraVersionLabel.setObjectName("mantraVersionLabel")
        self.horizontalLayout_3.addWidget(self.mantraVersionLabel)
        self.mantraVersionComboBox = QtGui.QComboBox(self.submissionTab)
        self.mantraVersionComboBox.setEnabled(False)
        self.mantraVersionComboBox.setObjectName("mantraVersionComboBox")
        self.horizontalLayout_3.addWidget(self.mantraVersionComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.scenesTableView = QtGui.QTableView(self.submissionTab)
        self.scenesTableView.setAcceptDrops(True)
        self.scenesTableView.setObjectName("scenesTableView")
        self.gridLayout.addWidget(self.scenesTableView, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addScenesButton = QtGui.QPushButton(self.submissionTab)
        self.addScenesButton.setObjectName("addScenesButton")
        self.verticalLayout.addWidget(self.addScenesButton)
        self.syncAssetsButton = QtGui.QPushButton(self.submissionTab)
        self.syncAssetsButton.setObjectName("syncAssetsButton")
        self.verticalLayout.addWidget(self.syncAssetsButton)
        self.submitScenesButton = QtGui.QPushButton(self.submissionTab)
        self.submitScenesButton.setObjectName("submitScenesButton")
        self.verticalLayout.addWidget(self.submitScenesButton)
        self.syncImagesButton = QtGui.QPushButton(self.submissionTab)
        self.syncImagesButton.setObjectName("syncImagesButton")
        self.verticalLayout.addWidget(self.syncImagesButton)
        self.clearTableButton = QtGui.QPushButton(self.submissionTab)
        self.clearTableButton.setEnabled(False)
        self.clearTableButton.setObjectName("clearTableButton")
        self.verticalLayout.addWidget(self.clearTableButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 2, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pathStartsWithsLabel = QtGui.QLabel(self.submissionTab)
        self.pathStartsWithsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pathStartsWithsLabel.setObjectName("pathStartsWithsLabel")
        self.horizontalLayout_4.addWidget(self.pathStartsWithsLabel)
        self.pathStartsWiths = QtGui.QLineEdit(self.submissionTab)
        self.pathStartsWiths.setObjectName("pathStartsWiths")
        self.horizontalLayout_4.addWidget(self.pathStartsWiths)
        self.commaSeparatedLabel = QtGui.QLabel(self.submissionTab)
        self.commaSeparatedLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.commaSeparatedLabel.setObjectName("commaSeparatedLabel")
        self.horizontalLayout_4.addWidget(self.commaSeparatedLabel)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.submissionTab, "")
        self.repoTab = QtGui.QWidget()
        self.repoTab.setObjectName("repoTab")
        self.gridLayout_3 = QtGui.QGridLayout(self.repoTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.arnoldRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.arnoldRepoVersionComboBox.setEnabled(False)
        self.arnoldRepoVersionComboBox.setObjectName("arnoldRepoVersionComboBox")
        self.arnoldRepoVersionComboBox.addItem("")
        self.arnoldRepoVersionComboBox.addItem("")
        self.gridLayout_2.addWidget(self.arnoldRepoVersionComboBox, 3, 5, 1, 1)
        self.arnoldRepoPathGlob = QtGui.QLineEdit(self.repoTab)
        self.arnoldRepoPathGlob.setEnabled(False)
        self.arnoldRepoPathGlob.setObjectName("arnoldRepoPathGlob")
        self.gridLayout_2.addWidget(self.arnoldRepoPathGlob, 3, 1, 1, 1)
        self.arnoldRepoExcludes = QtGui.QLineEdit(self.repoTab)
        self.arnoldRepoExcludes.setText("")
        self.arnoldRepoExcludes.setObjectName("arnoldRepoExcludes")
        self.gridLayout_2.addWidget(self.arnoldRepoExcludes, 3, 6, 1, 1)
        self.vrayRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.vrayRepoBrowseButton.setObjectName("vrayRepoBrowseButton")
        self.gridLayout_2.addWidget(self.vrayRepoBrowseButton, 1, 2, 1, 1)
        self.houdiniRepoStripPathPrefix = QtGui.QLineEdit(self.repoTab)
        self.houdiniRepoStripPathPrefix.setText("")
        self.houdiniRepoStripPathPrefix.setObjectName("houdiniRepoStripPathPrefix")
        self.gridLayout_2.addWidget(self.houdiniRepoStripPathPrefix, 2, 4, 1, 1)
        self.syncHoudiniRepoButton = QtGui.QPushButton(self.repoTab)
        self.syncHoudiniRepoButton.setEnabled(False)
        self.syncHoudiniRepoButton.setObjectName("syncHoudiniRepoButton")
        self.gridLayout_2.addWidget(self.syncHoudiniRepoButton, 2, 7, 1, 1)
        self.vrayRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vrayRepoPathGlobLabel.setObjectName("vrayRepoPathGlobLabel")
        self.gridLayout_2.addWidget(self.vrayRepoPathGlobLabel, 1, 0, 1, 1)
        self.houdiniRepoExcludes = QtGui.QLineEdit(self.repoTab)
        self.houdiniRepoExcludes.setObjectName("houdiniRepoExcludes")
        self.gridLayout_2.addWidget(self.houdiniRepoExcludes, 2, 6, 1, 1)
        self.syncArnoldRepoButton = QtGui.QPushButton(self.repoTab)
        self.syncArnoldRepoButton.setEnabled(False)
        self.syncArnoldRepoButton.setObjectName("syncArnoldRepoButton")
        self.gridLayout_2.addWidget(self.syncArnoldRepoButton, 3, 7, 1, 1)
        self.houdiniRepoPathGlobL = QtGui.QLineEdit(self.repoTab)
        self.houdiniRepoPathGlobL.setEnabled(False)
        self.houdiniRepoPathGlobL.setObjectName("houdiniRepoPathGlobL")
        self.gridLayout_2.addWidget(self.houdiniRepoPathGlobL, 2, 1, 1, 1)
        self.houdiniRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.houdiniRepoPathGlobLabel.setEnabled(False)
        self.houdiniRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.houdiniRepoPathGlobLabel.setObjectName("houdiniRepoPathGlobLabel")
        self.gridLayout_2.addWidget(self.houdiniRepoPathGlobLabel, 2, 0, 1, 1)
        self.vrayInstallButton = QtGui.QPushButton(self.repoTab)
        self.vrayInstallButton.setObjectName("vrayInstallButton")
        self.gridLayout_2.addWidget(self.vrayInstallButton, 1, 3, 1, 1)
        self.vrayRepoStripPathPrefix = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoStripPathPrefix.setText("")
        self.vrayRepoStripPathPrefix.setObjectName("vrayRepoStripPathPrefix")
        self.gridLayout_2.addWidget(self.vrayRepoStripPathPrefix, 1, 4, 1, 1)
        self.vrayRepoExcludes = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoExcludes.setObjectName("vrayRepoExcludes")
        self.gridLayout_2.addWidget(self.vrayRepoExcludes, 1, 6, 1, 1)
        self.houdiniRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.houdiniRepoVersionComboBox.setEnabled(False)
        self.houdiniRepoVersionComboBox.setObjectName("houdiniRepoVersionComboBox")
        self.houdiniRepoVersionComboBox.addItem("")
        self.houdiniRepoVersionComboBox.addItem("")
        self.gridLayout_2.addWidget(self.houdiniRepoVersionComboBox, 2, 5, 1, 1)
        self.houdiniRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.houdiniRepoBrowseButton.setEnabled(False)
        self.houdiniRepoBrowseButton.setObjectName("houdiniRepoBrowseButton")
        self.gridLayout_2.addWidget(self.houdiniRepoBrowseButton, 2, 2, 1, 1)
        self.arnoldRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.arnoldRepoPathGlobLabel.setEnabled(False)
        self.arnoldRepoPathGlobLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.arnoldRepoPathGlobLabel.setObjectName("arnoldRepoPathGlobLabel")
        self.gridLayout_2.addWidget(self.arnoldRepoPathGlobLabel, 3, 0, 1, 1)
        self.vrayRepoSyncButton = QtGui.QPushButton(self.repoTab)
        self.vrayRepoSyncButton.setObjectName("vrayRepoSyncButton")
        self.gridLayout_2.addWidget(self.vrayRepoSyncButton, 1, 7, 1, 1)
        self.vrayRepoVersionComboBox = QtGui.QComboBox(self.repoTab)
        self.vrayRepoVersionComboBox.setObjectName("vrayRepoVersionComboBox")
        self.vrayRepoVersionComboBox.addItem("")
        self.vrayRepoVersionComboBox.addItem("")
        self.gridLayout_2.addWidget(self.vrayRepoVersionComboBox, 1, 5, 1, 1)
        self.arnoldRepoBrowseButton = QtGui.QPushButton(self.repoTab)
        self.arnoldRepoBrowseButton.setEnabled(False)
        self.arnoldRepoBrowseButton.setObjectName("arnoldRepoBrowseButton")
        self.gridLayout_2.addWidget(self.arnoldRepoBrowseButton, 3, 2, 1, 1)
        self.arnoldRepoStripPathPrefix = QtGui.QLineEdit(self.repoTab)
        self.arnoldRepoStripPathPrefix.setText("")
        self.arnoldRepoStripPathPrefix.setObjectName("arnoldRepoStripPathPrefix")
        self.gridLayout_2.addWidget(self.arnoldRepoStripPathPrefix, 3, 4, 1, 1)
        self.vrayRepoPathGlob = QtGui.QLineEdit(self.repoTab)
        self.vrayRepoPathGlob.setObjectName("vrayRepoPathGlob")
        self.gridLayout_2.addWidget(self.vrayRepoPathGlob, 1, 1, 1, 1)
        self.localRepoPathGlobLabel = QtGui.QLabel(self.repoTab)
        self.localRepoPathGlobLabel.setObjectName("localRepoPathGlobLabel")
        self.gridLayout_2.addWidget(self.localRepoPathGlobLabel, 0, 1, 1, 1)
        self.vrayRepoStripPathPrefixLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoStripPathPrefixLabel.setObjectName("vrayRepoStripPathPrefixLabel")
        self.gridLayout_2.addWidget(self.vrayRepoStripPathPrefixLabel, 0, 4, 1, 1)
        self.localVersionLabel = QtGui.QLabel(self.repoTab)
        self.localVersionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.localVersionLabel.setObjectName("localVersionLabel")
        self.gridLayout_2.addWidget(self.localVersionLabel, 0, 5, 1, 1)
        self.vrayRepoExcludesLabel = QtGui.QLabel(self.repoTab)
        self.vrayRepoExcludesLabel.setObjectName("vrayRepoExcludesLabel")
        self.gridLayout_2.addWidget(self.vrayRepoExcludesLabel, 0, 6, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 135, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.repoTab, "")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setEnabled(False)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
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
        self.dataBucketNameLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Data Bucket", None, QtGui.QApplication.UnicodeUTF8))
        self.repoBucketCheckBox.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Repository Bucket", None, QtGui.QApplication.UnicodeUTF8))
        self.repoBucketName.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "optional", None, QtGui.QApplication.UnicodeUTF8))
        self.dragDropOnlyLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Scenes list - just drag&drop your .vrscene .ifd .hip .ass", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "default versions:", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "V-Ray", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.mantraVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Mantra", None, QtGui.QApplication.UnicodeUTF8))
        self.addScenesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "add .vrscene/.ass files", None, QtGui.QApplication.UnicodeUTF8))
        self.syncAssetsButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync assets", None, QtGui.QApplication.UnicodeUTF8))
        self.submitScenesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "submit synced scenes", None, QtGui.QApplication.UnicodeUTF8))
        self.syncImagesButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync rendered images", None, QtGui.QApplication.UnicodeUTF8))
        self.clearTableButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "clear table", None, QtGui.QApplication.UnicodeUTF8))
        self.pathStartsWithsLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "paths must start with:", None, QtGui.QApplication.UnicodeUTF8))
        self.pathStartsWiths.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/localhost,/Users,/home", None, QtGui.QApplication.UnicodeUTF8))
        self.commaSeparatedLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "(comma separated)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.submissionTab), QtGui.QApplication.translate("OpenCloudRenderSubmit", "Submission", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoVersionComboBox.setItemText(0, QtGui.QApplication.translate("OpenCloudRenderSubmit", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoVersionComboBox.setItemText(1, QtGui.QApplication.translate("OpenCloudRenderSubmit", "scan...", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoPathGlob.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/localhost/opt/arnold/*", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoBrowseButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "browse", None, QtGui.QApplication.UnicodeUTF8))
        self.syncHoudiniRepoButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Houdini", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Vray", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoExcludes.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "toolkit", None, QtGui.QApplication.UnicodeUTF8))
        self.syncArnoldRepoButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoPathGlobL.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/localhost/opt/hfs*", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Houdini", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayInstallButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "install", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoExcludes.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "docs,include,opensl,samples,scenes", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoVersionComboBox.setItemText(0, QtGui.QApplication.translate("OpenCloudRenderSubmit", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoVersionComboBox.setItemText(1, QtGui.QApplication.translate("OpenCloudRenderSubmit", "scan...", None, QtGui.QApplication.UnicodeUTF8))
        self.houdiniRepoBrowseButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "browse", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoSyncButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "sync Vray", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoVersionComboBox.setItemText(0, QtGui.QApplication.translate("OpenCloudRenderSubmit", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoVersionComboBox.setItemText(1, QtGui.QApplication.translate("OpenCloudRenderSubmit", "scan...", None, QtGui.QApplication.UnicodeUTF8))
        self.arnoldRepoBrowseButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "browse", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoPathGlob.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "/localhost/opt/vray/*", None, QtGui.QApplication.UnicodeUTF8))
        self.localRepoPathGlobLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Local Linux Repository paths (glob)", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoStripPathPrefixLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "strip path prefix - optional", None, QtGui.QApplication.UnicodeUTF8))
        self.localVersionLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "local version", None, QtGui.QApplication.UnicodeUTF8))
        self.vrayRepoExcludesLabel.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "Exclude directories:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.repoTab), QtGui.QApplication.translate("OpenCloudRenderSubmit", "Repositories", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("OpenCloudRenderSubmit", "cancel", None, QtGui.QApplication.UnicodeUTF8))

