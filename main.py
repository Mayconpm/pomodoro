import tkinter as tk
from math import floor

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


def timer_reset():
    global timer
    global reps
    window.after_cancel(timer)
    reps = 0
    checkmarks_text = ""
    checkmarks_label.config(text=checkmarks_text)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(work_time)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_time)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(long_break_time)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    # global checkmarks_label
    # global checkmarks_text
    global reps

    count_minutes = floor(count / 60)
    count_seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{count_minutes:02d}:{count_seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = floor(reps / 2)
        checkmarks_text = ""
        for _ in range(work_sessions):
            checkmarks_text += "✔ "
            checkmarks_label.config(text=checkmarks_text)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, background=YELLOW)


canvas = tk.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas_tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=canvas_tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

checkmarks_label = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
checkmarks_label.grid(column=1, row=3)

start_button = tk.Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=timer_reset)
reset_button.grid(column=2, row=2)


window.mainloop()
