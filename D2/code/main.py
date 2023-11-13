import tkinter as tk
import calculator as calculator
import data_validator as data_validator
import csv_processor as csv_processor

from tkinter.filedialog import askopenfile
from tkinter import messagebox

def browse_csv():
    try:
        file = askopenfile(parent= root, mode='r', filetypes=[("CSV Files","*.csv")], title='Choose a file')
        if file is not None:
            csv_worker = csv_processor.CsvProcessor(file)
            input_data = csv_worker.read_csv_and_validate()
            input_text.delete('1.0', tk.END)
            input_text.insert('1.0', ','.join([str(i) for i in input_data]))
    except Exception as e:
       messagebox.showerror("Error", e)

# create window
root = tk.Tk()
root.title("METRICSTICS")

# input frame
input_frame = tk.Frame(root)
input_frame.pack(side="top", fill=tk.BOTH, expand=True)

# input text box
input_label = tk.Label(input_frame, text="Input", anchor="w")
input_label.pack(side="left", anchor="w")

input_text = tk.Text(root, height=20, width=40)
input_text.pack(fill=tk.BOTH, expand=True)

upload_button = tk.Button(input_frame,text="Upload sales data", command=lambda: browse_csv())
upload_button.pack(side="right", padx=10, pady=10)

# buttons
operations_frame = tk.Frame(root)
operations_frame.pack(side="top", fill=tk.BOTH, expand=True)

calc = calculator.Calculator([])
validator = data_validator.DataValidator()

# output text box
output_label = tk.Label(root, text="Output", anchor="w")
output_label.pack(side="top", anchor="w")

output_text = tk.Text(root, height=3, width=40, state="disabled")
output_text.pack(fill=tk.BOTH, expand=True)

def calculate_input(func):
    try: 
        input_array = validator.process(input_text.get("1.0",tk.END))
        calc.set_data(input_array)
        output_text.configure(state="normal")
        output_text.delete('1.0', tk.END)
        output_text.insert("1.0", str(func()))
        output_text.configure(state="normal")
    except Exception as e:
       messagebox.showerror("Error", e)

operations = {
    "Minimum" : lambda: calc.get_min(),
    "Maximum": lambda: calc.get_max(),
    "Median": lambda: calc.get_median(),
    "Arithmetic Mean": lambda: calc.get_arithmetic_mean(),
    "MAD": lambda: calc.get_mean_abs_deviation(),
    "Standard Deviation": lambda: calc.get_standard_deviation()
}

for index, key in enumerate(operations):
    operation_button = tk.Button(operations_frame, text=key, command= lambda func = operations[key]: calculate_input(func))
    operation_button.pack(side="left", padx=10, pady=10)

root.mainloop()


