from tkinter import Tk, Label, Entry, Button

class Form:
    pass

commision_form = Form()

while True:
    attribute_name = input("Please enter attribute name: ")
    attribute_value = input("Please enter attribute value: ")

    setattr(commision_form, attribute_name, attribute_value)


    if input("Do want continue[Y,N]: ").upper() == "N":
        break

window = Tk()
window.title("Dynamic Form")

entry_list = []

row_number = 0
for key, value in commision_form.__dict__.items():
    label_form = Label(window, text=key)
    label_form.grid(column=0, row=row_number, pady=5, padx=5)

    entry_form = Entry(window, width=50)
    entry_form.insert(0, value)
    entry_form.grid(column=1, row=row_number, pady=5, padx=5)

    entry_list.append({f"{key}": entry_form})

    row_number += 1

def submit():
    data = ""
    for entry_dict in entry_list:
        for name, entry in entry_dict.items():
            data += f"{name}:{entry.get()},"

    with open("FormData.txt", mode="w") as file:
        file.write(data)

    window.destroy()

submit_button = Button(window, text="Submit", command=submit)
submit_button.grid(row=row_number, column=1, pady=5, padx=5)

window.mainloop()




