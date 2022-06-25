from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_window():
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    tick_mark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        title_label.config(text="WORK", fg=RED)
        count_down(work_sec)
    elif reps % 2 == 0 and reps < 8:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        reps = 0
        title_label.config(text="L_Break", fg=GREEN)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick_mark_label.config(text=mark)
        window.after(1, start_timer())

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(105, 140, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

tick_mark_label = Label(fg=GREEN, bg=YELLOW, font=14)
tick_mark_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_window)
reset_button.grid(column=2, row=2)

window.mainloop()
