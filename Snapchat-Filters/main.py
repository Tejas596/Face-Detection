import cv2
import tkinter as tk
import glass as g
import mustache as m
import oil_paint as o
import dog_filter as d
import fire_eyes as f
import brightener as b
import bw
import blur as bl

# Initialize Tkinter root window
root = tk.Tk()
root.geometry("500x400")  # Adjust the window size for better spacing
root.title("SNAPCHAT_FILTERS")
root.config(bg="#2e3b4e")  # Dark background color for the window

# Define a custom style for buttons
button_style = {
    'width': 20,
    'height': 2,
    'font': ('Arial', 12),
    'bg': 'grey',
    'fg': 'white',
    'bd': 0,
    'relief': 'solid',
    'activebackground': '#45a049',
    'activeforeground': 'black',
}

# Add a frame to group the buttons together and make the layout cleaner
frame = tk.Frame(root, bg="#2e3b4e")
frame.pack(pady=30)  # Add some space at the top of the window

# Add buttons using grid layout for better arrangement
button1 = tk.Button(frame, text="GLASSES", command=g.apply_glass, **button_style)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(frame, text="MUSTACHE", command=m.apply_mustache, **button_style)
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(frame, text="OIL_PAINT", command=o.apply_oilpaint, **button_style)
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = tk.Button(frame, text="DOG_FILTER", command=d.apply_dogfilter, **button_style)
button4.grid(row=1, column=1, padx=10, pady=10)

button5 = tk.Button(frame, text="FIRE_EYES", command=f.apply_fire_eyes, **button_style)
button5.grid(row=2, column=0, padx=10, pady=10)

button6 = tk.Button(frame, text="BRIGHTENER", command=b.apply_brighten, **button_style)
button6.grid(row=2, column=1, padx=10, pady=10)

button7 = tk.Button(frame, text="BW", command=bw.apply_bw, **button_style)
button7.grid(row=3, column=0, padx=10, pady=10)

button8 = tk.Button(frame, text="BLUR", command=bl.apply_blur, **button_style)
button8.grid(row=3, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
