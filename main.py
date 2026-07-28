import tkinter as tk

# Főablak létrehozása
window = tk.Tk()

# A jelszó elemzéséhez szükséges függvény
def analyze_password():

    # A beviteli mező tartalmának kiolvasása
    password = password_entry.get()

    # Ellenőrizzük, hogy üres-e a mező
    if password == "":
        result_label.config(
            text="Bitte geben Sie ein Passwort ein!",
            fg="red"
        )
    else:
        result_label.config(
            text="Das Passwort wurde erkannt.",
            fg="green"
        )

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
    text="Passwort analysieren",
    command=analyze_password
)
analyze_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Program indítása
window.mainloop()