from tkinter import  *

def calculate_km():
    miles = float(miles_input.get())
    km = round(miles *1.61)
    km_output.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")

miles_input = Entry()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

km_output = Label(text="0")
km_output.grid(row=1, column=1)

km_label=Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(row=2, column=1)

window.mainloop()