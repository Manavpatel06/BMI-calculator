import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        user = user_entry.get()
        result_label.config(text="{}'s BMI: {:.2f}".format(user, bmi))
        save_bmi_data(user, bmi)
        show_bmi_chart(user)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height")

def save_bmi_data(user, bmi):
    with open("bmi_data.txt", "a") as file:
        file.write("{} {}\n".format(user, bmi))

def show_past_details():
    user = user_entry.get()
    past_bmi_data = []
    with open("bmi_data.txt", "r") as file:
        for line in file:
            data = line.split()
            if data[0] == user:
                past_bmi_data.append(float(data[1]))

    if past_bmi_data:
        plt.figure(figsize=(6, 4))
        plt.plot(past_bmi_data, marker='o', linestyle='-', color='b')
        plt.title("{}'s BMI Trend".format(user))
        plt.xlabel("Record")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, columnspan=2, padx=10, pady=10)
    else:
        messagebox.showinfo("Info", "No past BMI data found for {}".format(user))

def show_bmi_chart(user):
    past_bmi_data = []
    with open("bmi_data.txt", "r") as file:
        for line in file:
            data = line.split()
            if data[0] == user:
                past_bmi_data.append(float(data[1]))

    if past_bmi_data:
        plt.figure(figsize=(6, 4))
        plt.plot(past_bmi_data, marker='o', linestyle='-', color='b')
        plt.title("{}'s BMI Trend".format(user))
        plt.xlabel("Record")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, columnspan=2, padx=10, pady=10)
    else:
        messagebox.showinfo("Info", "No past BMI data found for {}".format(user))

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

user_label = tk.Label(root, text="User:")
user_label.grid(row=2, column=0, padx=10, pady=10)
user_entry = tk.Entry(root)
user_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

show_past_button = tk.Button(root, text="Show Past Details", command=show_past_details)
show_past_button.grid(row=5, columnspan=2, padx=10, pady=10)

root.mainloop()
