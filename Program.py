# DIET-SELF 사용설명서 
# 1. Program.py를 실행해주세요
# 2. '한끼 권장량 구하기' 버튼을 클릭하세요.
# 3. 이름, 나이, 몸무게, 키, 성별을 체크해주세요 ! 하나라도 입력하지 않으면 BMR 값이 나오지 않아요 ㅜㅜㅠ 모두 입력해주세요
# 4. 다 입력하셨다면 아래 버튼을 누르면 자신의 '한끼 권장 열량'을 알 수 있어요 ! 
# *** 여기서 주의 : 한끼 권장 열량입니당 하루 권장 열량이 아니니 너무 적다고 놀라지 마세요 !! ***
# 5. 조리 식품 리스트 창에서 아래 원하는 음식이 있다면 항목을 눌러주세요 ! 위 상단 리스트에 추가될 거에요
# 6. 위 상단 리스트에서 원하는 항목을 누르시면 해당 음식에 대한 열량, 영양분, 재료, 레시피를 알 수 있어요 !
# 7. 조리 식품 리스트 창에서 위 상단 리스트 오른쪽에 위치한 버튼 중 '파일 저장' 버튼을 누르면 옆 리스트의 항목들이 list.txt에 저장됩니당 !
# 8. 아래 지우기 버튼을 눌러주시면 옆 상단 리스트의 항목들이 초기화될 거에요 !! 조심히 눌러주세요 
#
# 오늘도 당신의 다이어트를 응원합니다 ,,!

from calories import Calories
from tkinter import *

class App():
    def __init__(self, master, title):
        self.master = master
        self.title = title
        titleLb = Label(self.master, text = self.title, height=3, font = ("나눔바른고딕", 36))
        titleLb.place(x=60, y=30)
        titleBtn = Button(self.master, text='한끼 권장량 구하기',font = ("나눔바른고딕", 20), command=self.check)
        titleBtn.place(x=90, y=170)

    def check(self):
        self.master.destroy()
        Calories("한끼 권장량 구하기")
        
        
title = 'DIET - SELF'
root = Tk()
root.wm_title(title)
app = App(root, title)
root.geometry("400x300+550+250")
root.resizable(False, False)
root.mainloop()