import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from threading import Thread
import time
from plyer import notification
from playsound import playsound

def remind_at_time(title, msg, remind_time):
    while True:
        now = datetime.now()
        if now >= remind_time:
            notification.notify(
                title=f"📞 {title}",
                message=msg,
                timeout=10
            )
            # Simulate a 'call' with popup and sound
            playsound("ringtone.mp3")
            messagebox.showinfo(f"📞 Incoming Reminder: {title}", msg)
            break
        time.sleep(1)

def set_reminder():
    title = title_entry.get()
    msg = msg_entry.get()
    date_str = date_entry.get()
    time_str = time_entry.get()

    try:
        remind_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        if remind_time < datetime.now():
            messagebox.showerror("Error", "Time must be in the future.")
            return

        Thread(target=remind_at_time, args=(title, msg, remind_time), daemon=True).start()
        messagebox.showinfo("Reminder Set", f"Reminder set for {remind_time}")
    except Exception as e:
        messagebox.showerror("Invalid Input", str(e))

# GUI Setup
root = tk.Tk()
root.title("📅 Lightweight Reminder App")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="white")

tk.Label(root, text="Reminder Title:", bg="white").pack(pady=(20, 5))
title_entry = tk.Entry(root, width=40)
title_entry.pack()

tk.Label(root, text="Message:", bg="white").pack(pady=5)
msg_entry = tk.Entry(root, width=40)
msg_entry.pack()

tk.Label(root, text="Date (YYYY-MM-DD):", bg="white").pack(pady=5)
date_entry = tk.Entry(root, width=20)
date_entry.pack()

tk.Label(root, text="Time (HH:MM in 24hr):", bg="white").pack(pady=5)
time_entry = tk.Entry(root, width=20)
time_entry.pack()

tk.Button(root, text="Set Reminder", command=set_reminder, bg="#4CAF50", fg="white", width=20).pack(pady=20)

root.mainloop()
