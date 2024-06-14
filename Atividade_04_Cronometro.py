import tkinter as tk

class Stopwatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cronómetro")
        self.label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 30))
        self.label.pack()
        self.start_button = tk.Button(self.root, text='Iniciar', command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text='Parar', command=self.stop)
        self.stop_button.pack()
        self.reset_button = tk.Button(self.root, text='Resetar', command=self.reset)
        self.reset_button.pack()
        self.running = False
        self.seconds = 0

    def tick(self):
        if self.running:
            self.seconds += 1
            time_string = "{:02}:{:02}:{:02}".format(self.seconds // 3600, (self.seconds // 60) % 60, self.seconds % 60)
            self.label.config(text=time_string)
            self.root.after(1000, self.tick)

    def start(self):
        if not self.running:
            self.running = True
            self.tick()

    def stop(self):
        self.running = False

    def reset(self):
        if not self.running:
            self.seconds = 0
            self.label.config(text="00:00:00")

if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.root.mainloop()