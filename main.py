import tkinter as tk
from field import Field

window = tk.Tk()
fr_playfield = tk.Frame()
fr_playfield.rowconfigure(3)
fr_playfield.columnconfigure(3)

label = tk.Label(
    text="Time to play!"
)

field = Field(label)

for i in range(3):
    for j in range(3):
        new_button = tk.Button(
            fr_playfield,
            height="4",
            width="4",
            text="❓",
            command=lambda i_=i, j_=j: field.tick(i_, j_)
        )
        field.tile_list[3 * i + j].button = new_button
        new_button.grid(
            row=i,
            column=j
        )

field.label.pack()
fr_playfield.pack()
window.mainloop()
