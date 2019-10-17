import tkinter as tk
from tkinter.messagebox import showinfo
screen_width=700
screen_height=700
screen=tk.Tk()
flag=0
butt=0
button_list=[]
score =[100+x for x in range(9)]
class button:
    global button_list
    def __init__(self,screen,r,c):
        self.frame = tk.Frame(screen, width=screen_width/3, height=screen_height/3)
        self.button= tk.Button(self.frame,font=('Arial',100),command=lambda:click(self.button))
        self.frame.grid_propagate(False)
        self.frame.columnconfigure(0, weight=2)
        self.frame.rowconfigure(0,weight=2)
        self.frame.grid(row=r, column=c)
        self.button.grid(sticky="wens")
        button_list.append(self.button)

def restart(input):
    if input==1:
        MsgBox = tk.messagebox.askquestion ('Restart','Player 1 wins, restart?',icon = 'warning')
    elif input==2:
        MsgBox = tk.messagebox.askquestion ('Restart','Player 2 wins, restart?',icon = 'warning')
    elif input==0:
        MsgBox = tk.messagebox.askquestion ('Restart','DRAW!!!!!!, restart?',icon = 'warning')

    if MsgBox == 'yes':
       main()
    else:
        screen.destroy()

def click(button_instance):
    global flag,button_list,score
    if flag%2==1:
        score[button_list.index(button_instance)]=-1
        button_instance.config(text="X",state="disabled",bg="white",disabledforeground="red")
    else:
         score[button_list.index(button_instance)]=1
         button_instance.config(text="O",state="disabled",bg="white",disabledforeground="blue")
    flag+=1

    check()

def state_all():
    global button_list
    if button_list[0]['state']==button_list[1]['state']==button_list[2]['state']==button_list[3]['state']==button_list[4]['state']==button_list[5]['state']==button_list[6]['state']==button_list[7]['state']==button_list[8]['state']:
        return True
    else: return False

def check():
    global score,button_list
    if score[0]+score[1]+score[2]==3 or score[0]+score[3]+score[6]==3 or score[0]+score[4]+score[8]==3 or score[2]+score[4]+score[6]==3 or score[3]+score[4]+score[5]==3 or score[6]+score[7]+score[8]==3 or score[1]+score[4]+score[7]==3 or score[2]+score[5]+score[8]==3:
        restart(1)
    elif score[0]+score[1]+score[2]==-3 or score[0]+score[3]+score[6]==-3 or score[0]+score[4]+score[8]==-3 or score[2]+score[4]+score[6]==-3 or score[3]+score[4]+score[5]==-3 or score[6]+score[7]+score[8]==-3 or score[1]+score[4]+score[7]==-3 or score[2]+score[5]+score[8]==-3:
        restart(2)
    elif (score[0]+score[1]+score[2]!=3 or score[0]+score[3]+score[6]!=3 or score[0]+score[4]+score[8]!=3 or score[2]+score[4]+score[6]!=3 or score[3]+score[4]+score[5]!=3 or score[6]+score[7]+score[8]!=3 or score[1]+score[4]+score[7]!=3 or score[2]+score[5]+score[8]!=3) and state_all():
        restart(0)
    elif (score[0]+score[1]+score[2]!=-3 or score[0]+score[3]+score[6]!=-3 or score[0]+score[4]+score[8]!=-3 or score[2]+score[4]+score[6]!=-3 or score[3]+score[4]+score[5]!=-3 or score[6]+score[7]+score[8]!=-3 or score[1]+score[4]+score[7]!=-3 or score[2]+score[5]+score[8]!=-3) and state_all():
        restart(0)

def main():
    global button_list,score
    button_list.clear()
    score=[100+x for x in range(9)]
    for i in range(0,3):
        for j in range(0,3):
            button(screen,i,j)

    screen.mainloop()

if __name__=='__main__':
    main()
