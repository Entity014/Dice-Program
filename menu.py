import tkinter as tk
import time
from PIL import ImageTk, Image, ImageSequence
import random

class Base(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('500x500')
        self.title('Menu')
        container = tk.Frame(self)
        
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        self.job = [ImageTk.PhotoImage(Image.open('Class/BackCard.jpg').resize((200,300))),ImageTk.PhotoImage(Image.open('Class/Berserker.jpg').resize((200,300))),
                    ImageTk.PhotoImage(Image.open('Class/Knight.jpg').resize((200,300))), ImageTk.PhotoImage(Image.open('Class/Ninja.jpg').resize((200,300))), 
                    ImageTk.PhotoImage(Image.open('Class/Pirate.jpg').resize((200,300))), Image.open("Class/tenor.gif")]
        
        self.image_4 = [ImageTk.PhotoImage(Image.open("Dice/Dice4/1.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice4/2.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice4/3.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice4/4.jpg").resize((100,100))),
        Image.open("Dice/Dice4/1-4.gif")]
        
        self.image_6 = [ImageTk.PhotoImage(Image.open("Dice/Dice6/1.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice6/2.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice6/3.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice6/4.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice6/5.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice6/6.jpg").resize((100,100))),
        Image.open("Dice/Dice6/1-6.gif")]
        
        self.image_10 = [ImageTk.PhotoImage(Image.open("Dice/Dice10/1.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice10/2.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice10/3.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice10/4.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice10/5.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice10/6.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice10/7.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice10/8.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice10/9.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice10/10.jpg").resize((100,100))),
        Image.open("Dice/Dice10/1-10.gif")]
        
        self.image_20 = [ImageTk.PhotoImage(Image.open("Dice/Dice20/1.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/2.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/3.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/4.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/5.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/6.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/7.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/8.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/9.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/10.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/11.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/12.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/13.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/14.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/15.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/16.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/17.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/18.jpg").resize((100,100))),
        ImageTk.PhotoImage(Image.open("Dice/Dice20/19.jpg").resize((100,100))), ImageTk.PhotoImage(Image.open("Dice/Dice20/20.jpg").resize((100,100))),
        Image.open("Dice/Dice20/1-20.gif")]
        
        for F in (Main, Dice_4, Dice_6, Dice_10, Dice_20):
            
            frame = F(container, self)
            self.frames[F] =frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame(Main)
        
    def show_frame(self, cont):
         
        frame = self.frames[cont]
        frame.tkraise()
    
    def dice_roll(self, img):
        self.dice_num = -1
        self.dice = []
        self.dice_max = tk.IntVar()
        
        for x in range(0, 9):
            self.dice_num += 1
            self.dice.append(tk.Label(self, image = img[0]))
            #print(self.dice)
            self.dice[self.dice_num].place(x=100 + ((x % 3)*150), y=140 + ((x // 3) * 120), anchor='center')
    
    def on_click(self, label):
        for x in range(len(self.dice)):
            self.dice[x].after(10, self.dice[x].destroy())
            label.config(text='')
    
    def hide_button(self):
        for x in range(len(self.skill)):
            self.skill[x].place_forget()
    
    def show_button(self):
        for x in range(len(self.skill)):
            self.skill[x].place(x=450, y=50 + (x*50), anchor='center')
    
    def rd(self, img, label, a: int,b :int):
        self.d = []
        for x in range(len(self.dice)):
            self.d.append(random.randint(a,b))
        result = sum(self.d)
        for i in ImageSequence.Iterator(img[len(img)-1]):
            self.gif_resize = img[len(img)-1].resize((100,100))
            self.gif = ImageTk.PhotoImage(self.gif_resize)
            label.config(text="")
            for x in range(len(self.dice)):
                self.dice[x].configure(image = self.gif)
            self.update()
            time.sleep(0.1)
        for x in range(len(self.dice)):
            print(self.d[x])
            #self.change_pic(img, self.d[x], self.dice[x])
            self.dice[x].config(image= img[self.d[x]-1])
            time.sleep(0.015)
        label.config(text=str(result))
    
    def rd_job(self, img, label, button):
        self.skill_num = -1
        self.skill = []
        self.num_job = random.randint(2,len(self.job))    
        for i in ImageSequence.Iterator(img[len(img)-1]):
            self.gif_resize = img[len(img)-1].resize((200,300))
            self.gif = ImageTk.PhotoImage(self.gif_resize)
            label.configure(image = self.gif)
            self.update()
            time.sleep(0.06)
        label.config(image= img[self.num_job-1])
        for x in range(0, 4):
            self.skill_num += 1
            self.skill.append(tk.Button(self, text='Skill ' + str(x), height=1, width=10, command=None))
            self.skill[self.skill_num].place(x=450, y=50 + (x*50), anchor='center')
        #print(self.num_job)
        #button['state'] = tk.DISABLED
        button.destroy()
        
        

class Main(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg='black')
        
        label = tk.Label(self, text='Profile', font=('Calibri 15 bold'), bg = 'black', fg='white')
        label.pack(padx=10, pady=10)
        image = tk.Label(self, image = controller.job[0])
        image.place(x=250, y=200, anchor='center')
        
        Dice4 = tk.Button(self, text='Dice 4', height=1, width=10, command=lambda: [controller.show_frame(Dice_4),controller.dice_roll(controller.image_4),controller.hide_button()])
        Dice4.place(x=50, y=50, anchor='center')
        Dice6 = tk.Button(self, text='Dice 6', height=1, width=10, command=lambda: [controller.show_frame(Dice_6),controller.dice_roll(controller.image_6),controller.hide_button()])
        Dice6.place(x=50, y=100, anchor='center')
        Dice10 = tk.Button(self, text='Dice 10', height=1, width=10, command=lambda: [controller.show_frame(Dice_10),controller.dice_roll(controller.image_10),controller.hide_button()])
        Dice10.place(x=50, y=150, anchor='center')
        Dice20 = tk.Button(self, text='Dice 20', height=1, width=10, command=lambda: [controller.show_frame(Dice_20),controller.dice_roll(controller.image_20),controller.hide_button()])
        Dice20.place(x=50, y=200, anchor='center')
        job = tk.Button(self, text='Class', height=1, width=10, command=lambda: controller.rd_job(controller.job, image, job))
        job.place(x=50, y=250, anchor='center')

class Dice_4(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        label = tk.Label(self, text='Dice 4', font=('Calibri 15 bold'))
        label.pack(padx=10, pady=10)
        text_sum = tk.Label(self, text='',font=('Calibri 15 bold'), bg='white')
        text_sum.place(x=250, y=460, anchor='center')
        
        button = tk.Button(self, text='Menu', height=1, width=10, command=lambda: [controller.show_frame(Main), controller.on_click(text_sum), controller.show_button()], bg = 'red')
        button.pack()
        button_random = tk.Button(self, text = 'Random', height=1, width=10, command = lambda: controller.rd(controller.image_4, text_sum,1,4), bg = 'green')
        button_random.place(x=400, y=460, anchor='center')

class Dice_6(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        label = tk.Label(self, text='Dice 6', font=('Calibri 15 bold'))
        label.pack(padx=10, pady=10)
        text_sum = tk.Label(self, text='',font=('Calibri 15 bold'), bg='white')
        text_sum.place(x=250, y=460, anchor='center')
        
        button = tk.Button(self, text='Menu', height=1, width=10, command=lambda: [controller.show_frame(Main), controller.on_click(text_sum), controller.show_button()], bg = 'red')
        button.pack()
        button_random = tk.Button(self, text = 'Random', height=1, width=10, command = lambda: controller.rd(controller.image_6, text_sum,1,6), bg = 'green')
        button_random.place(x=400, y=460, anchor='center')

class Dice_10(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        label = tk.Label(self, text='Dice 10', font=('Calibri 15 bold'))
        label.pack(padx=10, pady=10)
        text_sum = tk.Label(self, text='',font=('Calibri 15 bold'), bg='white')
        text_sum.place(x=250, y=460, anchor='center')
        
        button = tk.Button(self, text='Menu', height=1, width=10, command=lambda: [controller.show_frame(Main), controller.on_click(text_sum), controller.show_button()], bg = 'red')
        button.pack()
        button_random = tk.Button(self, text = 'Random', height=1, width=10, command = lambda: controller.rd(controller.image_10, text_sum,1,10), bg = 'green')
        button_random.place(x=400, y=460, anchor='center')

class Dice_20(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        
        label = tk.Label(self, text='Dice 20', font=('Calibri 15 bold'))
        label.pack(padx=10, pady=10)
        text_sum = tk.Label(self, text='',font=('Calibri 15 bold'), bg='white')
        text_sum.place(x=250, y=460, anchor='center')
        
        button = tk.Button(self, text='Menu', height=1, width=10, command=lambda: [controller.show_frame(Main), controller.on_click(text_sum), controller.show_button()], bg = 'red')
        button.pack()
        button_random = tk.Button(self, text = 'Random', height=1, width=10, command = lambda: controller.rd(controller.image_20, text_sum,1,20), bg = 'green')
        button_random.place(x=400, y=460, anchor='center')

app = Base()
app.mainloop()
