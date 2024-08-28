import requests


def main():
    test_post_api_authorize()

def test_post_api():
    api_link = 'https://dummyjson.com/auth/login'
    http_headers = {'Content-Type': 'application/json'}
    body = {"username": "emilys","password": "emilyspass"}
    response = requests.post(api_link, json=body,headers=http_headers)
    print("status:",response.status_code)
    print("data:",response.json())
    return response

def test_get_api():
    api_link = 'https://dummyjson.com/users'
    try:
        response = requests.get(api_link)
        if(response.status_code!=200):
            return {"status":response.status_code,"message":"api error!"}
        # print("resp code:",response.status_code)
        # print("resp:",response.json())
        return response.json()
    except requests.exceptions.ConnectTimeout:
        return {"status":502,"message":"Time out Error!"}

def test_post_api_authorize():
    api_link = 'https://dummyjson.com/auth/login'
    http_headers = {'Content-Type': 'application/json'}
    body = {"username": "emilys","password": "emilyspass"}
    authorize_api_link = "https://dummyjson.com/auth/me"
    response = requests.post(api_link, json=body,headers=http_headers)
    result = response.json()
    # print(result)
    access_token = f"Bearer {result['token']}"
    authorize_api_response = requests.get(authorize_api_link,headers={"Authorization":access_token})
    print("status",authorize_api_response.status_code)
    print("res",authorize_api_response.json())
    return authorize_api_response.json()


if __name__ == "__main__":
    main()
