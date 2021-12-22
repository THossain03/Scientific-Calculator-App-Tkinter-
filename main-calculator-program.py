from tkinter import *
import math

board = Tk()
board.title("Scientific Calculator")
board.configure(bg='#6f9656')

#global access
operator = ""
text_Input = StringVar()
text_Input2 = DoubleVar()
previousAns = ""
mode_degree = True
n=0

#main text input
txt = Entry(board, width=70, borderwidth=10, font='bold', bg='#ffffff', textvariable=text_Input, justify='right')
txt.grid(row=0,column=0, columnspan=5, padx=10, pady=10)  

def button_click(operation):
    global operator
    global mode_degree
    global n
    if (operation == "absolute value"):
        text_Input.set("|" + operator + "|")
        operator = "abs(" + operator + ")"
    elif (operation == "math.pi"):
        if (len(operator)>0):
            if (operator[len(operator)-1] == "+" or operator[len(operator)-1] == "-" or operator[len(operator)-1] == "/" or operator[len(operator)-1] == "*"):
                operator = operator + str(operation)
                text_Input.set(text_Input.get() + "π")
            else:
                operator = operator + "*" + str(operation)
                text_Input.set(text_Input.get() + "*π")
        else:
            operator = str(operation)
            text_Input.set("π")
    elif (operation == "math.e"):
        if (len(operator)>0):
            if (operator[len(operator)-1] == "+" or operator[len(operator)-1] == "-" or operator[len(operator)-1] == "/" or operator[len(operator)-1] == "*"):
                operator = operator + str(operation)
                text_Input.set(text_Input.get() + "e")
            else:
                operator = operator + "*" + str(operation)
                text_Input.set(text_Input.get() + "*e")
        else:
            operator = str(operation)
            text_Input.set("e")
    elif (operation == "math.factorial"):
        if (len(operator)>0):
            if (operator[len(operator)-1] == "0" or operator[len(operator)-1] == "1" or operator[len(operator)-1] == "2" or operator[len(operator)-1] == "3" or operator[len(operator)-1] == "4" or operator[len(operator)-1] == "5" or operator[len(operator)-1] == "6" or operator[len(operator)-1] == "7" or operator[len(operator)-1] == "8" or operator[len(operator)-1] == "9" or operator[len(operator)-1] == ")" or operator[len(operator)-1] == "i" or operator[len(operator)-1] == "|" or operator[len(operator)-1] == "e"):
                operator = str(operation) + "(" + operator + ")"
                text_Input.set("(" + text_Input.get() + ")!")
    elif (operation == "math.sin"):
        if (mode_degree):
            operator = str(operation) + "(math.radians(" + operator +"))"
            text_Input.set("sin(" + text_Input.get() + ")")
        else:
            operator = str(operation) + "(" + operator +")"
            text_Input.set("sin(" + text_Input.get() + ")")
    elif (operation == "math.cos"):
        if (mode_degree):
            operator = str(operation) + "(math.radians(" + operator +"))"
            text_Input.set("cos(" + text_Input.get() + ")")
        else:
            operator = str(operation) + "(" + operator +")"
            text_Input.set("cos(" + text_Input.get() + ")")
    elif (operation == "math.tan"):
        if (mode_degree):
            operator = str(operation) + "(math.radians(" + operator +"))"
            text_Input.set("tan(" + text_Input.get() + ")")
        else:
            operator = str(operation) + "(" + operator +")"
            text_Input.set("tan(" + text_Input.get() + ")")
    elif (operation == "math.asin"):
        if (mode_degree):
            operator = "math.degrees(" + str(operation) + "(" + operator +"))"
            text_Input.set("asin(" + text_Input.get() + ")")
        else:
            operator = str(operation) + "(" + operator +")"
            text_Input.set("asin(" + text_Input.get() + ")")
    elif (operation == "math.acos"):
        if (mode_degree):
            operator = "math.degrees(" + str(operation) + "(" + operator +"))"
            text_Input.set("acos(" + text_Input.get() + ")")
        else:
            operator = str(operation) + "(" + operator +")"
            text_Input.set("acos(" + text_Input.get() + ")")
    elif (operation == "math.atan"):
        if (mode_degree):
            operator = "math.degrees(" + str(operation) + "(" + operator +"))"
            text_Input.set("atan(" + text_Input.get() + ")")
        else:
            operator = str(operation) + "(" + operator +")"
            text_Input.set("atan(" + text_Input.get() + ")")
    elif (operation == "math.pow(2)"):
        if(len(operator)>0):
            if(operator[len(operator)-1] == "0" or operator[len(operator)-1] == "1" or operator[len(operator)-1] == "2" or operator[len(operator)-1] == "3" or operator[len(operator)-1] == "4" or operator[len(operator)-1] == "5" or operator[len(operator)-1] == "6" or operator[len(operator)-1] == "7" or operator[len(operator)-1] == "8" or operator[len(operator)-1] == "9" or operator[len(operator)-1] == ")" or operator[len(operator)-1] == "|" or operator[len(operator)-1] == "e" or operator[len(operator)-1] == "i"):
                operator = "math.pow(" + operator + ",2)"
                text_Input.set("(" + text_Input.get() + ")\u00B2")
    elif (operation == "math.sqrt"):
        operator = str(operation) + "(" + text_Input.get() + ")"
        text_Input.set("√(" + text_Input.get() + ")")
    elif (operation == "math.pow(n)"):
        entering_n_input()
        if(len(operator)>0):
            if(operator[len(operator)-1] == "0" or operator[len(operator)-1] == "1" or operator[len(operator)-1] == "2" or operator[len(operator)-1] == "3" or operator[len(operator)-1] == "4" or operator[len(operator)-1] == "5" or operator[len(operator)-1] == "6" or operator[len(operator)-1] == "7" or operator[len(operator)-1] == "8" or operator[len(operator)-1] == "9" or operator[len(operator)-1] == ")" or operator[len(operator)-1] == "|" or operator[len(operator)-1] == "e" or operator[len(operator)-1] == "i"):
                operator = "math.pow(" + operator + "," +str(n) + ")"
                string__1 = "(" + text_Input.get() + ")"
                if (n<0.0):
                    n = (-1)*n
                    string__1 = string__1 + "\u207B"
                while (n != 0):
                    temp = n%10
                    n = n/10
                    if (temp == 0):
                        string__1 = string__1 + "\u2070"
                    elif (temp == 1):
                        string__1 = string__1 + "\u00B9"
                    elif (temp == 2):
                        string__1 = string__1 + "\u00B2"
                    elif (temp ==3):
                        string__1 = string__1 + "\u00B3"
                    elif (temp==4):
                        string__1 = string__1 + "\u2074"
                    elif (temp==5):
                        string__1 = string__1 + "\u2075"
                    elif (temp==6):
                        string__1 = string__1 + "\u2076"
                    elif (temp==7):
                        string__1 = string__1 + "\u2077"
                    elif (temp==8):
                        string__1 = string__1 + "\u2078"
                    elif (temp==9):
                        string__1 = string__1 + "\u2079"
                text_Input.set(string__1)
    elif (operation == "math.pow(1/n)"):
        entering_n_input()
        if(len(operator)>0):
            if(operator[len(operator)-1] == "0" or operator[len(operator)-1] == "1" or operator[len(operator)-1] == "2" or operator[len(operator)-1] == "3" or operator[len(operator)-1] == "4" or operator[len(operator)-1] == "5" or operator[len(operator)-1] == "6" or operator[len(operator)-1] == "7" or operator[len(operator)-1] == "8" or operator[len(operator)-1] == "9" or operator[len(operator)-1] == ")" or operator[len(operator)-1] == "|" or operator[len(operator)-1] == "e" or operator[len(operator)-1] == "i"):
                if (n > 0.0):
                    operator = "math.pow(" + operator + ",1/" +str(n) + ")"
                    text_Input.set("(" + str(n) + ")√(" + text_Input.get() + ")")
    elif (operation == "math.log10"):
        if(len(operator)>0):
            operator = str(operation) + "(" + operator + ")"
            text_Input.set("log(" + text_Input.get() + ")")
        else:
            operator = "math.log10(0)"
            text_Input.set("log(0)")
    elif (operation == "math.log"):
        if(len(operator)>0):
            operator = str(operation) + "(" + operator + ")"
            text_Input.set("ln(" + text_Input.get() + ")")
        else:
            operator = "math.log(0)"
            text_Input.set("ln(0)")
    elif (operation == "math.floor"):
        if(len(operator)>0):
            operator = str(operation) + "(" + operator + ")"
            text_Input.set("⌊" + text_Input.get() + "⌋")
        else:
            operator = "math.floor(0)"
            text_Input.set("⌊0⌋")
    elif (operation == "math.ceil"):
        if(len(operator)>0):
            operator = str(operation) + "(" + operator + ")"
            text_Input.set("⌈" + text_Input.get() + "⌉")
        else:
            operator = "math.ceil(0)"
            text_Input.set("⌈0⌉")
    else:
        operator = operator + str(operation)
        text_Input.set(text_Input.get() + str(operation))
    
