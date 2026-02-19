import random

def Load_playlist(filename):
    try:
        with open(filename,"r") as file:
            return [song.strip() for song in file]
    except FileNotFoundError:
        print("file not found , creating a new playlist")
        return []

def save_playlist(filename,playlist):
    with open(filename ,"w") as file:
        for song in playlist:
            file.write(song + "\n")




playlist=[]
Filename=""
    
def  view_playlist(playlist):
    print('your current playlist is:')
    if not playlist:
        print('no playlist found')
    else:
        for i,song in enumerate(playlist,1):
            print(f'{i} {song}')

def add_song(playlist):
    while True:
        song_name = input("enter song to add (or type 'done' to stop): ")

        if song_name.lower() == "done":
            break
        playlist.append(song_name)
        print(f'{song_name} added to your play list ')

def remove_song(playlist):
    song_name=input('enter song to remove:')    
    try:
        playlist.remove(song_name)
        print(f'{song_name} is removed from your playlist')
    except:
        print(f'{song_name} is not found in the playlist')   

def shuffle(playlist):
    random.shuffle(playlist)   
    print('your playlist is shufffled')
    for i,song  in enumerate (playlist,1):
        print(f'{i} {song}') 

def main():
    print('welcome to playlist manager')
    print('1. view playlist')
    print('2. add song')
    print('3. remove song') 
    print('4. shuffle playlist')
    print('5. exit')
    try:
        choice = int(input('enter your choice: '))
        return choice
    except ValueError:
        print("enter a valid number")
        

  
def run_manager():

    global playlist
    global Filename

    filename = input("enter playlist file name: ")
    playlist = Load_playlist(filename)

    while True:
        user_choice = main()

        if user_choice == 1:
            view_playlist(playlist)

        elif user_choice == 2:
            add_song(playlist)
            save_playlist(filename, playlist)

        elif user_choice == 3:
            remove_song(playlist)
            save_playlist(filename, playlist)

        elif user_choice == 4:
            shuffle(playlist)
            save_playlist(filename, playlist)

        elif user_choice == 5:
            print('enjoy your music....')
            break

        else:
            print('enter a valid choice')


if __name__ =="__main__":
    run_manager()            


