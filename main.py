import pygame
import tkinter as tk
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")  # Set background color

        pygame.mixer.init()

        self.loaded_files = []  # List to store loaded files

        button_style = {
            'font': ('Helvetica', 12, 'bold'),
            'bg': '#e74c3c',
            'fg': 'white',
            'activebackground': '#c0392b',
            'activeforeground': 'white',
            'relief': 'raised',
            'bd': 3,
            'width': 20
        }

        # Title Label
        self.title_label = tk.Label(
            self.root,
            text="Music Player",
            font=("Helvetica", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        self.title_label.pack(pady=10)

        # Load Button
        self.load_button = tk.Button(self.root, text="Load Music", command=self.load_music, **button_style)
        self.load_button.pack(pady=10)

        # Play/Pause Button with custom styling
        self.play_pause_button = tk.Button(
            self.root,
            text="Play",
            command=self.toggle_play_pause,
            font=('Arial', 12, 'bold'),
            bg='#1abc9c',
            fg='white',
            activebackground='#16a085',
            activeforeground='white',
            relief='flat',
            bd=0,
            width=15,
            height=2
        )
        self.play_pause_button.pack(pady=10)

        # Stop Button
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music, **button_style)
        self.stop_button.pack(pady=10)

        # Listbox to show loaded files
        self.file_listbox = tk.Listbox(
            self.root,
            width=50,
            height=15,
            font=('Helvetica', 10),
            bg="#ecf0f1",
            fg="#2c3e50",
            selectbackground="#3498db",
            selectforeground="white",
            relief='flat',
            bd=0
        )
        self.file_listbox.pack(pady=20)
        self.file_listbox.bind('<Double-1>', self.play_selected_file)

        self.current_file = None
        self.is_playing = False

    def load_music(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Music Files", "*.mp3")])
        for file_path in file_paths:
            if file_path not in self.loaded_files:
                self.loaded_files.append(file_path)
                self.file_listbox.insert(tk.END, file_path.split('/')[-1])  # Show only the file name
        print("Files loaded:", self.loaded_files)

    def toggle_play_pause(self):
        if not self.current_file:
            print("No music loaded!")
            return

        if self.is_playing:
            pygame.mixer.music.pause()
            self.play_pause_button.config(text="Play")
            print("Music paused.")
        else:
            pygame.mixer.music.play()
            self.play_pause_button.config(text="Pause")
            print("Music started playing.")
        self.is_playing = not self.is_playing

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.play_pause_button.config(text="Play")
        print("Music stopped.")

    def play_selected_file(self, event):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.loaded_files[selected_index[0]]
            self.current_file = selected_file
            pygame.mixer.music.load(selected_file)
            pygame.mixer.music.play()
            self.play_pause_button.config(text="Pause")
            self.is_playing = True
            print(f"Playing: {selected_file}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