def send_back_n(input):
    global n
    n=input
    return

def entering_n_input():   #ENTRY CHANGE REQUIRED (do it on main screen instead)
    new_window = Tk()
    new_window.title("Enter n")
    myLbl = Label(new_window, text="Enter an independent value n:").pack()
    n_input = Entry(new_window,textvariable=text_Input2, justify='right').pack()
    continue_btn = Button(new_window, text="Set this n value", command=lambda: send_back_n(text_Input2)).pack()
    new_window.mainloop()
    

def delete_button_click():
    global operator
    if (len(operator)>0 and "math.pi" in operator):
        operator = operator[:-6]
    elif (len(operator)>0 and "math.e" in operator):
        operator = operator[:-5]        
    if (len(operator) != 0): 
        operator = operator[:-1]
    text_Input.set(operator)                

def clear_it():
    global operator
    operator = ""
    text_Input.set("")
  
def calculate_it():
    global operator
    global previousAns
    try:
        answer=str(eval(operator))
    except:
        answer="Error"
    text_Input.set(answer)
    if(answer != "Error"):
        previousAns = answer
        operator=answer 
    else:
        previousAns=""
        operator=""

def reciprocal ():
    global operator
    global previousAns
    try:
        answer=str(1/(eval(txt.get())))
    except:
        answer="Error"
    text_Input.set(answer)
    if(answer != "Error"):
        previousAns = answer
        operator=answer 
    else:
        previousAns=""
        operator=""

