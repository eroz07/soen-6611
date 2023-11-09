import tkinter as tk
import calculator as calculator

# create window
root = tk.Tk()
root.title("METRICSTICS")

# input text box
input_label = tk.Label(root, text="Input", anchor="w")
input_label.pack(side="top", anchor="w")

input_text = tk.Text(root, height=20, width=40)
input_text.pack(fill=tk.BOTH, expand=True)

# buttons
operations_frame = tk.Frame(root)
operations_frame.pack(side="top", fill=tk.BOTH, expand=True)

calc = calculator.Calculator([])

# output text box
output_label = tk.Label(root, text="Output", anchor="w")
output_label.pack(side="top", anchor="w")

output_text = tk.Text(root, height=3, width=40, state="disabled")
output_text.pack(fill=tk.BOTH, expand=True)

def calculate_input(func):
    input_array = [int(x.strip()) for x in input_text.get("1.0",tk.END).split(',')]
    calc.set_data(input_array)
    output_text.configure(state="normal")
    output_text.delete('1.0', tk.END)
    output_text.insert("1.0", str(func()))
    output_text.configure(state="normal")

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


