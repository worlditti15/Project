import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel, QComboBox

class PlaylistUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Playlist')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.genre_combo = QComboBox()
        self.genre_combo.addItem("Select Genre")
        self.genre_combo.addItem("Rock")
        self.genre_combo.addItem("Pop")
        self.genre_combo.addItem("Classical")
        self.layout.addWidget(self.genre_combo)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.genre_combo.currentIndexChanged.connect(self.load_music)

    def load_music(self):
        selected_genre = self.genre_combo.currentText()
        self.list_widget.clear()

        if selected_genre != "Select Genre":
            folder_path = "path/to/your/music/folder"  # Replace with the actual folder path
            music_files = self.get_music_files(folder_path)
            
            self.add_songs_to_list(music_files)

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
            self.list_widget.addItem(song_item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlaylistUI()
    window.show()
    sys.exit(app.exec_())
