import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from moviepy.editor import AudioFileClip


transcribed_audio_file_name = "transcribed_speech.wav"
zoom_video_file_name = "zoom_0.mp4"

audioclip = AudioFileClip(zoom_video_file_name)
audioclip.write_audiofile(transcribed_audio_file_name)

with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    
total_duration = math.ceil(duration / 60)

r = sr.Recognizer()


for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open("transcription.txt", "a")
    f.write(r.recognize_google(audio))
    f.write(" ")
f.close()

with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
total_duration = math.ceil(duration / 60)
r = sr.Recognizer()
for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open("transcription.txt", "a")
    f.write(r.recognize_google(audio))
    f.write(" ")
f.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 836)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.selected_video_label = QtWidgets.QLabel(self.centralwidget)
        self.selected_video_label.setGeometry(QtCore.QRect(230, 20, 371,41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selected_video_label.setFont(font)
        self.selected_video_label.setFrameShape(QtWidgets.QFrame.Box)
        self.selected_video_label.setText("")
        self.selected_video_label.setObjectName("selected_video_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.transcribed_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.transcribed_text.setGeometry(QtCore.QRect(230, 320, 381, 431))
        self.transcribed_text.setObjectName("transcribed_text")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 280, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.transcribe_button = QtWidgets.QPushButton(self.centralwidget)
        self.transcribe_button.setEnabled(False)
        self.transcribe_button.setGeometry(QtCore.QRect(230, 150, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.transcribe_button.setFont(font)
        self.transcribe_button.setObjectName("transcribe_button")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(230, 250, 381, 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setGeometry(QtCore.QRect(0, 760, 651, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.message_label.setFont(font)
        self.message_label.setFrameShape(QtWidgets.QFrame.Box)
        self.message_label.setText("")
        self.message_label.setObjectName("message_label")
        self.output_file_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_file_name.setGeometry(QtCore.QRect(230, 90, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output_file_name.setFont(font)
        self.output_file_name.setObjectName("output_file_name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_mp4_video_recording = QtWidgets.QAction(MainWindow)
        self.actionOpen_mp4_video_recording.setObjectName("actionOpen_mp4_video_recording")
        self.actionAbout_vid2text = QtWidgets.QAction(MainWindow)
        self.actionAbout_vid2text.setObjectName("actionAbout_vid2text")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionOpen_mp4_video_recording)
        self.menuFile.addAction(self.actionNew)
        self.menuAbout.addAction(self.actionAbout_vid2text)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Selected video file:"))
        self.label_3.setText(_translate("MainWindow", "Output file name:"))
        self.label_5.setText(_translate("MainWindow", "Transcribed text:"))
        self.transcribe_button.setText(_translate("MainWindow", "Transcribe"))
        self.output_file_name.setPlaceholderText(_translate("MainWindow", "my_speech_file.txt"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen_mp4_video_recording.setText(_translate("MainWindow", "Open mp4 video recording"))
        self.actionAbout_vid2text.setText(_translate("MainWindow", "About vid2text"))
        self.actionNew.setText(_translate("MainWindow", "New"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
def open_audio_file(self):
    """Open the audio (*.mp4) file."""
    file_name = QFileDialog.getOpenFileName()
    if file_name[0][-3:] == "mp4":
        self.transcribe_button.setEnabled(True)
        self.mp4_file_name = file_name[0]
        self.message_label.setText("")
        self.selected_video_label.setText(file_name[0])
    else:
        self.message_label.setText("Please select an *.mp4 file")

self.transcribe_button.clicked.connect(self.process_and_transcribe_audio)

def process_and_transcribe_audio(self):
    """Process the audio into a textual transcription."""
    self.transcribe_button.setEnabled(False)
    self.convert_mp4_to_wav()
    self.transcribe_audio(self.audio_file)
    
def __init__(self):
    """Initialisation function."""
    self.mp4_file_name = ""
    self.output_file = ""
    self.audio_file = "speech.wav"
    
def convert_mp4_to_wav(self):
    """Convert the mp4 video file into an audio file."""
    audio_clip = AudioFileClip(self.mp4_file_name)
    audio_clip.write_audiofile(self.audio_file)