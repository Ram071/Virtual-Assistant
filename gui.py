from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text


def User_send():
    """Process text entered by the user."""

    send = entry1.get().strip()

    if not send:
        return

    text.insert(END, "Me --> " + send + "\n")

    bot = action.Action(send)

    if bot is not None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")

    entry1.delete(0, END)

    if bot == "ok sir":
        root.destroy()


def ask():
    """Listen to the user's voice and process the command."""

    ask_val = spech_to_text.spech_to_text()

    if ask_val is None:
        return

    text.insert(END, "Me --> " + ask_val + "\n")

    bot_val = action.Action(ask_val)

    if bot_val is not None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")

    if bot_val == "ok sir":
        root.destroy()


def delete_text():
    """Clear the conversation text."""

    text.delete("1.0", END)


# --------------------------------------------------
# Main Window
# --------------------------------------------------

root = Tk()

root.geometry("550x675")
root.title("AI Assistant")
root.resizable(False, False)
root.config(bg="#6F8FAF")


# --------------------------------------------------
# Main Frame
# --------------------------------------------------

Main_frame = LabelFrame(
    root,
    padx=100,
    pady=7,
    borderwidth=3,
    relief="raised",
    bg="#6F8FAF"
)

Main_frame.grid(
    row=0,
    column=1,
    padx=55,
    pady=10
)


# --------------------------------------------------
# Title
# --------------------------------------------------

Text_lable = Label(
    Main_frame,
    text="AI Assistant",
    font=("Comic Sans MS", 14, "bold"),
    bg="#356696"
)

Text_lable.grid(
    row=0,
    column=0,
    padx=20,
    pady=10
)


# --------------------------------------------------
# Assistant Image
# --------------------------------------------------

try:
    Display_Image = ImageTk.PhotoImage(
        Image.open("image/assitant.png")
    )

    Image_Lable = Label(
        Main_frame,
        image=Display_Image,
        bg="#6F8FAF"
    )

    Image_Lable.grid(
        row=1,
        column=0,
        pady=20
    )

except FileNotFoundError:
    Image_Lable = Label(
        Main_frame,
        text="AI Assistant",
        font=("Arial", 20, "bold"),
        bg="#6F8FAF"
    )

    Image_Lable.grid(
        row=1,
        column=0,
        pady=60
    )


# --------------------------------------------------
# Conversation Text Box
# --------------------------------------------------

text = Text(
    root,
    font=("Courier", 10, "bold"),
    bg="#356696",
    fg="white"
)

text.place(
    x=100,
    y=375,
    width=375,
    height=100
)


# --------------------------------------------------
# User Input
# --------------------------------------------------

entry1 = Entry(
    root,
    justify=CENTER,
    font=("Arial", 11)
)

entry1.place(
    x=100,
    y=500,
    width=350,
    height=30
)


# --------------------------------------------------
# ASK Button
# --------------------------------------------------

button1 = Button(
    root,
    text="ASK",
    bg="#356696",
    fg="white",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=ask
)

button1.place(
    x=70,
    y=575
)


# --------------------------------------------------
# SEND Button
# --------------------------------------------------

button2 = Button(
    root,
    text="Send",
    bg="#356696",
    fg="white",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=User_send
)

button2.place(
    x=400,
    y=575
)


# --------------------------------------------------
# DELETE Button
# --------------------------------------------------

button3 = Button(
    root,
    text="Delete",
    bg="#356696",
    fg="white",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=delete_text
)

button3.place(
    x=225,
    y=575
)


# --------------------------------------------------
# Start GUI
# --------------------------------------------------

root.mainloop()
