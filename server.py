import socket
import tkinter as tk
import threading as tr
from PIL import ImageTk, Image

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.sock = socket.socket()
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.sock.bind((ip, 9090))
        new_tr = tr.Thread(target=self.start_server)
        new_tr.start()

    def change_image(self):
        im = Image.open("phoenix.png")
        im = im.resize((256, 256))
        self.img = ImageTk.PhotoImage(im)
        self.lab = tk.Label(self, image=self.img)
        self.lab.pack()
        

    def start_server(self):
        self.sock.listen(1)

        user, addr = self.sock.accept()
        while True:
            data = user.recv(1024)
            if not data:
                break

            print(str(data))
            if (data.decode('utf-8') == "HI"):
                user.send(data)
            else:
                self.change_image()


root = tk.Tk()
root.title("server")
root.geometry("256x256+150+80")
root.config(bg="#C45B90")
root.minsize(256, 256)
my_app = App(root)
my_app.mainloop()