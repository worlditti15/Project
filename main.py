import os,sys,time,csv


from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

#from custom_action import close_app
#import UI's
from ui_loading_screen import Ui_SplashScreen
from ui_main import *

from pygame import *
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from main_elements import *
from custom_action import *
from PyQt5.QtWidgets import QApplication, QListWidget, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PyQt5.QtCore import QDir


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QDir, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QTabWidget,
    QWidget)

#Global
counter=0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui =Ui_SplashScreen()
        self.ui.setupUi(self)

       #Remove Outer Windows Frame and remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

         #Timer
        self.timer=QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)
        self.show()
       

    #Update Progress Bar
    def progress(self):
        global counter

        #Set Value to progress bar
        self.ui.progressBar.setValue(counter)
        
        #Close loading or splashscreen and open main app
        if counter>=100:
            #stop Timer
            self.timer.stop()
            
            #show main window
            self.main=MainWindow()
            self.main.show()

            #close splash screen
            self.close()

        #Increase Counter 
        counter+=1



   #Class file for loading ui from ui file 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.ui=Ui_MainWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowState(Qt.WindowMaximized)
        self.ui.setupUi(self)  
        self.show()

        
        #player control function
        self.player = QMediaPlayer()
        self.ui.comboBox.currentIndexChanged.connect(self.load_music)

        self.ui.playbutton.clicked.connect(self.play_music)
        self.ui.close_button.clicked.connect(self.close_app)
        self.ui.m_list.itemClicked.connect(self.play_music)
        self.ui.minimize_button.clicked.connect(self.minimize_window)

       # self.ui.open_musicdiag.clicked.connect(self.scan_audio_files)


    def minimize_window(self):
        self.setWindowState(self.windowState() | Qt.WindowMinimized)
    #Change icon when pressed Play button
    def toggle_play_pause(self):
        if self.playing:
            self.play_button.setIcon(QIcon('play.png'))  # Change to play icon
        else:
            self.play_button.setIcon(QIcon('pause-button.png'))  # Change to pause icon
        
        self.playing = not self.playing

    def load_music(self):
        selected_genre = self.ui.comboBox.currentText()
        self.ui.m_list.clear()

        if selected_genre != "All":
            folder_path = r"C:\Users\Lenovo\Videos\all"  
            music_files = self.get_music_files(folder_path)
            
            self.ui.m_list.addItems(music_files)


    def get_music_files(self, folder_path):
        music_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('.mp3', '.wav', '.ogg')):
                    music_files.append(file)
        return music_files

    def add_songs_to_list(self, songs):
        for song in songs:
            song_item = QListWidgetItem(song)
            # Set text color using stylesheet
            song_item.setForeground(self.palette().color(self.palette().WindowText))
            self.ui.m_list.addItem(song_item)
            

    def close_app(self):
        sys.exit()

    def play_music(self, item):
        song_index = self.ui.m_list.row(item)
        song_path = self.music_files[song_index]

        if self.playing and self.current_song == song_path:
            pygame.mixer.music.pause()
            self.playing = False
        else:
            if self.playing:
                pygame.mixer.music.stop()

            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            self.playing = True
            self.current_song = song_path

    def open_file(self):
        file_dialog = QFileDialog()
        self.current_file, _ = file_dialog.getOpenFileName(self, "Open Music File", "", "Audio Files (*.mp3 *.wav)")
        if self.current_file:
            self.ui.song_label.setText(f"Playing: {self.current_file}")
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.current_file)))
            self.player.play()


    # Directory containing your audio files
    audio_directory = r"C:\Users\Lenovo\Videos\all"

    # CSV file to store the details
    csv_file = "audio_details.csv"

    # Function to scan audio files and register details in the CSV file
    def scan_audio_files(directory, csv_file):  
        audio_details = []

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.mp3', '.wav')):
                    file_path = os.path.join(root, file)
                    file_name = os.path.splitext(file)[0]
                    audio_details.append({'name': file_name, 'path': file_path})

    # Write details to the CSV file
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['name', 'path']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(audio_details)

        print(f"Scanned {len(audio_details)} audio files and registered details in '{csv_file}'.")

    # Call the function to scan and register audio files
    scan_audio_files(audio_directory, csv_file)
      
if __name__=="__main__":
    app=QApplication(sys.argv)
    
    window=SplashScreen()
    sys.exit(app.exec())