def base_10 ():
    global operator
    global previousAns
    try:
        answer=str(pow(10,(eval(txt.get()))))
    except:
        answer="Error"
    text_Input.set(answer)
    if(answer != "Error"):
        previousAns = answer
        operator=answer 
    else:
        previousAns=""
        operator=""
        
def deg_rad ():
    global mode_degree
    if (mode_degree):
        mode_degree = False
        button_degree_or_radian.config(text="Rad", command=deg_rad)
    else:
        mode_degree = True
        button_degree_or_radian.config(text="Deg", command=deg_rad)

#keyboard usage to calculate (only active if equal key is pressed)
def key_use(a):
    global operator
    global previousAns
    try:
        answer=str(eval(txt.get()))
    except:
        answer="Error"
    text_Input.set(answer)
    if(answer != "Error"):
        previousAns = answer
        operator=answer 
    else:
        previousAns=""
        operator=""

board.bind('<Return>', key_use)
    
#grid layout for buttons
button_1 = Button(board, text="1", font=20, width=14, command=lambda: button_click("1"))
button_2 = Button(board, text="2", font=20, width=14, command=lambda: button_click("2"))
button_3 = Button(board, text="3", font=20, width=14, command=lambda: button_click("3"))
button_4 = Button(board, text="4", font=20, width=14, command=lambda: button_click("4"))
button_5 = Button(board, text="5", font=20, width=14, command=lambda: button_click("5"))
button_6 = Button(board, text="6", font=20, width=14, command=lambda: button_click("6"))
button_7 = Button(board, text="7", font=20, width=14, command=lambda: button_click("7"))
button_8 = Button(board, text="8", font=20, width=14, command=lambda: button_click("8"))
button_9 = Button(board, text="9", font=20, width=14, command=lambda: button_click("9"))
button_0 = Button(board, text="0", font=20, width=14, command=lambda: button_click("0"))
button_plus = Button(board, text="+", font=20, width=14, command=lambda: button_click("+"))
button_minus = Button(board, text="-", font=28, width=14, command=lambda: button_click("-"))
button_multiply = Button(board, text="x", font=20, width=14, command=lambda: button_click("*"))
button_divide = Button(board, text="÷", font=28, width=14, command=lambda: button_click("/"))
button_brack_open = Button(board, text="(", font=28, width=14, command=lambda: button_click("("))
button_brack_close = Button(board, text=")", font=28, width=14, command=lambda: button_click(")"))
button_decimal = Button(board, text=".", font=50, width=14, command=lambda: button_click("."))
button_access_ANS = Button(board, text="ANS", font=28, width=14, command=lambda: button_click(previousAns))
button_equal = Button(board, text="=", font=20, width=14, command=calculate_it)
button_clear = Button(board, text="C", font=16, width=14, command=clear_it)
button_delete = Button(board, text="DEL", font=28, width=14, command=delete_button_click)
button_reciprocal = Button(board, text="1/n", font=28, width=14, command=reciprocal)
button_10_exp = Button(board, text="10\u207f", font=28, width=14, command=base_10)
button_abs = Button(board, text="|n|", font=28, width=14, command=lambda: button_click("absolute value"))
button_pi = Button(board, text="π", font=28, width=14, command=lambda: button_click("math.pi"))
button_e = Button(board, text="e", font=28, width=14, command=lambda: button_click("math.e"))
button_factorial = Button(board, text="n!", font=28, width=14, command=lambda: button_click("math.factorial"))
button_modulus = Button(board, text="Mod", font=28, width=14, command=lambda: button_click("%"))
button_sine = Button(board, text="sin(n)", font=28, width=14, command=lambda: button_click("math.sin"))
button_cosine = Button(board, text="cos(n)", font=28, width=14, command=lambda: button_click("math.cos"))
button_tan = Button(board, text="tan(n)", font=28, width=14, command=lambda: button_click("math.tan"))
button_arcsine = Button(board, text="sin\u207b\u00B9(n)", font=28, width=14, command=lambda: button_click("math.asin"))
button_arccosine = Button(board, text="cos\u207b\u00B9(n)", font=28, width=14, command=lambda: button_click("math.acos"))
button_arctan = Button(board, text="tan\u207b\u00B9(n)", font=28, width=14, command=lambda: button_click("math.atan"))
button_squared = Button(board, text="n\u00B2", font=28, width=14, command=lambda: button_click("math.pow(2)"))
button_squareRoot = Button(board, text="√n", font=28, width=14, command=lambda: button_click("math.sqrt"))
button_nth_exponent = Button(board, text="x\u207f", font=28, width=14, command=lambda: button_click("math.pow(n)"))
button_nth_root = Button(board, text="(n)√x", font=28, width=14, command=lambda: button_click("math.pow(1/n)"))
button_log = Button(board, text="log", font=28, width=14, command=lambda: button_click("math.log10"))
button_ln = Button(board, text="ln", font=28, width=14, command=lambda: button_click("math.log"))
button_floor = Button(board, text="⌊x⌋", font=28, width=14, command=lambda: button_click("math.floor"))
button_ceiling = Button(board, text="⌈x⌉", font=28, width=14, command=lambda: button_click("math.ceil"))

