import json
import matplotlib.pyplot as plt

def process_user(data):
    return {
        "name": data.get("login"),
        "followers": data.get("followers"),
        "repos": data.get("public_repos")
    }


def save_to_file(data, filename="data/users.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_from_file(filename="data/users.json"):
    import json
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        print("读取失败")
        return []


def analyze_users(users):
    if not users:
        print("没有数据")
        return

    # 排序（核心）
    users.sort(key=lambda x: x["followers"], reverse=True)

    print("\n===== 用户排行榜 =====")

    for i, user in enumerate(users):
        print(f"{i+1}. {user['name']} - 粉丝: {user['followers']}")

    # 平均值
    total = sum(u["followers"] for u in users)
    avg = total / len(users)

    print("\n平均粉丝:", avg)

    # Top用户
    top = users[0]
    print("最强用户:", top["name"])


def plot_users(users):
    if not users:
        return

    names = [u["name"] for u in users]
    followers = [u["followers"] for u in users]

    # ⭐ 关键：设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
    plt.rcParams['axes.unicode_minus'] = False    # 解决负号问题

    plt.figure()
    plt.bar(names, followers)

    plt.title("GitHub 用户粉丝数对比")
    plt.xlabel("用户")
    plt.ylabel("粉丝数")

    plt.show()