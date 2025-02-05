import requests

def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        user_data = data['data']
        user_name = user_data['login']['username']
        country = user_data['location']['country']
        return user_name , country

def main():
    try:
        username,country_name= fetch_random_user()
        print(f'User_Name :{username} \nCountry_Name :{country_name}')
    except Exception as e:
        print(str(e))

if __name__=='__main__':
    main()