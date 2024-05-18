import webbrowser
import os
import time

os.system('bash /Users/faxinxu/Desktop/AT-Tool/logo.sh')
print(' ')

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
        os.system('bash /Users/faxinxu/Desktop/AT-Tool/code.sh')

    if(command=="clear"):
        os.system("clear")

    if(command == 'time'):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    if(command == 'about'):
        os.system('bash /Users/faxinxu/Desktop/AT-Tool/linusshyu.sh')

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



    if(command != 'home' and command != 'contest' and command != 'rank' and command != 'userdata' and command != 'play' and command != 'task' and command != 'submit' and command != 'stand' and command != 'code' and command != 'clear' and command != 'time' and command != 'about'):
        print("can't found command,please try again or type 'help'")
