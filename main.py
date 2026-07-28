import tkinter as tk

# Főablak létrehozása
window = tk.Tk()

# Ablak címe
window.title("Password Security Analyzer")

# Ablak mérete
window.geometry("500x400")

# Cím
title = tk.Label(
    window,
    text="Password Security Analyzer",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

# Jelszó felirat
password_label = tk.Label(window, text="Passwort:")
password_label.pack()

# Jelszó beviteli mező
password_entry = tk.Entry(window, show="*", width=30)
password_entry.pack(pady=10)

# Gomb
analyze_button = tk.Button(
    window,
    text="Passwort analysieren"
)
analyze_button.pack(pady=20)

# Program indítása
window.mainloop()