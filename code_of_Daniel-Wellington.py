import math
import time
import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.size = 500
        self.clock = tk.Canvas(self, width=self.size, height=self.size, background='black')
        self.clock.grid(row=0, column=0, columnspan=2)
        self.clock.create_oval(2, 2, self.size-3, self.size-3, outline='silver', width=4)
        self.font_size = int(self.size/12)
        
        
        self.strNum = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
        for number in range(1, 12+1):
            x = self.size/2 + math.cos(math.radians(number/12*360-90))*self.size/2*0.86
            y = self.size/2 + math.sin(math.radians(number/12*360-90))*self.size/2*0.86
            angle = number/12*360
            self.clock.create_text(x, y, text=self.strNum[number-1], fill='silver', font=('Times New Roman', 28), angle=-angle)
            self.b = tk.Button(self, text='hide sec line', font=('', 14), command=self.toggle)
            self.b.grid(row=1, column=0)
            self.b2 = tk.Button(self, text=('hide date'), font=('', 14), command=self.toggle2)
            self.b2.grid(row=1, column=1)
            self.sec = time.localtime().tm_sec
            self.min = time.localtime().tm_min
            self.hour = time.localtime().tm_hour
            self.show_time = True
            self.show_day = True
    
    def toggle(self):
        if self.show_time:
            self.b.configure(text='show sec line')
            self.show_time = False
        else:
            self.b.configure(text='hide sec line')
            self.show_time = True
            
    def toggle2(self):
        if self.show_day:
            self.b2.configure(text='show date')
            self.show_day = False
        else:
            self.b2.configure(text='hide date')
            self.show_day = True
    
    def display(self):
        self.prev_num = -1
        if self.sec != self.prev_num:
            self.sec = time.localtime().tm_sec
            x0 = self.size/2
            y0 = self.size/2
            angle = math.radians(self.sec/60*360-90)
            x = x0 + math.cos(angle)*self.size/2*0.75
            y = y0 + math.sin(angle)*self.size/2*0.75
            self.clock.delete('SEC')
            if self.show_time:
                self.clock.create_line(x0, y0, x, y, fill='silver', tag='SEC')
                
            self.min = time.localtime().tm_min
            angle = math.radians(self.min/60*360-90)
            x = x0 + math.cos(angle)*self.size/2*0.75
            y = y0 + math.sin(angle)*self.size/2*0.75
            self.clock.delete('MIN')
            self.clock.create_line(x0, y0, x, y, fill='silver', width=3.5,  tag='MIN')
            
            self.hour = time.localtime().tm_hour
            angle = math.radians((self.hour/12 + self.min/60/12)*360-90)
            x = x0 + math.cos(angle)*self.size/2*0.65
            y = y0 + math.sin(angle)*self.size/2*0.65
            self.clock.delete('HOUR')
            self.clock.create_line(x0, y0, x, y, fill='silver', width=5, tag='HOUR')
                
            x = self.size/2
            y = self.size/2 - 85
            self.clock.create_text(x, y, text='DW', fill = 'silver', font = ('Times New Roman', 28),  tag='DW')
            y = self.size/2 -60
            self.clock.create_text(x, y, text='Daniel Wellington', fill='silver', font=('Times New Roman', 14), tag='WELLINTON')
            
            
            x = self.size/2
            y = self.size/2 + 70
            if self.hour < 12:
                text = time.strftime('AM')
            else:
                text = time.strftime('PM')
            self.clock.delete('TIME')
            if self.show_day:
                self.clock.create_text(x, y, text=text, fill='silver', font=('Times New Roman', 17), tag='TIME')
            x = self.size/2 + 140
            y = self.size/2
            self.clock.delete('TIMEDAY')
            if self.show_day:
                self.clock.create_text(x, y, text=time.strftime('%d'), fill='silver', font=('Times New Roman', 17), tag='TIMEDAY')
        
            self.after(100, self.display)
            self.prev_num = self.sec
            
root = tk.Tk()
f = MyFrame(root)
f.pack()
f.display()
root.mainloop()