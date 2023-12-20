import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import tkinter as tk
import os


# Define the function
def func(d, R):
    return (math.pi ** (d / 2) * R ** d) / math.gamma(1 + d / 2)


# Function to generate the graph and save data to Excel
def generate_graph():
    # Get the values of R, start, and end from the user
    R = float(R_entry.get())
    start = float(start_entry.get())
    end = float(end_entry.get())

    # Generate x values
    x = np.linspace(start, end, 100)

    # Calculate y values
    y = [func(d, R) for d in x]

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, color='red', linestyle='-', linewidth=2, marker='o', markersize=4)

    # Customize the plot
    ax.set_xlabel('Number of Dimensions', fontsize=12)
    ax.set_ylabel(f'Volume of R = {R}', fontsize=12)

    # Generate the equation string
    equation = r'$\frac{\pi^{(\frac{D}{2})} \cdot R^D}{\Gamma(1+\frac{D}{2})}$'

    # Set the plot title with the equation
    ax.set_title('Plot of ' + equation, fontsize=14)

    # Add grid lines
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    # Set tick label font size
    ax.tick_params(axis='both', labelsize=10)

    # Show the plot
    plt.show()

# Function to open the default Excel data file
def open_excel_default():
    # Get the values of R, start, and end from the user
    R = float(R_entry.get())
    start = float(start_entry.get())
    end = float(end_entry.get())

    x = np.linspace(start, end, 100)

    # Calculate y values
    y = [func(d, R) for d in x]

    # Create a DataFrame with the data
    data = pd.DataFrame({'Number of Dimensions': x, 'Volume': y})

    # Save the data to an Excel file
    file_path = f'graph_data_R{R}_start{start}_end{end}.xlsx'
    data.to_excel(file_path, index=False)

    try:
        # Open the Excel file with the default program
        os.system(f'start excel "{os.path.abspath(file_path)}"')
    except Exception as e:
        print(f"Error opening Excel file: {e}")

# Create the GUI window
window = tk.Tk()
window.title("Hypersphere Volume Calculator & Grapher")
window.geometry("600x400")  # Set the window size

# Set font style
font_style = ("Times New Roman", 12)

# Create labels and entry fields for R, start, and end
R_label = tk.Label(window, text="Radius:", font=font_style)
R_label.pack()
R_entry = tk.Entry(window, font=font_style)
R_entry.pack()

start_label = tk.Label(window, text="Initial Dimension:", font=font_style)
start_label.pack()
start_entry = tk.Entry(window, font=font_style)
start_entry.pack()

end_label = tk.Label(window, text="Final Dimension:", font=font_style)
end_label.pack()
end_entry = tk.Entry(window, font=font_style)
end_entry.pack()

# Create buttons for generating the graph, opening Excel data, and canceling
generate_graph_button = tk.Button(window, text="Generate Graph", command=generate_graph, font=font_style)
generate_graph_button.pack()

open_excel_button = tk.Button(window, text="Show Excel Data", command=open_excel_default, font=font_style)
open_excel_button.pack()

cancel_button = tk.Button(window, text="Cancel", command=window.destroy, font=font_style)
cancel_button.pack()

# Run the GUI
window.mainloop()