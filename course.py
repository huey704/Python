import tkinter as tk

window = tk.Tk()
window.title("Assetto Tracker")
window.geometry("300x200")

lap_label = tk.Label(window, text="Current Lap Time: 0.00s")
lap_label.pack(pady=10)


def update_time():
    # Simulate lap time increment
    current = float(lap_label["text"].split(": ")[1][:-1])
    current += 0.1
    lap_label.config(text=f"Current Lap Time: {current:.2f}s")
    window.after(100, update_time)


update_time()
window.mainloop()
