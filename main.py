
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Loading Progress Simulator")
app.geometry("390x300")

progress = ctk.CTkProgressBar(
    app,
    width=300,
    height=18,
    progress_color="green"
)
progress.pack(pady=(30, 10))
progress.set(0)

percent_label = ctk.CTkLabel(
    app,
    text="0%",
    font=("Arial", 16)
)
percent_label.pack()

current = 0


def step():
    global current

    current += 1
    progress.set(current / 100)
    percent_label.configure(text=f"{current}%")

    if current < 100:
        app.after(30, step)
    else:
        percent_label.configure(text="Completed!")
        start_button.configure(state="normal")


def start():
    global current

    current = 0
    progress.set(0)
    percent_label.configure(text="0%")
    start_button.configure(state="disabled")

    step()


start_button = ctk.CTkButton(
    app,
    text="Start Loading",
    command=start
)
start_button.pack(pady=15)

app.mainloop()
