import tkinter as tk

window = tk.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.title("TrackGraph")
# window.attributes("-fullscreen", True)
window.geometry("%dx%d" % (600, 600))
window.mainloop()



