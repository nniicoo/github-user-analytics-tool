from api import fetch_user
from utils import process_user, save_to_file, load_from_file, analyze_users, plot_users

def main():
    print("GitHub 用户分析工具")
    print("=" * 30)

    users = []

    while True:
        name = input("输入GitHub用户名（输入 q 结束）: ")

        if name == "q":
            break

        users.append(name)

    results = []

    for u in users:
        data = fetch_user(u)

        if data:
            user = process_user(data)
            results.append(user)

    save_to_file(results)

    data = load_from_file()
    analyze_users(data)

    plot_users(data)


if __name__ == "__main__":
    main()