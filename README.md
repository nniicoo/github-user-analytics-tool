# GitHub 用户数据分析工具（Python）

## 📌 项目简介
本项目是一个基于 Python 开发的 GitHub 用户数据分析工具，支持通过 GitHub API 获取用户信息，并进行数据处理、分析与可视化展示。同时提供命令行（CLI）和图形界面（GUI）两种使用方式。

---

## 🚀 功能特点

- 🔍 根据用户名获取 GitHub 用户数据
- 📊 自动统计用户粉丝数、仓库数等信息
- 🏆 生成用户排行榜（按粉丝数排序）
- 💾 支持数据保存为 JSON 文件
- 📈 使用 matplotlib 生成可视化图表
- 🖥️ 提供 tkinter 图形界面，支持交互操作

---

## 🧱 项目结构

```bash
github_user_tool/
│
├── main.py # 命令行版本入口
├── gui.py # GUI界面程序
├── api.py # API请求模块
├── utils.py # 数据处理/分析/可视化
├── data/
│ └── users.json # 存储用户数据


---

## ⚙️ 环境要求

- Python 3.7+
- pip

安装依赖：

```bash
pip install requests matplotlib
▶️ 使用方法
1️⃣ 命令行版本

运行：

python main.py

输入 GitHub 用户名（多个用逗号分隔或按提示输入），程序会：

获取数据
保存 JSON
输出排行榜
显示图表
2️⃣ GUI 图形界面版本（推荐）

运行：

python gui.py

##功能：

输入用户名（如：octocat,torvalds）
点击按钮获取数据
一键生成排行榜
显示可视化图表
---
##📊 示例功能
用户排行榜（按粉丝数排序）
平均粉丝统计
柱状图展示用户影响力对比
---
##🧠 技术要点
HTTP 请求：requests
数据结构：list / dict
文件存储：json
数据分析：排序 / 聚合（sum）
可视化：matplotlib
图形界面：tkinter
---
##💼 项目亮点
实现完整的数据处理流程（获取 → 存储 → 分析 → 展示）
模块化设计（api / utils / 主程序解耦）
提供 CLI 与 GUI 两种交互方式
具备基础数据分析与可视化能力
---
👤 Author

This project is built for learning Python, API integration, and data analysis, and serves as a portfolio project demonstrating engineering and analytical skills.
---
