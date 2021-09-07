import tkinter as tk
from cookie_clicker import CookieClicker

class ClickerController(tk.Frame):
    def __init__(self, master=None, clicker=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.clicker = clicker
        self.pack()

    def create_widgets(self):
        self.click_count = tk.Text(root, height=20, width=50)
        rapid_button = tk.Button(self, text="Rapid Click", command=self._rapid_clicker)
        quit_button = tk.Button(self, text="Quit", command=self._shutdown_all)

        self.click_count.pack()
        rapid_button.pack()
        quit_button.pack()

    def _rapid_clicker(self):
        count = int(self.click_count.get("1.0", "end-1c"))
        self.clicker.rapid_click(count)

    def _shutdown_all(self):
        self.clicker.shutdown_clicker()
        self.quit()

if __name__ == "__main__":
    root = tk.Tk()
    clicker_obj = CookieClicker()
    c = ClickerController(master=root, clicker=clicker_obj)
    c.mainloop()