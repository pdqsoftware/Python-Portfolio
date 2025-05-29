from tkinter import *
from tkinter import messagebox
import datetime
import time
import threading


try:
    import winsound
    SOUND_ENABLED = True
    SOUND_EFFECT = "./Sounds/alarm_beep.wav"
except ImportError:
    SOUND_ENABLED = False


#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def set_alarm():
    alarm_time = entry.get()
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        status_label.config(text=f"Alarm set for {alarm_time}")
        threading.Thread(target=alarm_thread, args=(alarm_time,), daemon=True).start()
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format")

def alarm_thread(alarm_time_str):
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time_str:
            if SOUND_ENABLED:
                winsound.PlaySound(SOUND_EFFECT, winsound.SND_FILENAME)
            else:
                messagebox.showinfo("Alarm", "🔔 Wake up!")
            break
        time.sleep(1)

def update_clock():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=f"Current Time: {now}")
    window.after(1000, update_clock,)


#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

# Setup GUI
window = Tk()
window.title("Alarm Clock")
window.geometry("350x200")
window.resizable(False, False)

clock_label = Label(window, font=("Helvetica", 20))
clock_label.pack(pady=10)

entry_label = Label(window, text="Set Time (HH:MM:SS):")
entry_label.pack()

entry = Entry(window, font=("Helvetica", 14), justify='center')
entry.pack(pady=5)

set_button = Button(window, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

status_label = Label(window, text="", fg="green")
status_label.pack()

update_clock()
window.mainloop()
