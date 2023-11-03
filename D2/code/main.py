import tkinter as tk

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

operations = ["Minimum", "Maximum", "Mode", "Median", "Arithmetic Mean", "MAD", "Standard Deviation"]

for operation in operations:
    operation_button = tk.Button(operations_frame, text=operation)
    operation_button.pack(side="left", padx=10, pady=10)

# output text box
output_label = tk.Label(root, text="Output", anchor="w")
output_label.pack(side="top", anchor="w")

output_text = tk.Text(root, height=3, width=40)
output_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()


