from tkinter import messagebox
updating = False

def start_update():
    global updating
    if updating:
        print("Update blocked")
        return False
    print("Starting update")
    updating = True
    return True

def end_update():
    global updating
    print("Ending update")
    updating = False

def clamp(value, min_value=0, max_value=255):
    return max(min_value, min(value, max_value))

def warn_if_clamped(original_value, clamped_value):
    if original_value != clamped_value:
        messagebox.showwarning("Warning", f"Value {original_value} was clamped to {clamped_value} to fit the color model limits.")