button_degree_or_radian = Button(board, text="Deg", font=('arial',16,'bold'), width=14, command=deg_rad)


#-------------------------------------------------------------
button_access_ANS.grid(row=1, column=0)
button_brack_open.grid(row=1,column=1)
button_brack_close.grid(row=1, column=2)
button_plus.grid(row=1,column=3)
#------------------------------------------------------------
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_minus.grid(row=2,column=3)
#-------------------------------------------------------------
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_multiply.grid(row=3,column=3)
#-------------------------------------------------------------
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_divide.grid(row=4,column=3)
#--------------------------------------------------------------
button_clear.grid(row=5,column=0)
button_0.grid(row=5,column=1)
button_decimal.grid(row=5, column=2)
button_equal.grid(row=5,column=3)
#-------------------------------------------------------------
#To-Add:
button_delete.grid(row=6, column=0)
button_reciprocal.grid(row=6, column=1)
button_10_exp.grid(row=6,column=3)
button_abs.grid(row=6, column=2)
button_pi.grid(row=7, column=0)
button_e.grid(row=7,column=1)
button_factorial.grid(row=7, column=2)
button_modulus.grid(row=7,column=3)
button_degree_or_radian.grid(row=8,column=0,columnspan=4)
button_sine.grid(row=9,column=0)
button_cosine.grid(row=9, column=1)
button_tan.grid(row=9, column=2)
button_arcsine.grid(row=10, column=0)
button_arccosine.grid(row=10, column=1)
button_arctan.grid(row=10, column=2)
button_squared.grid(row=6,column=6)
button_squareRoot.grid(row=6,column=7)
button_nth_exponent.grid(row=7,column=6)
button_nth_root.grid(row=7,column=7)
button_log.grid(row=8, column=6)
button_ln.grid(row=8, column=7)
button_ceiling.grid(row=9,column=6)
button_floor.grid(row=9,column=7)


board.mainloop()