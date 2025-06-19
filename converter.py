from tkinter import *

def mile_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 2)
        kilometer_result_label.config(text=f"{km}")
    except ValueError:
        kilometer_result_label.config(text="Invalid input. Please enter a number.")

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", pady=10)
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0", pady=10)
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Kilometers", pady=10)
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
