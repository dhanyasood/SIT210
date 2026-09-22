import tkinter as tk
import RPi.GPIO as GPIO


LIVING_ROOM = 18   # PWM pin
BATHROOM = 27
CLOSET = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(LIVING_ROOM, GPIO.OUT)
GPIO.setup(BATHROOM, GPIO.OUT)
GPIO.setup(CLOSET, GPIO.OUT)

# PWM for Living Room
pwm = GPIO.PWM(LIVING_ROOM, 1000)
pwm.start(0)


def select_room(room_number):

    # Turn off normal LEDs
    GPIO.output(BATHROOM, GPIO.LOW)
    GPIO.output(CLOSET, GPIO.LOW)

    if room_number == 1:
        # Living Room
        pwm.ChangeDutyCycle(brightness.get())

        selected_room.config(text="Living Room")

    elif room_number == 2:
        # Bathroom
        pwm.ChangeDutyCycle(0)
        GPIO.output(BATHROOM, GPIO.HIGH)

        selected_room.config(text="Bathroom")

    elif room_number == 3:
        # Closet
        pwm.ChangeDutyCycle(0)
        GPIO.output(CLOSET, GPIO.HIGH)

        selected_room.config(text="Closet")


def change_brightness(value):

    brightness_value = float(value)

    # Update percentage displayed
    percentage.config(text=f"{int(brightness_value)}%")

    # Only control PWM when Living Room is selected
    if room.get() == 1:
        pwm.ChangeDutyCycle(brightness_value)


def exit_program():

    pwm.stop()
    GPIO.cleanup()
    window.destroy()


window = tk.Tk()

window.title("Smart Home Lighting")
window.geometry("500x500")

window.configure(bg="#EAF2F8")




title = tk.Label(
    window,
    text="Smart Home Lighting",
    font=("Arial", 24, "bold"),
    bg="#EAF2F8"
)

title.pack(pady=25)



selected_room = tk.Label(
    window,
    text="Select a Room",
    font=("Arial", 16, "bold"),
    bg="#EAF2F8"
)

selected_room.pack(pady=10)



room = tk.IntVar(value=0)

living = tk.Radiobutton(
    window,
    text="Living Room",
    variable=room,
    value=1,
    command=lambda: select_room(1),
    font=("Arial", 15),
    bg="#EAF2F8"
)

living.pack(pady=5)


bathroom = tk.Radiobutton(
    window,
    text="Bathroom",
    variable=room,
    value=2,
    command=lambda: select_room(2),
    font=("Arial", 15),
    bg="#EAF2F8"
)

bathroom.pack(pady=5)


closet = tk.Radiobutton(
    window,
    text="Closet",
    variable=room,
    value=3,
    command=lambda: select_room(3),
    font=("Arial", 15),
    bg="#EAF2F8"
)

closet.pack(pady=5)


brightness_title = tk.Label(
    window,
    text="Living Room Brightness",
    font=("Arial", 15, "bold"),
    bg="#EAF2F8"
)

brightness_title.pack(pady=(25, 5))


percentage = tk.Label(
    window,
    text="100%",
    font=("Arial", 18, "bold"),
    bg="#EAF2F8"
)

percentage.pack()


brightness = tk.IntVar(value=100)

brightness_slider = tk.Scale(
    window,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    variable=brightness,
    length=350,
    showvalue=False,
    command=change_brightness,
    bg="#EAF2F8"
)

brightness_slider.pack(pady=10)



exit_button = tk.Button(
    window,
    text="Exit",
    command=exit_program,
    font=("Arial", 14),
    width=12
)

exit_button.pack(pady=25)


pwm.ChangeDutyCycle(0)

GPIO.output(BATHROOM, GPIO.LOW)
GPIO.output(CLOSET, GPIO.LOW)


window.mainloop()
