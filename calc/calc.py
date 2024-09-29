from tkinter import*
from tkinter.font import BOLD
first_no=sec_no=op=None


def getdigit(digit):
  current=result_label['text']
  new=current+str(digit)
  result_label.config(text=new)


def clear():
  result_label.config(text=" ")
def get_operator(operator):
  global first_no,op
  first_no=int(result_label['text'])
  op=operator
  result_label.config(text='')
 

def ans():
  global first_no,sec_no,op
  
  sec_no=int(result_label['text'])
  if op=="+":
    result_label.config(text=int(first_no)+int(sec_no))
  elif op=='-':
    result_label.config(text=int(first_no)-int(sec_no))
  elif op=="*":
    result_label.config(text=int(first_no)*int(sec_no))
  elif op=='÷':
    if sec_no==0:
      result_label.config(text="undefined")
    else:
      result_label.config(text=int(first_no)/int(sec_no))

root=Tk()
root.title("Calculator")
root.geometry("240x329")
root.resizable(0,0)

root.configure(background="#0A044B")
result_label=Label(root,text='',bg='#0A044B',fg='white')
result_label.grid(column=0,row=0,columnspan=4,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,BOLD))

btn7=Button(root,text="7",bg='#0A044B',fg="white",width='5',height='2',command=lambda:getdigit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("verdana",12))

btn8=Button(root,text="8",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("verdana",12))

btn9=Button(root,text="9",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("verdana",12))

btn_add=Button(root,text="+",bg='#0A044B',fg='white',width='5',height='2',command=lambda:get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=("verdana",12))



btn4=Button(root,text="4",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("verdana",12))

btn5=Button(root,text="5",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("verdana",12))

btn6=Button(root,text="6",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("verdana",12))

btn_sub=Button(root,text="-",bg='#0A044B',fg='white',width='5',height='2',command=lambda:get_operator("-"))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=("verdana",12))




btn1=Button(root,text="1",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("verdana",12))

btn2=Button(root,text="2",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("verdana",12))

btn3=Button(root,text="3",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("verdana",12))

btn_mul=Button(root,text="x",bg='#0A044B',fg='white',width='5',height='2',command=lambda:get_operator("*"))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=("verdana",12))



btn_clr=Button(root,text="C",bg='#0A044B',fg='white',width='5',height='2',command=lambda:clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=("verdana",12))

btn0=Button(root,text="0",bg='#0A044B',fg='white',width='5',height='2',command=lambda:getdigit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("verdana",12))

btn_equal=Button(root,text="=",bg='#16E8F0',fg='white',width='5',height='2',command=ans)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=("verdana",12))

btn_div=Button(root,text="÷",bg='#0A044B',fg='white',width='5',height='2',command=lambda:get_operator("÷"))
btn_div.grid(row=4,column=3)
btn_div.config(font=("verdana",12))




root.mainloop()


        

