import requests

def randuser_freeAPI():
    url = 'https://api.freeapi.app/api/v1/public/books/39'
    
    response = requests.get(url)
    # print(response)
    data  = response.json()

    if data['success'] and 'data' in data:
        user_data = data['data']
        title = user_data['volumeInfo']['title']
        user_country = user_data['accessInfo']['country']
        return title,user_country
    else:
        raise Exception("Failed to fetch user data!!")
       
        
def main():
    try:
        title,country = randuser_freeAPI()
        print(f"Title of the book is : {title}, Country: {country}")
    except Exception as ex:
        print(str(ex))

if __name__ == "__main__":
    main()