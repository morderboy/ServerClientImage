import socket
import tkinter as tk

def sub_ip(ip : str):
    idx = ip.rfind('.')
    return ip[:idx + 1]

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
        ip = sub_ip(ip)

        is_connected = False
        for i in range(0, 15):
            try:
                self.client.settimeout(1)
                self.client.connect((ip + str(i), 9090))
                self.client.settimeout(None)
            except socket.timeout:
                print("timeout:" + str(i))
                print(self.client.getsockname())
                self.client.close()
                self.client = socket.socket()
                continue
            except socket.error as msg:
                print(i)
                print(msg)
                self.client.close()
                self.client = socket.socket()
                continue

            self.client.send(bytes("HI", 'ascii'))
            while True:
                print("start handshake")
                data = self.client.recv(1024)
                if not data:
                    break
                if (data.decode('utf-8') == "HI"):
                    is_connected = True
                    break

            if is_connected:
                break

        if is_connected:
            pass
        else:
            print(self.client.gettimeout())
            print("GG WP EZ")


root = tk.Tk()
root.title("client")
root.geometry("256x256+150+80")
root.config(bg="#C45B90")
root.minsize(256, 256)
my_app = App(root)
my_app.mainloop()
