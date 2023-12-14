# -*- coding: utf-8 -*-
"""
Created on Tue Dec 5 13:07:01 2023

@author: isaia
"""

import tkinter as tk
from tkinter import ttk, filedialog

def update_shielding_material():
    # Retrieve the selected material name
    selected_material_name = material_combobox.get()

    # Correlate the material name to material number and density
    material_correlations = {
        "Air": (1, 0.001205),
        "Pure SIS Copolymer": (2, 0.91),
        "50% Tungsten SIS Blend": (3, 10.095),
        "50% Bismuth SIS Blend": (4, 5.3295),
        "50% Titanium SIS Blend": (5, 2.715),
        "Pure Aluminum": (6, 2.7),
        "50% Copper SIS Blend": (7, 4.935),
        "50% v/v Blended & SIS": (8, 6.835),
        "50% v/v BN SIS Composite": (9, 1.2075),
        "Silicon Chip": (10, 2.329)
    }

    # Get the material number and density based on the selected material name
    material_number, new_density = material_correlations[selected_material_name]

    # Construct the updated shielding material line
    updated_shielding_line = f"3     {material_number}  -{new_density}  -3 2                  $Shielding"

    # Update the input content with the new shielding material line
    updated_input_content = original_input_content.replace(current_shielding_line, updated_shielding_line)

    # Save the updated MCNP input file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("MCNP files", "*.txt")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write(updated_input_content)
        status_label.config(text=f"MCNP input file saved: {file_path}")

# Read the original MCNP input file content
with open("50PercentVolume_Cosmic_System.txt", 'r') as original_file:
    original_input_content = original_file.read()

# Find the line containing the current shielding material
current_shielding_line_start = original_input_content.find("$Shielding")
current_shielding_line_end = original_input_content.find("\n", current_shielding_line_start)
current_shielding_line = original_input_content[current_shielding_line_start:current_shielding_line_end]

# Create the main window
root = tk.Tk()
root.title("MCNP Shielding Material Adjuster")

# Material Selection
material_label = tk.Label(root, text="Select Material:")
material_label.pack()

# Material names
material_options = ["Air", "Pure SIS Copolymer", "50% Tungsten SIS Blend",
                    "50% Bismuth SIS Blend", "50% Titanium SIS Blend",
                    "Pure Aluminum", "50% Copper SIS Blend",
                    "50% v/v Blended & SIS", "50% v/v BN SIS Composite",
                    "Silicon Chip"]

material_combobox = ttk.Combobox(root, values=material_options)
material_combobox.set(material_options[0])
material_combobox.pack()

# Update Button
update_button = tk.Button(root, text="Update Shielding Material", command=update_shielding_material)
update_button.pack()

# Status Label
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()



