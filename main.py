from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CHECKMARK = "✅"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0

# ---------------------------- BUTTON COMMANDS ------------------------------- #


def start_command():
    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text='Long break', fg=RED)
        countdown(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        title_label.config(text='Short break', fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)

    else:
        title_label.config(text='Work', fg=GREEN)
        countdown(WORK_MIN * 60)


def reset_command():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    success_label.config(text="")
    title_label.config(text="Timer")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global timer
    mins = math.floor(count / 60)
    secs = math.floor(count % 60)

    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)

    else:
        success_string = ""
        session = math.floor(reps / 2)

        for _ in range(session):
            success_string += CHECKMARK

        success_label.config(text=success_string)

        start_command()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN, highlightthickness=0)
title_label.grid(row=0, column=1)

canvas = Canvas(width=206, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 113, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_command, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_command, highlightthickness=0)
reset_button.grid(row=2, column=2)

success_label = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
success_label.grid(row=3, column=1)

window.mainloop()
