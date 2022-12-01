# module load
import random  
import os
import platform
from time import sleep   


menu = ""
menus = []

def input_menu():   # 후보기입 함수
    global menus
    global menu
    try:
        hubo = int(input("후보 갯수 >>>"))  
        if hubo <= 0:
            print("후보 1개 이상을 입력해주세요")
            input_menu()
        else:
            pass
        for i in range(1, hubo+1):
            menu = input("먹고싶은 메뉴 %d번째 후보를 적어주세요! - " %i)
            menus.append(menu)
    except:
        print("정수로 치라고")
        input_menu()
    return menus, menu

def chDinner():     # 메뉴추첨 함수
    global menus
    sleep(1)
    print("\n당신이 고른 후보들 중 하나를 추첨해 드릴게요!")
    for f in range(100):
        print(random.choice(menus))
        sleep(f*(1/1000))
        if f == 90:
            sleep(f*(1/500))
    result = random.choice(menus)
    print(f"\n{result}'가 나왔네요! 5초 뒤에 배달사이트 열어드릴게요!")
    sleep(5)
    try:        # 시스템 운영체제 확인 & 배달사이트 오픈
        if platform.system() == "Windows":
            os.system('explorer "https://www.yogiyo.co.kr/mobile/#/"')
            return
        elif platform.system() == "Darwin":
            os.system('open "https://www.yogiyo.co.kr/mobile/#/"')
            return
    except:
        print("당신이 뭔가 일을 저질렀어요! 자숙하세요!")
        exit()


# 실행
input_menu()
chDinner()
