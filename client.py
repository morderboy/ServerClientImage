import socket
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.btn = tk.Button(text='BTN', font="Arial 40", width=5, height=2, command=self.click)
        self.btn.place(relx=0.5, rely=0.5, anchor='center')

        self.client = socket.socket()
        self.scan_conn()

    def click(self):
        self.client.send(bytes("\00", 'ascii'))

    def scan_conn(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        self.client.connect((ip, 9090))


root = tk.Tk()
root.title("client")
root.geometry("256x256+150+80")
root.config(bg="#C45B90")
root.minsize(256, 256)
my_app = App(root)
my_app.mainloop()
