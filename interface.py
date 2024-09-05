# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacefGyqkG.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSlider, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(631, 448)
        MainWindow.setStyleSheet(u"border: none;")
        self.actionNew_tab = QAction(MainWindow)
        self.actionNew_tab.setObjectName(u"actionNew_tab")
        self.actionNew_window = QAction(MainWindow)
        self.actionNew_window.setObjectName(u"actionNew_window")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionClose_window = QAction(MainWindow)
        self.actionClose_window.setObjectName(u"actionClose_window")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainbody = QFrame(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        self.mainbody.setStyleSheet(u"")
        self.mainbody.setFrameShape(QFrame.StyledPanel)
        self.mainbody.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainbody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.mainbody)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color:#2F363D;\n"
"color:white;")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 2, 3, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/icons/music-player-cinema-svgrepo-com (1).svg"))

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_7.addWidget(self.frame)

        self.frame_8 = QFrame(self.header)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolButton_4 = QToolButton(self.frame_8)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setStyleSheet(u"QToolButton:hover {\n"
"	border:none;\n"
"    border-radius:10%;\n"
"    background-color: rgba(255, 255, 255, 0.426);\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.toolButton_4)

        self.toolButton_3 = QToolButton(self.frame_8)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setStyleSheet(u"QToolButton:hover {\n"
"	border:none;\n"
"    border-radius:10%;\n"
"    background-color: rgba(255, 255, 255, 0.426);\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.toolButton_3)

        self.toolButton_2 = QToolButton(self.frame_8)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setStyleSheet(u"QToolButton:hover {\n"
"	border:none;\n"
"    border-radius:10%;\n"
"    background-color: rgba(255, 255, 255, 0.426);\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.toolButton_2)


        self.horizontalLayout_7.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.centerbody = QFrame(self.mainbody)
        self.centerbody.setObjectName(u"centerbody")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerbody.sizePolicy().hasHeightForWidth())
        self.centerbody.setSizePolicy(sizePolicy)
        self.centerbody.setStyleSheet(u"background-color:#24292E;\n"
"color:white;")
        self.centerbody.setFrameShape(QFrame.StyledPanel)
        self.centerbody.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.centerbody)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.centerbody)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/icons/icons/music-player-cinema-svgrepo-com - Copy.svg"))

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_5 = QLabel(self.centerbody)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Bauhaus 93"])
        font1.setPointSize(40)
        font1.setBold(False)
        self.label_5.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_6 = QLabel(self.centerbody)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(8)
        self.label_6.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout.addWidget(self.centerbody)

        self.controlbody = QFrame(self.mainbody)
        self.controlbody.setObjectName(u"controlbody")
        self.controlbody.setStyleSheet(u"border: none;\n"
"background-color:#2F363D;\n"
"color:white;")
        self.controlbody.setFrameShape(QFrame.StyledPanel)
        self.controlbody.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.controlbody)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.controlbody)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSlider_2trim = QSlider(self.frame_5)
        self.horizontalSlider_2trim.setObjectName(u"horizontalSlider_2trim")
        self.horizontalSlider_2trim.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider_2trim)

        self.labeltimer = QLabel(self.frame_5)
        self.labeltimer.setObjectName(u"labeltimer")
        self.labeltimer.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.horizontalLayout_3.addWidget(self.labeltimer)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.frame_4 = QFrame(self.controlbody)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.play = QToolButton(self.frame_4)
        self.play.setObjectName(u"play")
        self.play.setStyleSheet(u"QToolButton:hover {\n"
"    border-radius: 5%;\n"
"    background-color: rgba(255, 255, 255, 0.426);\n"
"\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.play.setIcon(icon3)
        self.play.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.play, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pause = QToolButton(self.frame_4)
        self.pause.setObjectName(u"pause")
        self.pause.setStyleSheet(u"QToolButton:hover {\n"
"    border-radius: 5%;\n"
"    background-color: rgba(255, 255, 255, 0.426);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/pause.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pause.setIcon(icon4)
        self.pause.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pause, 0, Qt.AlignBottom)

        self.stop = QToolButton(self.frame_4)
        self.stop.setObjectName(u"stop")
        self.stop.setStyleSheet(u"QToolButton:hover {\n"
"    border-radius: 5%;\n"
"    background-color: rgba(255, 255, 255, 0.426);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stop.setIcon(icon5)
        self.stop.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.stop, 0, Qt.AlignBottom)

        self.openfile = QToolButton(self.frame_4)
        self.openfile.setObjectName(u"openfile")
        self.openfile.setStyleSheet(u"QToolButton:hover {\n"
"    border-radius: 5%;\n"
"    background-color: rgba(255, 255, 255, 0.426);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openfile.setIcon(icon6)
        self.openfile.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.openfile, 0, Qt.AlignBottom)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.volume = QToolButton(self.frame_4)
        self.volume.setObjectName(u"volume")
        self.volume.setStyleSheet(u"QToolButton:hover {\n"
"    border-radius: 5%;\n"
"    background-color: rgba(255, 255, 255, 0.426);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/volume-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.volume.setIcon(icon7)
        self.volume.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.volume, 0, Qt.AlignBottom)

        self.horizontalSlidervolume = QSlider(self.frame_4)
        self.horizontalSlidervolume.setObjectName(u"horizontalSlidervolume")
        self.horizontalSlidervolume.setMinimumSize(QSize(60, 0))
        self.horizontalSlidervolume.setMaximumSize(QSize(60, 16777215))
        self.horizontalSlidervolume.setAcceptDrops(False)
        self.horizontalSlidervolume.setMaximum(10)
        self.horizontalSlidervolume.setTracking(True)
        self.horizontalSlidervolume.setOrientation(Qt.Horizontal)
        self.horizontalSlidervolume.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_2.addWidget(self.horizontalSlidervolume)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.frame_6 = QFrame(self.controlbody)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sizegrip = QFrame(self.frame_6)
        self.sizegrip.setObjectName(u"sizegrip")
        self.sizegrip.setMinimumSize(QSize(10, 10))
        self.sizegrip.setMaximumSize(QSize(10, 10))
        self.sizegrip.setFrameShape(QFrame.StyledPanel)
        self.sizegrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sizegrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_6, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.controlbody, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_tab.setText(QCoreApplication.translate("MainWindow", u"New tab", None))
        self.actionNew_window.setText(QCoreApplication.translate("MainWindow", u"New window", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionClose_window.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SonicSphere", None))
#if QT_CONFIG(tooltip)
        self.toolButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_4.setText("")
        self.toolButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_2.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SonicSphere", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Powered by - G. A. Pasindu Vidunitha", None))
        self.label_7.setText("")
        self.labeltimer.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
#if QT_CONFIG(tooltip)
        self.play.setToolTip(QCoreApplication.translate("MainWindow", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.play.setText("")
#if QT_CONFIG(shortcut)
        self.play.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pause.setToolTip(QCoreApplication.translate("MainWindow", u"Pause", None))
#endif // QT_CONFIG(tooltip)
        self.pause.setText("")
#if QT_CONFIG(shortcut)
        self.pause.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.stop.setToolTip(QCoreApplication.translate("MainWindow", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.stop.setText("")
#if QT_CONFIG(tooltip)
        self.openfile.setToolTip(QCoreApplication.translate("MainWindow", u"Open File", None))
#endif // QT_CONFIG(tooltip)
        self.openfile.setText("")
#if QT_CONFIG(tooltip)
        self.volume.setToolTip(QCoreApplication.translate("MainWindow", u"Volume", None))
#endif // QT_CONFIG(tooltip)
        self.volume.setText("")
#if QT_CONFIG(shortcut)
        self.volume.setShortcut(QCoreApplication.translate("MainWindow", u"Volume Up, Volume Down, Volume Mute", None))
#endif // QT_CONFIG(shortcut)
        self.label_8.setText("")
    # retranslateUi

