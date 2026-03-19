from tkinter import *

rt = Tk()
rt.title("Stopwatch")
rt.geometry("500x300")
rt.configure(bg="black")

# time variables
hr = 0
mn = 0
sc = 0
running = False


lbl = Label(rt, text="0:0:0",
            font=("arial", 30, "bold"),
            fg="red",
            bg="black",
            width=8)
lbl.place(x=170, y=120)


def update_time():
    global hr, mn, sc, running

    if running:
        sc += 1

        if sc == 60:
            sc = 0
            mn += 1

        if mn == 60:
            mn = 0
            hr += 1

        lbl.config(text=f"{hr}:{mn}:{sc}")

        rt.after(1000, update_time)


def Start():
    global running
    running = True
    update_time()


def Stop():
    global running
    running = False


def Reset():
    global hr, mn, sc, running
    running = False
    hr = 0
    mn = 0
    sc = 0
    lbl.config(text="0:0:0")



start_btn = Button(rt, text="Start", font=("arial", 15), command=Start)
start_btn.place(x=60, y=20)

stop_btn = Button(rt, text="Stop", font=("arial", 15), command=Stop)
stop_btn.place(x=200, y=20)

reset_btn = Button(rt, text="Reset", font=("arial", 15), command=Reset)
reset_btn.place(x=330, y=20)

rt.mainloop()