import sqlite3

con = sqlite3.connect("youtube_videos.db")
cursor = con.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_ID, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_ID))
    con.commit()

def delete_video(video_ID):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_ID,))
    con.commit()

def main():
    while True:
        print("******************************")
        print("Youtube videos Manager")
        print("******************************\n")
        print("1. List of Youtube Videos")
        print("2. Add video in Youtube list")
        print("3. Update video in video list")
        print("4. Delete a video in a video list")
        print("5. Exit from the list")
        choice = input("Choose any Options from above list: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time duration: ")
            add_videos(name, time)
        elif choice == '3':
            video_ID = int(input("Enter your video number you want to update: "))
            name = input("Enter video name: ")
            time = input("Enter video time duration: ")
            update_video(video_ID, name, time)
        elif choice == '4':
            video_ID = int(input("Enter your video number you want to delete: "))
            delete_video(video_ID)
        elif choice == '5':
            break
        else:
            print("Invalid video index!!")

    con.close()

if __name__ == "__main__":
    main()
