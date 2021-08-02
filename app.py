from tkinter import * 

from app_helper import chat

def send():
    message = EntryBox.get("1.0", "end-1c").strip()
    EntryBox.delete("0.0", END)

    if message != "":

        ChatLog.config(state = NORMAL)
        ChatLog.insert(END, "You: " + message + "\n\n")

        result = chat(message)
        ChatLog.insert(END, "MC: " + result + "\n\n")

        ChatLog.config(state = DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Monolingual Chatbot")
base.geometry("500x500")
base.resizable(width = False, height = False)

ChatLog = Text(base, bd = 0, bg = "white", height = "8", width = "50", font = "Arial")

ChatLog.config(state = NORMAL)
ChatLog.insert(END, "MC: " + "Hello there! How are you?" + "\n\n")
ChatLog.config(foreground = "#cd5c5c", font = ("Verdana", 12))
ChatLog.config(state = DISABLED)

scrollbar = Scrollbar(base, command = ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set 

EntryBox = Text(base, bd = 0, bg = "white", width = "10", height = "5", font = "Arial")

SendButton = Button(base, font = ("Verdana", 12, 'bold'), text = "Send", width = "11", height = 5,
                    bd = 0, bg = "#cd5c5c", activebackground = "#cd5c5c", fg = "#ffffff",
                    command = send)

scrollbar.place(x = 475, y = 6, height = 386)
ChatLog.place(x = 6, y = 6, height = 386, width = 466)
EntryBox.place(x = 6, y = 401, height = 90, width = 350)
SendButton.place(x = 360, y = 401, height = 90)

base.mainloop()