from tkinter import *

def mile_to_km(event=None):
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.60934, 2)
        kilometer_result_label.config(text=f"{km} Kilometers", fg="#2e7d32")
    except ValueError:
        kilometer_result_label.config(text="Invalid input", fg="red")

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=30, pady=30, bg="#f9f9f9")

# Font settings
label_font = ("Arial", 14, "bold")
result_font = ("Arial", 16, "bold")
entry_font = ("Arial", 14)
button_font = ("Arial", 14, "bold")

# Miles input box
miles_input = Entry(window, width=10, font=entry_font)
miles_input.grid(column=1, row=0)
miles_input.focus()

# Miles label
miles_label = Label(window, text="Miles", font=label_font, bg="#f9f9f9")
miles_label.grid(column=2, row=0, padx=10)

# "is equal to" label
is_equal_label = Label(window, text="is equal to", font=label_font, bg="#f9f9f9")
is_equal_label.grid(column=0, row=1, pady=20)

# Result label
kilometer_result_label = Label(window, text="0 Kilometers", font=result_font, bg="#e0f2f1", width=15)
kilometer_result_label.grid(column=1, row=1)

# Kilometers label
kilometer_label = Label(window, text="Kilometers", font=label_font, bg="#f9f9f9")
kilometer_label.grid(column=2, row=1, padx=10)

# Calculate button
calculate_button = Button(window, text="Calculate", font=button_font, bg="#4caf50", fg="white",
                          activebackground="#45a049", padx=10, pady=5, command=mile_to_km)
calculate_button.grid(column=1, row=2, pady=10)

# Bind Enter key to calculation
window.bind("<Return>", mile_to_km)

window.mainloop()
