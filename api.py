import requests

def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    
    try:
        res = requests.get(url)
        
        if res.status_code == 200:
            return res.json()
        else:
            print(f"{username} 请求失败")
            return None
    except Exception as e:
        print("请求错误:", e)
        return None