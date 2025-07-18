import tkinter as tk
from tkinter import ttk

# Create main window
window = tk.Tk()
window.title("Responsive Hello GUI")
window.geometry("600x400")
window.configure(bg="#2c3e50")

# Allow rows and columns to expand when window is resized
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Create a Frame to center content
main_frame = ttk.Frame(window)
main_frame.grid(column=0, row=0, sticky="nsew", padx=20, pady=20)

# Let the frame's row and column expand
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# Style settings
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel",
                background="#2c3e50",
                foreground="#ecf0f1",
                font=("Segoe UI", 24, "bold"),
                anchor="center")

style.configure("TButton",
                font=("Segoe UI", 14),
                foreground="#2c3e50",
                background="#ecf0f1",
                padding=10)

style.map("TButton",
          background=[("active", "#bdc3c7")])

# Label
label = ttk.Label(main_frame, text="👋 Hello, World!", anchor="center")
label.grid(row=0, column=0, sticky="n", pady=20)

# Button click action
def say_hi():
    label.config(text="🎉 You clicked the button!")

# Button
button = ttk.Button(main_frame, text="Click Me", command=say_hi)
button.grid(row=1, column=0, sticky="n")

# Start the GUI
window.mainloop()
