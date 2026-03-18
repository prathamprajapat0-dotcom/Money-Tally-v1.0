import tkinter as tk 
root = tk.Tk()

SWIDTH = root.winfo_screenwidth()
SHEIGHT = root.winfo_screenheight()
BG = "lightblue"
Title = root.title("Money tally")
root.geometry(f"{SWIDTH}x{SHEIGHT}")
root.config(bg=BG )


STL = tk.Label(text="Enter \n \nthe \n \nmoney \n \nyou \n \nhave \n \nas \n \nper \n \nthe \n \nnumber \n \nof \n \nnotes:", font=("Arial", 30), bg=BG)
STL.place(x=SWIDTH//2-650, y=SHEIGHT//11-80)

E500N = tk.Entry(font=("Arial", 15))
E500N.place(x=SWIDTH//2, y=SHEIGHT//11-80)

L500N = tk.Label(text="Number of ₹500 notes", font=("Arial", 20), bg=BG)
L500N.place(x=SWIDTH//2-300, y=SHEIGHT//11-80)

T500N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T500N.place(x=SWIDTH//2+400, y=SHEIGHT//11-80)

E200N = tk.Entry(font=("Arial", 15))
E200N.place(x=SWIDTH//2, y=SHEIGHT//11)

L200N = tk.Label(text="Number of ₹200 notes", font=("Arial", 20), bg=BG)
L200N.place(x=SWIDTH//2-300, y=SHEIGHT//11)

T200N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T200N.place(x=SWIDTH//2+400, y=SHEIGHT//11)

E100N = tk.Entry(font=("Arial", 15))
E100N.place(x=SWIDTH//2, y=SHEIGHT//11+100)

L100N = tk.Label(text="Number of ₹100 notes", font=("Arial", 20), bg=BG)
L100N.place(x=SWIDTH//2-300, y=SHEIGHT//11+100)

T100N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T100N.place(x=SWIDTH//2+400, y=SHEIGHT//11+100)

E50N = tk.Entry(font=("Arial", 15))
E50N.place(x=SWIDTH//2, y=SHEIGHT//11+200)

L50N = tk.Label(text="Number of ₹50 notes", font=("Arial", 20), bg=BG)
L50N.place(x=SWIDTH//2-300, y=SHEIGHT//11+200)

T50N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T50N.place(x=SWIDTH//2+400, y=SHEIGHT//11+200)

E20N = tk.Entry(font=("Arial", 15))
E20N.place(x=SWIDTH//2, y=SHEIGHT//11+300)

L20N = tk.Label(text="Number of ₹20 notes", font=("Arial", 20), bg=BG)
L20N.place(x=SWIDTH//2-300, y=SHEIGHT//11+300)

T20N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T20N.place(x=SWIDTH//2+400, y=SHEIGHT//11+300)

E10N = tk.Entry(font=("Arial", 15))
E10N.place(x=SWIDTH//2, y=SHEIGHT//11+400)

L10N = tk.Label(text="Number of ₹10 notes", font=("Arial", 20), bg=BG)
L10N.place(x=SWIDTH//2-300, y=SHEIGHT//11+400)

T10N = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T10N.place(x=SWIDTH//2+400, y=SHEIGHT//11+400)

E10C = tk.Entry(font=("Arial", 15))
E10C.place(x=SWIDTH//2, y=SHEIGHT//11+500)

L10C = tk.Label(text="Number of ₹10 coins", font=("Arial", 20), bg=BG)
L10C.place(x=SWIDTH//2-300, y=SHEIGHT//11+500)

T10C = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T10C.place(x=SWIDTH//2+400, y=SHEIGHT//11+500)

E5C = tk.Entry(font=("Arial", 15))
E5C.place(x=SWIDTH//2, y=SHEIGHT//11+600)

L5C = tk.Label(text="Number of ₹5 coins", font=("Arial", 20), bg=BG)
L5C.place(x=SWIDTH//2-300, y=SHEIGHT//11+600)

T5C = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T5C.place(x=SWIDTH//2+400, y=SHEIGHT//11+600)

E2C = tk.Entry(font=("Arial", 15))
E2C.place(x=SWIDTH//2, y=SHEIGHT//11+700)

L2C = tk.Label(text="Number of ₹2 coins", font=("Arial", 20), bg=BG)
L2C.place(x=SWIDTH//2-300, y=SHEIGHT//11+700)

T2C = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T2C.place(x=SWIDTH//2+400, y=SHEIGHT//11+700)

E1C = tk.Entry(font=("Arial", 15))
E1C.place(x=SWIDTH//2, y=SHEIGHT//11+800)

L1C = tk.Label(text="Number of ₹1 coins", font=("Arial", 20), bg=BG)
L1C.place(x=SWIDTH//2-300, y=SHEIGHT//11+800)

T1C = tk.Label(text="=  ₹0", font=("Arial", 20), bg=BG)
T1C.place(x=SWIDTH//2+400, y=SHEIGHT//11+800)

GB = tk.Button(text="Get total", font=("Arial", 20), command=lambda: get_total(), bg=BG)
GB.place(x=SWIDTH//2+600, y=SHEIGHT//2)

TA = tk.Label(text="Total amount: ₹0", font=("Arial", 30), bg=BG)
TA.place(x=SWIDTH//2+500, y=SHEIGHT//2+100)

def get_total():
    try:
        N500 = int(E500N.get())
        N200 = int(E200N.get())
        N100 = int(E100N.get())
        N50 = int(E50N.get())
        N20 = int(E20N.get())
        N10 = int(E10N.get())
        C10 = int(E10C.get())
        C5 = int(E5C.get())
        C2 = int(E2C.get())
        C1 = int(E1C.get())

        total = (N500*500) + (N200*200) + (N100*100) + (N50*50) + (N20*20) + (N10*10) + (C10*10) + (C5*5) + (C2*2) + (C1*1)
        TA.config(text=f"Total amount: ₹{total}")

        T500N.config(text=f"₹{N500*500}")
        T200N.config(text=f"₹{N200*200}")
        T100N.config(text=f"₹{N100*100}")
        T50N.config(text=f"₹{N50*50}")
        T20N.config(text=f"₹{N20*20}")
        T10N.config(text=f"₹{N10*10}")
        T10C.config(text=f"₹{C10*10}")
        T5C.config(text=f"₹{C5*5}")
        T2C.config(text=f"₹{C2*2}")
        T1C.config(text=f"₹{C1*1}")

    except ValueError:
        pass

tk.mainloop()
