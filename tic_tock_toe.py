from tkinter import *
import numpy as np

root  = Tk()
root.resizable(0,0)
#   #   #
#   #   #
#########
#   #   #
#   #   # 
class Tick_Tack_Toe:
    def __init__(self):
        self.check_123=False
        self.matrix = np.array( [[0,0,0],
                       [0,0,0],
                       [0,0,0]])
        self.can =Canvas(root,width=600,height=600)
        self.can.pack()
        self.result_declare= False
        self.turn = "O" # for O = 1 for X = 2
        self.loc = [[5,5,200,200],[200,5,400,200],[400,5,600,200],[5,200,200,400],[200,200,400,400],
                    [400,200,600,400],[5,400,200,600],[200,400,400,600],[400,400,600,600]]
        self.First = self.can.create_rectangle(5,5,200,200,fill="white",width=2,tags="1")
        self.Sec = self.can.create_rectangle(200,5,400,200,fill="white",width=2,tags="2")
        self.third = self.can.create_rectangle(400,5,600,200,fill="white",width=2,tags="3")
        
        self.fourth = self.can.create_rectangle(5,200,200,400,fill="white",width=2,tags="4")
        self.five = self.can.create_rectangle(200,200,400,400,fill="white",width=2,tags="5")
        self.six = self.can.create_rectangle(400,200,600,400,fill="white",width=2,tags="6")
       
        self.seven = self.can.create_rectangle(5,400,200,600,fill="white",width=2,tags="7")
        self.eight = self.can.create_rectangle(200,400,400,600,fill="white",width=2,tags="8")        
        self.nine = self.can.create_rectangle(400,400,600,600,fill="white",width=2,tags="9")        
        self.mouse__click__event()
    def leftclick(self,event):
        if self.check_123:
            self.result_declare=False
            self.turn = "O"
           
            self.check_123=False
            
        if  self.result_declare:
            self.can.delete("new")
            self.check_123=True
            
            self.matrix = np.array( [[0,0,0],
                           [0,0,0],
                           [0,0,0]])
            
        if not self.result_declare:
            item_id = self.can.find_closest(event.x, event.y)[0]
            item_tags = self.can.gettags(item_id)
           
            squr = int(item_tags[0])
            loc=self.loc[squr-1]
            
            first = squr//3
            sec = squr%3
           
          
            i,j=0,0
            if first==0:
                if sec==0:
                    pass
                else:
                    i,j=0,sec-1
                    
            elif first==1:
                if sec==0:
                    i,j=0,2
                   
                else:
                    i,j=1,sec-1
                    
            else:   
                    if first==3:
                        i,j=2,2
                      
                    elif sec==0:
                        i,j=1,2
                       
                    else:
                        i,j=2,sec-1
                        
            
            if  self.matrix[i][j]:
                pass
                
            else:
                print(self.turn)
                if self.turn == "O":
                    self.matrix[i][j]=1
                    self.can.create_oval(loc[0]+20,loc[1]+20,loc[2]-20,loc[3]-20,width=2,tags='new')
                    self.turn = "X"      
                else:
                    self.matrix[i][j]=2
                    self.can.create_line(loc[0]+20,loc[1]+20,loc[2]-20,loc[3]-20,width=2,tags='new')
                    self.can.create_line(loc[0]+180,loc[1]+20,loc[2]-180,loc[3]-20,width=2,tags='new')
                    self.turn = "O"
            self.check_result()
    def check_result(self):
         if not self.result_declare:
            result = [0,0,0,0,0,0,0,0]
            if self.matrix[0][0]==self.matrix[0][1] and self.matrix[0][0]==self.matrix[0][2]:
                result[0]=self.matrix[0][0]
            if self.matrix[1][0]==self.matrix[1][1] and self.matrix[1][0]==self.matrix[1][2]:
                result[1]=self.matrix[1][0]
            if self.matrix[2][0]==self.matrix[2][1] and self.matrix[2][0]==self.matrix[2][2]:
                result[2]=self.matrix[2][0]
            
            if self.matrix[0][0]==self.matrix[1][0] and self.matrix[0][0]==self.matrix[2][0]:
                result[3]=self.matrix[0][0]
            if self.matrix[0][1]==self.matrix[1][1] and self.matrix[0][1]==self.matrix[2][1]:
               result[4]=self.matrix[0][1]
            if self.matrix[0][2]==self.matrix[1][2] and self.matrix[0][2]==self.matrix[2][2]:
                result[5]=self.matrix[0][2]
            
            if self.matrix[0][0]==self.matrix[1][1] and self.matrix[1][1]==self.matrix[2][2]:
                result[6]=self.matrix[0][0]
            if self.matrix[0][2]==self.matrix[1][1] and self.matrix[1][1]==self.matrix[2][0]:
                result[7]=self.matrix[0][2]
            for i in range(len(result)):
                if result[i]==1:
                    self.can.create_text(300,300,text="O is winner",font=('Helvetica 50 bold'),tags='new')
                    self.result_declare=True
                elif result[i]==2:
                    self.can.create_text(300,300,text="X is winner",font=('Helvetica 50 bold'),tags='new')
                    self.result_declare=True
            
            
            
            
    def mouse__click__event(self):
        pass
        root.bind("<Button-1>", self.leftclick)
        
        
        
        
Tick_Tack_Toe()
root.mainloop()