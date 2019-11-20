from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from search import Search

# 남성: BMR = 10 × 체중(kg) + 6.25 × 키(cm) - 5 × 나이(y) + 5
# 여성:	BMR = 10 × 체중(kg) + 6.25 × 키(cm) - 5 × 나이(y) - 161

class Calories:
  def __init__(self, title):
    self.root = Tk()
    self.root.wm_title(title)
    self.root.geometry("600x480+400+180")
    self.root.resizable(False, False)

    self.name_lb = Label(self.root, text = "이름 (ex. 000)", height=3, width=50, font = ("나눔바른고딕", 15))
    self.name_tb = ttk.Entry(self.root, width=20)
    self.age_lb = Label(self.root, text = "나이 (단위 : 세))", height=3, width=50, font = ("나눔바른고딕", 15))
    self.age_tb = ttk.Entry(self.root, width=20)
    self.weight_lb = Label(self.root, text = "몸무게 (단위 : kg)", height=3, width=50, font = ("나눔바른고딕", 15))
    self.weight_tb = ttk.Entry(self.root, width=20)
    self.height_lb = Label(self.root, text = "키 (단위 : cm)", height=3, width=50, font = ("나눔바른고딕", 15))
    self.height_tb = ttk.Entry(self.root, width=20)
    self.gender_lb = Label(self.root, text = "성별", height=3, width=50, font = ("나눔바른고딕", 15))

    string = StringVar()
    self.combo = ttk.Combobox(self.root, width=20, textvariable=string)
    self.combo['values'] = ('여자', '남자')
    self.combo.current(0)
    self.resultBtn = Button(self.root, text='결과 보기',font = ("나눔바른고딕",  20), command= lambda: self.cal_calories(string))

    self.name_lb.place(x=-110, y=32)
    self.name_tb.place(x = 300, y = 60)
    self.age_lb.place(x=-110, y=90)
    self.age_tb.place(x = 300, y = 120)
    self.weight_lb.place(x=-110, y=152)
    self.weight_tb.place(x = 300, y = 180)
    self.height_lb.place(x=-110, y=212)
    self.height_tb.place(x = 300, y = 240)
    self.gender_lb.place(x=-110, y=272)
    self.combo.place(x = 300, y = 300)
    self.resultBtn.place(x = 240, y = 400)

    self.root.mainloop()
    
# 자신의 정보를 입력하는 창 생성

  def cal_calories(self, string):
    BMR = 0.0
    try:
      while True:
        self.name = self.name_tb.get()
        self.age = int(self.age_tb.get())
        self.weight = float(self.weight_tb.get())
        self.height = float(self.height_tb.get())
        self.gender = string.get()

        if(self.gender=='남자'):
          BMR = (10*self.weight + 6.25*self.height - 5*float(self.age) + 5)/3
          # 남자의 BMR 구하는 공식 / 3으로 한끼 권장량 계산
        elif(self.gender=='여자'):
          BMR = (10*self.weight + 6.25*self.height - 5*float(self.age) - 161)/3
          # 여자의 BMR 구하는 공식 / 3으로 한끼 권장량 계산
        if BMR <= 0 :
          msg = messagebox.showinfo( "주의" , "BMR을 측정할 수 없습니다." )
        else :
          info = ("당신의 한 끼 권장 열량은 %.2f Kcal입니다." %BMR)
          msg = messagebox.showinfo( "알림" , info )
          
          self.go_search(BMR)

        break 
    except ValueError:
      messagebox.showinfo( "Title" , "형식에 맞추어 다시 입력해주세요 ;)" )  
# 자신의 '한끼 권장 열량'을 구하는 함수

  def go_search(self, BMR):
    BMR = float("%.2f" %BMR)
    self.root.destroy()
    Search(self.name, BMR)
# 조리 식품 리스트 창으로 이동


