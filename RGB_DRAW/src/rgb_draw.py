import tkinter

class RgbDraw():
    def __init__(self) -> None:
        window=tkinter.Tk()
        window.title("codingnow  RGB 그리기 Ver.02")
        window.geometry("640x400+100+100")#"너비x높이+x좌표+y좌표"
        window.resizable(False, False)
        
        frame1=tkinter.Frame(window, relief="solid", bd=2)
        # frame1.pack(side="left", fill="both", expand=True)
        frame1.place(x=0,y=0,width=400,height=400)

        frame2=tkinter.Frame(window, relief="solid", bd=2)
        # frame2.pack(side="right", fill="both", expand=True)
        frame2.place(x=400,y=0,width=240,height=400)
        self.status_sort = 0
        self.select_list = []
        cnt=0
        btn_size = 49
        self.buttons = []
        self.button_sel = [False for i in range(64)]
        for i in range(8):
            for k in range(8):
                btn=tkinter.Button(frame1, 
                                       text=str(cnt), 
                                       command = lambda cmd=str(cnt): self.btn_press(cmd)
                                       )
                # button1.grid(row=i, column=k, width=10, height=10)
                btn.place(x=k*btn_size+3, y=i*btn_size+3, width=btn_size, height=btn_size)
                # button1.bind("<Button-1>", self.btn_press())
                btn.configure(bg='white')
                self.buttons.append(btn)
                cnt += 1

        self.text_widget  = tkinter.Text(frame2, wrap=tkinter.WORD) 
        self.text_widget.configure(bg="lightgray", fg="black")
        self.text_widget.configure(font=("Arial", 10))
        self.text_widget .place(x=0,y=0,width=233,height=200)
        
        self.button2=tkinter.Button(frame2, 
                                    text="정렬하기", 
                                    command = lambda : self.btn_sort_change()
                                    )
        self.button2.place(x=2,y=205,width=233,height=90)
        
        self.button3=tkinter.Button(frame2, 
                                    text="모두지우기", 
                                    command = lambda : self.btn_clear()
                                    )
        self.button3.place(x=2,y=205+90+10,width=233,height=90)
        window.mainloop()
    
    def btn_sort(self): 
        self.text_widget.delete("1.0", tkinter.END)
        msg = ''
        cnt = 0
        total = 0
        
        msg = f'[번호 순서]\n\n'
        self.text_widget.insert(tkinter.END, msg)
        
        for i, staus in enumerate(self.button_sel):
            if staus:
                msg = f'{i},'
                cnt += 1
                total += 1
                if cnt > 10:
                    cnt = 0
                    self.text_widget.insert(tkinter.END, '\n')
                    
                self.text_widget.insert(tkinter.END, msg)
            
        if total > 0:
            msg = f'\n\n{total}개\n\n'
            self.text_widget.insert(tkinter.END, msg)
            
    def btn_sort_click(self): 
        self.text_widget.delete("1.0", tkinter.END)
        msg = ''
        cnt = 0
        total = 0
        
        msg = f'[클릭한 순서]\n\n'
        self.text_widget.insert(tkinter.END, msg)
        
        for i  in self.select_list:
            msg = f'{i},'
            cnt += 1
            total += 1
            if cnt > 10:
                cnt = 0
                self.text_widget.insert(tkinter.END, '\n')
                
            self.text_widget.insert(tkinter.END, msg)
                
        if total > 0:
            msg = f'\n\n{total}개\n\n'
            self.text_widget.insert(tkinter.END, msg)
    
    def btn_sort_change(self):
        
        if self.status_sort == 0:
            self.status_sort = 1
            self.btn_sort()
        else:
            self.status_sort = 0
            self.btn_sort_click()

    def btn_clear(self):
        print('clear')
        self.text_widget.delete("1.0", tkinter.END)
        self.select_list.clear()
        for i, staus in enumerate(self.button_sel):
            self.button_sel[i] = False
            self.buttons[i].configure(bg = 'white')
        
    def btn_press(self,cmd):
        print(f'bbbb {cmd}')
        idex = int(cmd)
        if self.button_sel[idex]:
            self.button_sel[idex] = False
            self.buttons[idex].configure(bg = 'white')
            if idex in self.select_list:
                self.select_list.remove(idex)
        else:
            self.button_sel[idex] = True
            self.buttons[idex].configure(bg = 'yellow')
            if idex not in self.select_list:
                self.select_list.append(idex)
        
        if self.status_sort == 0:
            self.btn_sort_click()
        else:
            self.btn_sort()
            
if __name__ == '__main__':
    main = RgbDraw()