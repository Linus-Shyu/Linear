import requests
from datetime import datetime
import math
import os
from collections import defaultdict

def clear_screen():
    """清空命令行屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_rating(handle):
    """获取指定用户的 rating 信息"""
    url = f"https://codeforces.com/api/user.rating?handle={handle}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] == 'OK':
            return data['result']
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

def print_centered(text, width=60, fill_char='='):
    """居中打印文本"""
    padding = (width - len(text)) // 2
    print(f"{fill_char*padding} {text} {fill_char*padding}")

def print_rating_info(handle, rating_data):
    """在命令行中显示用户 rating 信息"""
    if not rating_data:
        print(f"用户 {handle} 没有比赛记录")
        return
    
    current_rating = rating_data[-1]['newRating']
    max_rating = max(contest['newRating'] for contest in rating_data)
    min_rating = min(contest['newRating'] for contest in rating_data)
    contest_count = len(rating_data)
    
    # 计算rating变化
    rating_changes = [contest['newRating'] - contest['oldRating'] for contest in rating_data[1:]]
    avg_change = sum(rating_changes) / len(rating_changes) if rating_changes else 0
    
    clear_screen()
    print_centered(f"Codeforces Rating: {handle}")
    print(f"\n{'当前Rating:':<15}{current_rating}")
    print(f"{'最高Rating:':<15}{max_rating}")
    print(f"{'最低Rating:':<15}{min_rating}")
    print(f"{'参赛次数:':<15}{contest_count}")
    print(f"{'平均变化:':<15}{avg_change:+.1f}\n")
    
    # 绘制ASCII图表
    draw_ascii_chart(handle, rating_data)
    
    # 显示最近比赛
    print("\n最近5场比赛:")
    for contest in rating_data[-5:][::-1]:
        date = datetime.fromtimestamp(contest['ratingUpdateTimeSeconds']).strftime('%Y-%m-%d')
        change = contest['newRating'] - contest['oldRating']
        print(f"{date} {contest['contestName'][:30]:<30} {contest['newRating']} ({change:+.0f})")

def draw_ascii_chart(handle, rating_data):
    """在命令行中绘制ASCII rating图表"""
    if len(rating_data) < 2:
        print("比赛数据不足，无法绘制图表")
        return
    
    ratings = [contest['newRating'] for contest in rating_data]
    min_r = min(ratings)
    max_r = max(ratings)
    
    # 调整图表高度范围
    chart_min = math.floor(min_r / 100) * 100
    chart_max = math.ceil(max_r / 100) * 100
    if chart_max - chart_min < 200:
        chart_min = max(0, chart_min - 100)
        chart_max += 100
    
    height = 10  # 图表高度(行数)
    scale = (chart_max - chart_min) / height
    
    # 初始化图表网格
    chart = [[' ' for _ in range(len(ratings))] for _ in range(height)]
    
    # 填充数据点
    for i, rating in enumerate(ratings):
        row = height - 1 - min(int((rating - chart_min) / scale), height - 1)
        chart[row][i] = '●'
    
    # 连接数据点
    for i in range(1, len(ratings)):
        prev_row = height - 1 - min(int((ratings[i-1] - chart_min) / scale), height - 1)
        curr_row = height - 1 - min(int((ratings[i] - chart_min) / scale), height - 1)
        
        if prev_row == curr_row:
            continue
        
        step = 1 if curr_row > prev_row else -1
        for row in range(prev_row, curr_row, step):
            if 0 <= row < height:
                chart[row][i] = '│'
    
    # 添加Y轴标签
    y_labels = [f"{int(chart_max - i*scale):<4}" for i in range(height)]
    
    # 打印图表
    print("Rating变化图表:")
    for row, label in zip(chart, y_labels):
        print(f"{label} {' '.join(row)}")
    
    # 打印X轴
    print("    " + "─" * (len(ratings)*2 - 1))
    
    # 简化的X轴标签
    if len(ratings) > 10:
        step = len(ratings) // 5
        x_labels = [' '] * len(ratings)
        for i in range(0, len(ratings), step):
            x_labels[i] = str(i+1)
        print("     " + ' '.join(x_labels) + " (比赛场次)")

def main():
    clear_screen()
    print_centered("Codeforces Rating 查询工具")
    
    while True:
        handle = input("\n请输入 Codeforces 用户名 (或输入 'q' 退出): ").strip()
        if handle.lower() == 'q':
            break
        
        print("查询中...")
        rating_data = get_user_rating(handle)
        
        if rating_data is not None:
            print_rating_info(handle, rating_data)

if __name__ == "__main__":
    main()