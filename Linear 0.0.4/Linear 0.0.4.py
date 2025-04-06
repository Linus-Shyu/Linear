import webbrowser
import os
import time
import qrcode
import requests
from datetime import datetime

def get_user_rating(username):
    try:
        url = f"https://codeforces.com/api/user.rating?handle={username}"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'OK':
            contests = data['result']
            return [(c['contestId'], c['contestName'], c['ratingUpdateTimeSeconds'], c['newRating']) for c in contests]
        else:
            print("Error fetching rating data:", data.get('comment', 'Unknown error'))
            return None
    except Exception as e:
        print("Error:", e)
        return None

def draw_ascii_chart(data, width=60, height=20):
    if not data:
        return
    
    ratings = [x[3] for x in data]
    dates = [datetime.fromtimestamp(x[2]).strftime('%Y-%m') for x in data]
    
    min_rating = min(ratings)
    max_rating = max(ratings)
    range_rating = max_rating - min_rating
    if range_rating == 0:
        range_rating = 1
    
    # Normalize ratings to fit in the chart height
    normalized = [int((r - min_rating) / range_rating * (height - 1)) for r in ratings]
    
    # Create the chart
    chart = []
    for y in range(height - 1, -1, -1):
        line = []
        for i, val in enumerate(normalized):
            if i >= width:
                break
            if val == y:
                line.append('●')  # Data point
            elif val > y:
                line.append('│')  # Vertical line
            else:
                line.append(' ')  # Empty space
        
        # Add y-axis label
        current_rating = int(min_rating + (y / (height - 1)) * range_rating)
        line.append(f' {current_rating}')
        chart.append(''.join(line))
    
    # Add x-axis labels (dates)
    x_labels = []
    step = max(1, len(dates) // width)
    for i in range(0, min(len(dates), width), step):
        x_labels.append(dates[i][-2:])  # Show only month
    
    chart.append(' '.join(x_labels))
    
    return '\n'.join(chart)

def show_rating_history(username):
    rating_data = get_user_rating(username)
    if not rating_data:
        print(f"Could not fetch rating data for {username}")
        return
    
    print(f"\nCodeforces Rating History ({username}):")
    print("=" * 50)
    
    # Show basic stats
    current_rating = rating_data[-1][3]
    max_rating = max(r[3] for r in rating_data)
    min_rating = min(r[3] for r in rating_data)
    contests_count = len(rating_data)
    
    print(f"Current Rating: {current_rating}")
    print(f"Highest Rating: {max_rating}")
    print(f"Lowest Rating: {min_rating}")
    print(f"Contests Participated: {contests_count}")
    print("\nRating Chart:")
    
    # Draw ASCII chart
    chart = draw_ascii_chart(rating_data)
    if chart:
        print(chart)
    
    # Show last 5 contests
    print("\nLast 5 Contests:")
    for contest in rating_data[-5:]:
        date = datetime.fromtimestamp(contest[2]).strftime('%Y-%m-%d')
        print(f"{date}: {contest[1]} (Rating: {contest[3]})")

def main():
    print('\033[34m /$$       /$$\033[0m')
    print('\033[34m| $$      |__/\033[0m')
    print('\033[34m| $$       /$$ /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ \033[0m')
    print('\033[34m| $$      | $$| $$__  $$ /$$__  $$ |____  $$ /$$__  $$\033[0m')
    print('\033[34m| $$      | $$| $$  | $$| $$_____/ /$$__  $$| $$\033[0m')
    print('\033[34m| $$$$$$$$| $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \033[0m')
    print('\033[34m|________/|__/|__/  |__/ \\_______/ \\_______/|__/ \033[0m')
    os.system("echo ' '") 
    os.system("echo '\033[32m Developed by Linus Shyu \033[0m'")

    while True:
        command = input('What would you like to do: ')

        if command == 'home':
            webbrowser.open("https://atcoder.jp/")

        elif command == 'contest':
            webbrowser.open("https://atcoder.jp/contests/")

        elif command == 'rank':
            webbrowser.open("https://atcoder.jp/ranking")

        elif command == 'userdata':
            username = input('Enter your username: ')
            webbrowser.open(f"https://atcoder.jp/users/{username}")

        elif command == 'play':
            contest_name = input('Enter contest name: ')
            webbrowser.open(f"https://atcoder.jp/contests/{contest_name}")

        elif command == 'task':
            contest_name = input('Enter contest name: ')
            task_name = input('Enter task name (a-g): ').lower()
            if task_name in 'abcdefg':
                webbrowser.open(f"https://atcoder.jp/contests/{contest_name}/tasks/{contest_name}_{task_name}")

        elif command == 'submit':
            contest_name = input('Enter contest name: ')
            webbrowser.open(f"https://atcoder.jp/contests/{contest_name}/submit")

        elif command == 'stand':
            contest_name = input('Enter contest name: ')
            webbrowser.open(f"https://atcoder.jp/contests/{contest_name}/standings")

        elif command == 'code':
            user = input("Enter your Mac username: ")
            try:
                os.chdir(f"/Users/{user}/Desktop")
                folder_name = input("Enter contest name for folder: ")
                os.mkdir(folder_name)
                os.chdir(f"/Users/{user}/Desktop/{folder_name}")
                os.system("touch A.cpp B.cpp C.cpp D.cpp E.cpp F.cpp G.cpp")
                
                cpp_code = """#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef unsigned int uint;
typedef long double lb;
typedef long long ll;
typedef long l;

#define endl '\\n';

void solve()
{
  
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int T;
    cin >> T;
    while(T--)
    {
        solve();
    }
    return 0;
}
"""
                for filename in ['A.cpp', 'B.cpp', 'C.cpp', 'D.cpp', 'E.cpp', 'F.cpp', 'G.cpp']:
                    with open(filename, 'w') as f:
                        f.write(cpp_code)
                os.system(f'nvim /Users/{user}/Desktop/{folder_name}')
            except Exception as e:
                print(f"Error: {e}\nPlease check your username and try again!")

        elif command == 'clear':
            os.system("clear")

        elif command == 'time':
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        elif command == 'about':
            print('\033[34m /$$       /$$\033[0m')
            print('\033[34m| $$      |__/\033[0m')
            print('\033[34m| $$       /$$ /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ \033[0m')
            print('\033[34m| $$      | $$| $$__  $$ /$$__  $$ |____  $$ /$$__  $$\033[0m')
            print('\033[34m| $$      | $$| $$  | $$| $$_____/ /$$__  $$| $$\033[0m')
            print('\033[34m| $$$$$$$$| $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \033[0m')
            print('\033[34m|________/|__/|__/  |__/ \\_______/ \\_______/|__/ \033[0m')

            print('\033[34mWeChat QR code payment to support this project:\033[0m')
            code = 'wxp://f2f08Xmtax1P6TX2gayuRlMjXvgWRIJSXz5TmEnDiWWHgLLc3W7dIqFeUqjb4g8DAPp4'
            qr = qrcode.QRCode(version=1, box_size=1, border=1)
            qr.add_data(code)
            qr.print_ascii()

            print('\033[34mDeveloped by Linus Shyu\033[0m')
            print('\033[34mSupport this project to keep it running!\033[0m')

            print('GitHub Repository: \033[4mhttps://github.com/Linus-Shyu/AT-Tool\033[0m')
            print('Developer Bilibili: \033[4mhttps://space.bilibili.com/411591950\033[0m')
            print('Developer YouTube: \033[4mhttps://www.youtube.com/@LinusShyu\033[0m')

        elif command == 'exit':
            confirm = input('Are you sure to close all web pages? (y/n): ')
            if confirm.lower() == 'y':
                os.system('pkill Google Chrome')
                break
            if confirm.lower() == 'n':
                break

        elif command == 'help':
            print('\nAvailable commands:')
            print('home       - Open AtCoder home page')
            print('contest    - Open contests page')
            print('rank       - Open global rankings')
            print('userdata   - View user profile')
            print('play       - Open specific contest')
            print('task       - Open specific problem (a-g)')
            print('submit     - Open submission page')
            print('stand      - Open contest standings')
            print('code       - Create C++ template files for contest')
            print('clear      - Clear terminal screen')
            print('time       - Show current time')
            print('rating     - Show Codeforces rating graph')
            print('about      - Show about information')
            print('exit       - Exit the program')
            print('help       - Show this help message\n')

        elif command == 'rating':
            username = input('Enter Codeforces username: ')
            show_rating_history(username)

        elif command.strip() == '':
            continue

        else:
            print("Command not found. Type 'help' for available commands.")

if __name__ == '__main__':
    main()