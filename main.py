import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, background=YELLOW)

canvas = tk.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas_tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=canvas_tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=1)

checkmark_label = tk.Label(text=" ✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
checkmark_label.grid(column=1, row=4)

start_button = tk.Button(text="Start", font=(FONT_NAME, 12, "bold"))
start_button.grid(column=0, row=3)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 12, "bold"))
reset_button.grid(column=2, row=3)


window.mainloop()
