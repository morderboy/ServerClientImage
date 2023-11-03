import socket
import tkinter as tk
import threading as tr

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.sock = socket.socket()
        self.sock.bind(('192.168.1.7', 9090))
        new_tr = tr.Thread(target=self.start_server)
        new_tr.start()

    def change_image(self):
        self.master.configure(background='black')

    def start_server(self):
        self.sock.listen(1)

        user, addr = self.sock.accept()
        while True:
            data = user.recv(1)
            if not data:
                break
            self.change_image()


root = tk.Tk()
root.title("server")
root.geometry("256x256+150+80")
root.config(bg="#C45B90")
root.minsize(256, 256)
my_app = App(root)
my_app.mainloop()