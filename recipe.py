from tkinter import *
from tkinter import font
import json

with open('foods.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

class Recipe:    
    def __init__(self, item):
        self.master = Tk()
        self.master.wm_title(item + "의 정보")
        self.master.geometry("1000x600+200+50")
        self.master.resizable(False, False)
        
        font_info = font.Font(size=15)
    
        scrollbar_y = Scrollbar(self.master)
        scrollbar_x = Scrollbar(self.master, orient=HORIZONTAL)

        manuals = Listbox(self.master, font=font.Font(size=13), height=7, yscrollcommand = scrollbar_y.set, xscrollcommand = scrollbar_x.set)

        for i in range(len(json_data['COOKRCP01']['row'])):
            if item == json_data['COOKRCP01']['row'][i]["RCP_NM"]:
                titlelb = Label(self.master, text=json_data['COOKRCP01']['row'][i]["RCP_NM"], font=font.Font(size=30, weight="bold"))
                kindlb = Label(self.master, text=("(" + json_data['COOKRCP01']['row'][i]["RCP_PAT2"] + ")"), width=5, height=3, font=font_info)
                englb = Label(self.master, text=(json_data['COOKRCP01']['row'][i]["INFO_ENG"] + "g (1인분)"), height=3, font=font_info)
                carlb = Label(self.master, text=("탄수화물 : " + json_data['COOKRCP01']['row'][i]["INFO_CAR"] + " mg, "), height=3, font=font_info)
                prolb = Label(self.master, text=("단백질 : " + json_data['COOKRCP01']['row'][i]["INFO_PRO"] + " mg, "), height=3, font=font_info)
                fatlb = Label(self.master, text=("지방 : " + json_data['COOKRCP01']['row'][i]["INFO_FAT"] + " mg, "), height=3, font=font_info)
                nalb = Label(self.master, text=('나트륨 : ' + json_data['COOKRCP01']['row'][i]["INFO_NA"] + " mg"), height=3, font=font_info)
                lb = Label(self.master, text=("__" * 38), height=1, font=font_info)
                partslb = Label(self.master, text=("재료 : " + json_data['COOKRCP01']['row'][i]["RCP_PARTS_DTLS"]),)
                for j in range(1, 20+1):
                    if j < 10:
                        num = "0" + str(j)
                    if json_data['COOKRCP01']['row'][i]["MANUAL" + str(num)] == "" :
                        break
                    manual = json_data['COOKRCP01']['row'][i]["MANUAL" + str(num)]
                    print(manual)
                    manuals.insert(j, manual)
            
        scrollbar_y.config(command=manuals.yview)
        scrollbar_x.config(command=manuals.xview)
                
        titlelb.place(x=150, y=70)
        kindlb.place(x=150, y=120)
        englb.place(x=250, y=120)
        carlb.place(x=150, y=170)
        prolb.place(x=320, y=170)
        fatlb.place(x=460, y=170)
        nalb.place(x=580, y=170)
        lb.place(x=130, y=220)
        partslb.pack()
        partslb.place(x=50, y=260, width=900)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        manuals.place(x=130, y=400 + partslb.winfo_height(), width=800)
        scrollbar_y.pack( side = RIGHT, fill=Y )

                
        self.master.mainloop()
# 전달된 항목의 이름으로 레시피의 항목을 보여줌