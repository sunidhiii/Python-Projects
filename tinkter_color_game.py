
import tkinter 
import random 
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 30
  
def startGame(event): 
      
    if timeleft == 30: 
        countdown() 
          
   
    nextColour() 
  

def nextColour(): 
    global score 
    global timeleft 
  
    if timeleft > 0: 
        # make the text entry box active. 
        e.focus_set() 
  
        if e.get().lower() == colours[1].lower(): 
            score += 1
  
        # clear the text entry box. 
        e.delete(0, tkinter.END) 
          
        random.shuffle(colours) 
        label.config(fg = str(colours[1]), text = str(colours[0])) 
        scoreLabel.config(text = "Score: " + str(score)) 
  
  
def countdown(): 
    global timeleft 
  
    if timeleft > 0: 
        timeleft -= 1
        timeLabel.config(text = "Time left: " +str(timeleft)) 
        timeLabel.after(1000, countdown) 
  
  

root = tkinter.Tk() 
root.title("COLORGAME") 
root.geometry("600x350") 
instructions = tkinter.Label(root, text = "Type the colour of the word", font = ('Helvetica', 32), fg = "Brown",background='pink') 
instructions.pack()  
  
root.configure(background='pink')

scoreLabel = tkinter.Label(root, text = "Press enter to start", font = ('Helvetica', 32), fg = "black",background='pink') 
scoreLabel.pack() 
  
 
timeLabel = tkinter.Label(root, text = "Time left: " +str(timeleft), font = ('Helvetica', 32), fg = "Green",background='pink') 
timeLabel.pack() 
  

label = tkinter.Label(root, font = ('Helvetica', 70), fg = "Black",background='pink') 
label.pack()


  
# add a text entry box for typing colours
e = tkinter.Entry(root , font = ('Helvetica', 30)) 
  
# run the 'startGame' function when enter key is pressed
root.bind('<Return>', startGame) 
e.pack() 
  
# set focus on the entry box 
e.focus_set() 
  
# start the GUI 
root.mainloop()
