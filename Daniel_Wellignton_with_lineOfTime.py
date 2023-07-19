import math
import time
import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.size = 470
        self.clock = tk.Canvas(self, width=self.size, height=self.size, background='black')
        self.clock.grid(row=0, column=0)
        self.clock.create_oval(2, 2, self.size-3, self.size-3, outline='silver', width=4)
        self.font_size = int(self.size/12)
        
        for number in range(1, 12+1):
            self.sec = time.localtime().tm_sec
            self.min = time.localtime().tm_min
            self.hour = time.localtime().tm_hour
        for number in range(1, 60+1):
            if number%5 != 0:
                x = self.size/2 + math.cos(math.radians(number*6-90))*self.size/2*0.95
                y = self.size/2 + math.sin(math.radians(number*6-90))*self.size/2*0.95
                angle = number/60*360
                self.clock.create_text(x, y, text='|', fill='silver', font=('', 18), angle=-angle)
            else:
                x = self.size/2 + math.cos(math.radians(number*6-90))*self.size/2*0.91
                y = self.size/2 + math.sin(math.radians(number*6-90))*self.size/2*0.91
                angle = number/60*360
                self.clock.create_text(x, y, text='|', fill='silver', font=('', 42), angle=-angle)
                
    def display(self):
        
        self.sec = time.localtime().tm_sec
        x0 = self.size/2
        y0 = self.size/2
        angle = math.radians(self.sec/60*360-90)
        x = x0 + math.cos(angle)*self.size/2*0.78
        y = y0 + math.sin(angle)*self.size/2*0.78
        self.clock.delete('SEC')
        self.clock.create_line(x0, y0, x, y, width=2, fill='silver', tag='SEC')
        
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
        self.clock.create_text(x, y, text=time.strftime('%d'), fill='silver', font=('Times New Roman', 17), tag='TIMEDAY')
        
        self.after(100, self.display)
root = tk.Tk()
f = MyFrame(root)
f.pack()
f.display()
root.mainloop()