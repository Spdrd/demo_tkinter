import customtkinter as ctk
from tkinter import ttk

class table_display():
    def __init__(self, app, headings, data):
        frame = ctk.CTkToplevel(app)
        frame.pack(expand=True, fill="both")

        table = ttk.Treeview(frame, columns=headings, show="headings")
        table.pack(fill="both")

        for heading in headings:
            table.heading(heading, text=heading)
            table.column(heading, width=100, anchor="center")

        for row in data:
            table.insert("", "end", values=row)

def main():
    app = ctk.CTk()
    frame = table_display(app, ["ID", "Codigo", "Ciudad"], [(1, "BOG", "Bogota"), (2, "CAL", "Cali")])
    app.mainloop()

if __name__ == "__main__":
    main()