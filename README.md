# PyPlay — Persistent Playlist Manager 🎵

PyPlay is a command-line playlist manager built using Python that allows users to create, manage, and maintain music playlists with permanent file storage. The application provides a simple, interactive, and efficient way to organize songs directly from the terminal.

PyPlay ensures that your playlist is saved automatically, so your songs remain available even after closing the program.

---

# Key Features

## Persistent Playlist Storage

* Saves playlist data in a `.txt` file for permanent storage
* Automatically loads existing playlists when the program starts
* Prevents data loss by saving changes immediately after modifications
* Allows reuse and management of playlists across multiple sessions

---

## View Playlist

* Displays all songs currently in the playlist
* Shows songs in a clean, numbered format for easy reading
* Helps users quickly see the full contents of their playlist
* Displays an appropriate message if the playlist is empty

Example:

```
Your current playlist:
1. Lose Yourself
2. Stan
3. Mockingbird
```

---

## Add Songs (Continuous Input Supported)

* Allows users to add new songs to the playlist
* Supports adding multiple songs continuously without returning to the menu
* Uses a simple keyword (`done`) to stop adding songs
* Automatically updates and saves the playlist file after adding songs
* Ensures newly added songs are permanently stored

Example:

```
Enter song to add: Beautiful
Beautiful added to your playlist

Enter song to add: Done
```

---

## Remove Songs

* Allows users to remove any song from the playlist
* Searches the playlist and removes the specified song
* Displays confirmation after successful removal
* Shows an error message if the song is not found
* Automatically updates the saved playlist file

---

## Shuffle Playlist

* Randomly rearranges the order of songs in the playlist
* Uses Python’s built-in randomization functionality
* Provides a new listening order each time shuffle is used
* Automatically saves the new shuffled order

---

## Automatic File Synchronization

* Ensures playlist file always reflects the latest changes
* Eliminates need for manual saving
* Maintains consistency between memory and stored data

---

## Menu-Driven User Interface

* Provides a clear and simple menu for navigation
* Allows users to select actions easily using numbered options
* Keeps the program running until the user chooses to exit
* Improves usability and interaction

Menu Example:

```
1. View playlist
2. Add song
3. Remove song
4. Shuffle playlist
5. Exit
```

---

## Input Validation and Error Handling

* Prevents program crashes from invalid input
* Handles missing files safely
* Displays helpful error messages when necessary
* Improves overall program reliability

---

# Technical Features

* Modular function-based design
* Persistent storage using file handling
* Efficient playlist management using Python lists
* Clean and readable code structure
* Interactive command-line interface

---

# Technologies Used

* Python
* File Handling
* Command-Line Interface (CLI)
* Modular Programming

---

# How Playlist Storage Works

Each playlist is stored in a simple text file format:

Example file:

```
Lose Yourself
Stan
Mockingbird
Beautiful
```

Each line represents one song.

---

# Example Workflow

```
Enter playlist file name: gym.txt

1. View playlist
2. Add song
3. Remove song
4. Shuffle playlist
5. Exit

Enter choice: 2
Enter song to add: Mockingbird
Mockingbird added

Enter song to add: done
```

---

# Project Purpose

PyPlay was created to demonstrate:

* Python programming fundamentals
* File handling and persistent storage
* Command-line application development
* Modular program design
* Real-world project structure

---

# Author

Harshit Joshi

---

# Future Improvements

Possible enhancements include:

* Song search functionality
* Multiple playlist switching
* Duplicate song prevention
* Graphical User Interface (GUI)
* JSON-based storage

---

# Summary

PyPlay is a reliable, efficient, and scalable playlist manager that demonstrates core Python development skills and real-world application design.
