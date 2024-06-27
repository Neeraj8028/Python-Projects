import json

def load_video():
    try:
        with open('facebook.txt','r') as file:
            json.load(file)
    except FileNotFoundError:
        return []
    
def save_video_file(video):
    with open('facebook.txt','w') as file:
        json.dump(video,file)
        
def video_list(video):
    for index, video in enumerate(video,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
        
def add_video(video):
    name  = input("Enter video name: ")
    time = input("Enter duration of the video: ")
    
    video.append({'name':name, 'time':time})
    save_video_file(video)
    


def update_video(video):
    video_list(video)
    index = int(input("Enter video number: "))
    
    if 1 <= index >= len(video):
        name = input("Enter name of the video: ")
        time = input("Enter time of the video")
        
        video[index-1]={'name':name , 'time':time}
        save_video_file(video)
    else:
        print("Invalid index")

def delete_video(video):
    video_list(video)
    index = int(input("Enter the number which video you want to delete: "))
    
    if 1<= index >= len(video):
        del video [index-1]
        save_video_file(video)
    else:
        print("Invalid index")
        
def main():
        
        video = load_video()
        while(True):
            print("******************************")
            print("Youtube videos Manager")
            print("******************************")
            print("List of Youtube Videos")
            print("Add video in Youtube list")
            print("Update video in video list")
            print("Delete a video in a video list")
            print("Exit from the list")
            index = input("Choose any Options from above list: ")

            match index:
                case '1':
                    video_list(video)
                case '2':
                    add_video(video)
                case '3':
                    update_video(video)
                case '4':
                    delete_video(video)
                # case '5':
                #     exit_list(video)
                
if __name__ == "__main__":
    main()
    
