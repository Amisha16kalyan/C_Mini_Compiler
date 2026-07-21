import tkinter as tk
import subprocess
import time

def compile_code():
    # Get code from input box
    source_code = input_text.get("1.0", tk.END)

    # Save code to test.txt
    with open("/home/satendra/Downloads/x86_compiler_web/x86_64_compiler-main/src/test.txt", "w") as f:
        f.write(source_code)

    result = subprocess.run(["bash", "/home/satendra/Downloads/x86_compiler_web/x86_64_compiler-main/src/run.sh", "test.txt"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


    print(result)

    # Load assembly output from chat.s
    time.sleep(5)
    try:
        with open("/home/satendra/Downloads/x86_compiler_web/x86_64_compiler-main/src/chat.s", "r") as f:
            output = f.read()
    except FileNotFoundError:
        output = "Compiler error: chat.s not found."

    # Show compiler output
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)

    # Show terminal output (stdout + stderr)
    terminal_output = result.stdout + "\n" + result.stderr
    terminal_text.delete("1.0", tk.END)
    terminal_text.insert(tk.END, terminal_output.strip())

# Create GUI window
root = tk.Tk()
root.title("x86-64 Compiler GUI")

# Input Label and Text Box
tk.Label(root, text="Enter Code:").pack()
input_text = tk.Text(root, height=12, width=80)
input_text.pack()

# Compile Button
tk.Button(root, text="Compile", command=compile_code).pack(pady=8)

# Assembly Output Section
tk.Label(root, text="Assembly Output (from chat.s):").pack()
output_text = tk.Text(root, height=10, width=80, bg="#f0f0f0")
output_text.pack()

# Terminal Output Section
tk.Label(root, text="Terminal Output (from run.sh):").pack()
terminal_text = tk.Text(root, height=10, width=80, bg="#e0e0e0")
terminal_text.pack()

# Start the GUI
root.mainloop()

