import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Systemrequirements")

# Create a label with some text
label = tk.Label(root, text="Python 3.12    Wi-Fi Connection")
label.pack(pady=50)

# Set the window size
root.geometry("400x200")

# Run the application
root.mainloop()
