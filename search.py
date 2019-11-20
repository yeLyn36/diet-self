from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from recipe import Recipe
from selectedFoodsInterface import SelectedFoodInterface
import json
import datetime


with open('foods.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
# foods.json 파일을 통해 조리 식품 DB 가져오기

class Search(SelectedFoodInterface):

    def __init__(self, name, BMR):
        self.sum = 0.0
        self.names = []
        self.calories = []    
        self.show_foodlist = []
        self.select_foodlist = []

        self.root=Tk()
        self.root.wm_title("레시피 검색하기")
        self.root.geometry("1200x700+150+40")
        self.root.resizable(False, False)

        self.name=name
        self.BMR=BMR
        self.sum_cal=0

        self.search_food=ttk.Entry(self.root, width=52)
        self.cal = "/ " + str(self.BMR) + "kcal"
        self.sum_cal=Label(self.root, text=self.cal, height=3, width=10, font=("나눔바른고딕", 10))
        self.result_btn=Button(self.root, text="검색", font=20, command=self.search_foodlist)
        self.hr=Label(self.root, text="_________"*100, height=3, font=("나눔바른고딕", 10))

        self.show_foodview=ttk.Treeview(self.root, columns=['name', 'Kcal'])
        self.show_foodview.column("#0", width=100, anchor="center")
        self.show_foodview.heading("#0", text="번호", anchor="center")
        self.show_foodview.column("#1", width=500, anchor="center")
        self.show_foodview.heading("name", text="요리 명", anchor="center")
        self.show_foodview.column("#2", width=200, anchor="center")
        self.show_foodview.heading("Kcal", text="칼로리 (Kcal)", anchor="center")
        self.vsb = ttk.Scrollbar(orient="vertical",command=self.show_foodview.yview)
        self.show_foodview.configure(yscrollcommand=self.vsb.set)
        self.show_foodview.bind('<ButtonRelease-1>', self.add_list)

        self.selected_foodview=ttk.Treeview(self.root, columns=['name', 'Kcal'])
        self.selected_foodview.column("#0", width=100, anchor="center")
        self.selected_foodview.heading("#0", text="번호", anchor="center")
        self.selected_foodview.column("#1", width=500, anchor="center")
        self.selected_foodview.heading("name", text="요리 명", anchor="center")
        self.selected_foodview.column("#2", width=200, anchor="center")
        self.selected_foodview.heading("Kcal", text="칼로리 (Kcal)", anchor="center")
        self.vsb_s = ttk.Scrollbar(orient="vertical",command=self.selected_foodview.yview)
        self.selected_foodview.configure(yscrollcommand=self.vsb_s.set)
        self.selected_foodview.bind('<ButtonRelease-1>', self.show_recipe)

        for i in range(len(json_data['COOKRCP01']['row'])):
            self.show_foodlist.append((json_data['COOKRCP01']['row'][i]["RCP_NM"], json_data['COOKRCP01']['row'][i]["INFO_ENG"]))
            self.show_foodview.insert("", "end", text=i+1, values=self.show_foodlist[i], iid=str(i)+"번")
        # 아래 조리식품 리스트에 모든 식품 추가

        self.save_btn=Button(self.root, text="파일 저장", font=20, command=self.save)
        self.show_btn=Button(self.root, text="지우기", font=20, command=self.del_list)

        self.sum_cal.place(x=750, y=280)
        self.search_food.place(x=350, y=295)
        self.hr.place(x=0, y=220)
        self.result_btn.place(x=850, y=290)
        self.show_foodview.place(x=200, y=400, width=800, height=280)
        self.vsb.place(x=1000, y=400, height=290)
        self.selected_foodview.place(x=200, y=10, width=800, height=180)
        self.vsb_s.place(x=1000, y=10, height=190)
        self.save_btn.place(x=1030, y=50)
        self.show_btn.place(x=1040, y=90)

        self.root.mainloop()

    def search_foodlist(self):
        plus = 0
        self.show_foodview.delete(*self.show_foodview.get_children())

        self.show_foodlist = []
        self.search=str(self.search_food.get())

        print(self.show_foodlist)
        print(self.show_foodview)
        for i in range(len(json_data['COOKRCP01']['row'])):
            if self.search in str(json_data['COOKRCP01']['row'][i]["RCP_NM"]):
                self.show_foodlist.append((json_data['COOKRCP01']['row'][i]["RCP_NM"], json_data['COOKRCP01']['row'][i]["INFO_ENG"]))
                self.show_foodview.insert("", "end", text=plus+1, values=self.show_foodlist[plus], iid=str(i)+"번")
                plus+=1
    # 검색창에 단어나 글자를 입력하면 해당 검색어가 들어있는 항목들만 보여줌

    def show_recipe(self, selected_foodlist):
        curItem = self.selected_foodview.focus()
        item = self.selected_foodview.item(curItem, "values")
        Recipe(item[0])
    # 상단 리스트에서 클릭한 항목의 정보를 보여주는 메서드

    def add_list(self, a):
        self.selected_foodview.delete(*self.selected_foodview.get_children())

        curItem = self.show_foodview.focus()
        item = self.show_foodview.item(curItem, "values")
        if not(item in self.select_foodlist):
            if self.sum + float(item[1]) <= self.BMR:
                self.sum += float(item[1])
                self.select_foodlist.append((item[0], item[1]))
            else :
                messagebox.showinfo( "한 끼 권장 열량 초과" , "한끼 권장 열량을 초과했습니다." ) 
        for i in range(len(self.select_foodlist)):        
            self.selected_foodview.insert("", "end", text=i+1, values=self.select_foodlist[i], iid=str(i)+"번")
    # 아래 조리 식품 리스트의 항목을 클릭하면 상단 리스트에 추가되는 메서드

    def del_list(self):
        self.select_foodlist = []
        self.selected_foodview.delete(*self.selected_foodview.get_children())
        self.sum = 0
    # 지우기 버튼을 눌렀을 때 상단 리스트 뷰 초기화

    def save(self):  
        story = ""
        if self.select_foodlist:
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
            story += ("현재 날짜 : " + str(nowDatetime) + "\n")
            story += (self.name + "님의 현재 한끼 권장량 : " + str(self.BMR) + "\n")
            for i in range(len(self.select_foodlist)):
                story += (self.select_foodlist[i][0] + " : " + self.select_foodlist[i][1] + "Kcal\n")
            story += ("-" * 50)+"\n"
            with open("list.txt", "a", encoding="utf-8") as file :
                file.write(story)
    # 상단 리스트에 추가된 음식 항목들의 정보를 list.txt에 저장