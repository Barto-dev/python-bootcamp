from tkinter import *

BACKGROUND = "white"


def create_label(parent, text, column, row, **kwargs):
    label = Label(parent, text=text, background=BACKGROUND, **kwargs)
    label.grid(column=column, row=row)
    return label


def create_button(parent, text, column, row, **kwargs):
    button = Button(parent, text=text, background=BACKGROUND, **kwargs)
    button.grid(column=column, row=row)
    return button


def mile_to_km():
    km = round(float(mile_entry.get()) * 1.609, 2)
    result.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=160)
window.config(padx=10, pady=10, background=BACKGROUND)
window.eval("tk::PlaceWindow . center")

main_frame = Frame(window, bg=BACKGROUND)
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


mile_entry = Entry(main_frame, background=BACKGROUND)
mile_entry.insert(END, string="0")
mile_entry.grid(column=1, row=0, padx=10, pady=10)

equal_label = create_label(main_frame, text="is equal to", column=0, row=1)
calculate_button = create_button(main_frame, text="Calculate", column=1, row=2, command=mile_to_km)
result = create_label(main_frame, text="0", column=1, row=1)
mile_label = create_label(main_frame, text="Miles", column=2, row=0)
km_label = create_label(main_frame, text="Km", column=2, row=1)

# should be always in the end of the program
window.mainloop()
