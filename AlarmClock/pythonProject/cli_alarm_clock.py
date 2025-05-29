from datetime import datetime
import time
import sys

try:
    import winsound
    SOUND_ENABLED = True
    SOUND_EFFECT = "./Sounds/alarm_beep.wav"
except ImportError:
    SOUND_ENABLED = False


#===============================================#
#============== FUNCTIONS ======================#
#===============================================#

def get_alarm_time():
    while True:
        alarm_input = input("Set alarm time (HH:MM:SS, 24-hour format), or Q to quit: ")
        if alarm_input == "Q":
            return None
        try:
            alarm_time = datetime.strptime(alarm_input, "%H:%M:%S").time()
            return alarm_time
        except ValueError:
            print("Invalid format. Please use HH:MM:SS (e.g., 07:30:00)")

def main():
    print("=== Python CLI Alarm Clock ===")
    alarm_time = get_alarm_time()
    if not alarm_time:
        # Safely quit from program
        sys.exit(1)

    print(f"Alarm set for {alarm_time}. Waiting...")

    while True:
        now = datetime.now().time()
        current_time = now.replace(microsecond=0)

        if current_time == alarm_time:
            print("\n🔔 Wake up! Alarm time reached!")

            if SOUND_ENABLED:
                winsound.PlaySound(SOUND_EFFECT, winsound.SND_FILENAME)
            else:
                print("Beep! Beep! (Sound disabled)")
            break

        # Sleep for 1 second
        time.sleep(1)

#===============================================#
#============== MAIN PROGRAM ===================#
#===============================================#

if __name__ == "__main__":
    main()
