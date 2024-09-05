import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip, QFileDialog
from PySide6.QtGui import QColor, QMouseEvent, Qt, QIcon
from PySide6 import QtCore,QtGui
from PySide6.QtCore import QPropertyAnimation, QUrl, QTime
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from interface import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.muted = True
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)  # Fix typo: setblurRadius -> setBlurRadius
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))  # Fix typo: Setcolor -> setColor
        self.ui.centralwidget.setGraphicsEffect(self.shadow)  
        QSizeGrip(self.ui.sizegrip)
        self.ui.toolButton_4.clicked.connect(lambda: self.showMinimized())
        self.ui.toolButton_3.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.toolButton_2.clicked.connect(lambda: self.close())

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(self.ui.horizontalSlidervolume.value())

        self.ui.play.setEnabled(False)
        self.ui.pause.setEnabled(False)
        self.ui.stop.setEnabled(False)
        self.ui.volume.setEnabled(False)
        self.ui.horizontalSlidervolume.setEnabled(False)
        self.ui.horizontalSlider_2trim.setEnabled(False)

        self.ui.play.clicked.connect(lambda:self.music_player())
        self.ui.pause.clicked.connect(lambda:self.pausemusic())
        self.ui.stop.clicked.connect(lambda:self.player.stop())
        self.ui.openfile.clicked.connect(lambda:self.open_file())
        self.player.positionChanged.connect(self.position)
        self.ui.horizontalSlidervolume.sliderMoved.connect(self.volume)
        self.ui.volume.clicked.connect(self.volume_muted)

        
        def moveWindow(e):
            if self.isMaximized()==False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos()+e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.header.mouseMoveEvent = moveWindow
        self.show()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Music")

        if filename != '':
            self.player.setSource(QUrl.fromLocalFile(filename))
            self.ui.play.setEnabled(True)
            self.ui.pause.setEnabled(True)
            self.ui.stop.setEnabled(True)
            self.ui.volume.setEnabled(True)
            self.ui.horizontalSlidervolume.setEnabled(True)
            self.ui.horizontalSlider_2trim.setEnabled(True)

    def music_player(self):
        if self.player.mediaStatus == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()
            self.ui.play.setEnabled(False)
            self.ui.pause.setEnabled(True)
    
    def position(self, position):
        if(self.ui.horizontalSlider_2trim.maximum() != self.player.duration()):
            self.ui.horizontalSlider_2trim.setMaximum(self.player.duration())

        self.ui.horizontalSlider_2trim.setValue(position)

        seconds = (position/1000) % 60
        minutes = (position/60000) % 60
        hours = (position/2600000) % 24

        time = QTime(hours, minutes, seconds)
        self.ui.labeltimer.setText(time.toString())

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def volume(self, position):
        self.audio.setVolume(position)

    def pausemusic(self):
        self.player.pause()
        self.ui.pause.setEnabled(False)
        self.ui.play.setEnabled(True)



    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.toolButton_3.setIcon(QtGui.QIcon(u":/icons/icons/maximize.svg"))
        else:
            self.showMaximized()
            self.ui.toolButton_3.setIcon(QtGui.QIcon(u":/icons/icons/minimize.svg"))


    def volume_muted(self):
        if(self.muted):
            self.audio.setMuted(True)
            self.ui.horizontalSlidervolume.setValue(0)
            self.ui.volume.setIcon(QtGui.QIcon(u":/icons/icons/volume-x.svg"))
            self.muted = False
        else:
            self.audio.setMuted(False)
            self.ui.horizontalSlidervolume.setValue(50)
            self.ui.volume.setIcon(QtGui.QIcon(u":/icons/icons/volume-2.svg"))
            self.muted = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon('D:\Python_works\Desktop Application\desktop application 3\icon.ico'))
    sys.exit(app.exec())
