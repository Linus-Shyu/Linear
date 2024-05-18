import webbrowser
import os
import time
import qrcode

def main():
    os.system("echo '\033[34m /$$       /$$\033[0m'")
    os.system("echo '\033[34m| $$      |__/\033[0m'")
    os.system("echo '\033[34m| $$       /$$ /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ \033[0m'")
    os.system("echo '\033[34m| $$      | $$| $$__  $$ /$$__  $$ |____  $$ /$$__  $$\033[0m'")  
    os.system("echo '\033[34m| $$      | $$| $$  | $$| $$_____/ /$$__  $$| $$\033[0m'")  
    os.system("echo '\033[34m| $$$$$$$$| $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \033[0m'")
    os.system("echo '\033[34m|________/|__/|__/  |__/ \_______/ \_______/|__/ \033[0m'")
    os.system("echo ' '") 
    os.system("echo '\033[32m Develop by Linus Shyu \033[0m'")

    while True:
        command = input('What are you want to do:')

        if(command == 'home'):
            webbrowser.open("https://atcoder.jp/")

        if(command == 'contest'):
            webbrowser.open("https://atcoder.jp/contests/")

        if(command == 'rank'):
            webbrowser.open("https://atcoder.jp/ranking")

        if(command == 'userdata'):
            User_Name = input('What is your username:')
            webbrowser.open("https://atcoder.jp/users/" + User_Name)

        if(command == 'play'): 
            Contest_Name = input('Contest Name:')
            webbrowser.open("https://atcoder.jp/contests/" + Contest_Name)

        if(command == 'task'):
            Contest_Name = input('Contest Name:')
            Task_Name = input('Task Name:')
            if(Task_Name == 'a'):
                webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/tasks/" + Contest_Name + "_a")
            if(Task_Name == 'b'):
                webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/tasks/" + Contest_Name + "_b")
            if(Task_Name == 'c'):
                webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/tasks/" + Contest_Name + "_c")
            if(Task_Name == 'd'):
                webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/tasks/" + Contest_Name + "_d")
            if(Task_Name == 'e'):
                webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/tasks/" + Contest_Name + "_e")
            if(Task_Name == 'f'):
                webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/tasks/" + Contest_Name + "_f")
            if(Task_Name == 'g'):
                webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/tasks/" + Contest_Name + "_g")
    
        if(command == 'submit'):
            Contest_Name = input('Contest Name:')
            webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/submit")
    
        if(command == 'stand'):
            Contest_Name = input('Contest Name:')
            webbrowser.open("https://atcoder.jp/contests/" + Contest_Name + "/standings")

        if(command == 'code'):
            user = input("Your Mac username:")
            try:
                os.chdir("/Users/" + user + "/Desktop")
                File = input("Contest Name:")
                os.mkdir(File)
                os.chdir("/Users/" + user + "/Desktop/" + File)
                os.system("touch A.cpp && touch B.cpp && touch C.cpp && touch D.cpp && touch E.cpp && touch F.cpp && touch G.cpp")
                os.system('nvim ' "/Users/" + user + "/Desktop/" + File)
            except:
                print("Please check your username try again!")

        if(command=="clear"):
            os.system("clear")

        if(command == 'time'):
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        if(command == 'about'):
            os.system("echo '\033[34m     __    _                 _____ __                \033[0m'")
            os.system("echo '\033[34m    / /   (_____  __  ______/ ___// /_  __  ____  __ \033[0m'")
            os.system("echo '\033[34m   / /   / / __ \/ / / / ___\__ \/ __ \/ / / / / / / \033[0m'")
            os.system("echo '\033[34m  / /___/ / / / / /_/ (__  ___/ / / / / /_/ / /_/ /  \033[0m'")
            os.system("echo '\033[34m /_____/_/_/ /_/\__,_/____/____/_/ /_/\__, /\__,_/   \033[0m'")
            os.system("echo '\033[34m                                    /____/           \033[0m'")
            os.system("echo ' '")

            os.system("echo '\033[34mWeChat QR code payment to help this project continue to update!!!\033[0m'")                                                                                    
            code = 'wxp://f2f08Xmtax1P6TX2gayuRlMjXvgWRIJSXz5TmEnDiWWHgLLc3W7dIqFeUqjb4g8DAPp4'
            qr = qrcode.QRCode(version = 1, box_size = 1, border = 1)
            qr.add_data(code)
            qr.print_ascii()

            os.system("echo '\033[34m Develop by Linus Shyu \033[0m'")
            os.system("echo '\033[34m Give me some power to keep this App running! \033[0m'")

            os.system("echo ' Linear Open Source Page:\033[4mhttps://github.com/Linus-Shyu/AT-Tool\033[0m'")
            os.system("echo ' Developer Bilibili:\033[4mhttps://space.bilibili.com/411591950\033[0m'")
            os.system("echo ' Developer Youtube:\033[4mhttps://www.youtube.com/@LinusShyu\033[0m'")

        if(command == 'exit'):
            close = input('Are you sure to close all web pages:(yes for ''y''|no for ''n''):')
            if(close == 'y'):
                os.system('pkill Google Chrome')
                break
            if(close == 'n'):
                break
        if(command == 'help'):
            print('home --visit home page')
            print('contest --visit contest page')
            print('rank --visit world rank page')
            print('userdata --visit personal data page')
            print('play -- visit contest page')
            print('task -- visit task page') 
            print('submit -- visit submit page')
            print('stand -- visit contest rank page')
            print('code -- create C++ code folder about contest')
            print('clear -- clear the information about AT-Tool')
            print('time -- show time for now')
            print('about -- support and some information about AT-Tool')



        if(command != 'home' and command != 'contest' and command != 'help' and command != 'rank' and command != 'userdata' and command != 'play' and command != 'task' and command != 'submit' and command != 'stand' and command != 'code' and command != 'clear' and command != 'time' and command != 'about' and command != '' and command.strip() != ''):
            print("can't found command,please try again or type 'help'")

if __name__ == '__main__':
    main()