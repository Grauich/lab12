import tkinter as tk
from tkinter import messagebox
from l12lab31 import IceCreamStand

class IceCreamStandApp:
    def __init__(self, root, ice_cream_stand):
        self.root = root
        self.ice_cream_stand = ice_cream_stand
        self.root.title("Кафе-мороженое")

        self.label_title = tk.Label(root, text=ice_cream_stand.restaurant_name, font=('Arial', 18))
        self.label_title.pack(pady=10)

        self.label_location = tk.Label(root, text=f"Адрес: {ice_cream_stand.location}", font=('Arial', 12))
        self.label_location.pack(pady=5)
        self.label_hours = tk.Label(root, text=f"Часы работы: {ice_cream_stand.hours}", font=('Arial', 12))
        self.label_hours.pack(pady=5)

        self.label_flavors = tk.Label(root, text="Сорта мороженого:", font=('Arial', 14))
        self.label_flavors.pack(pady=10)
        self.flavors_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=('Arial', 12))
        self.flavors_listbox.pack(pady=10, padx=20)

        self.update_flavors_listbox()

        self.entry_flavor = tk.Entry(root, font=('Arial', 12))
        self.entry_flavor.pack(pady=5)

        self.button_add_flavor = tk.Button(root, text="Добавить сорт", command=self.add_flavor, font=('Arial', 12))
        self.button_add_flavor.pack(pady=5)
        self.button_remove_flavor = tk.Button(root, text="Удалить сорт", command=self.remove_flavor, font=('Arial', 12))
        self.button_remove_flavor.pack(pady=5)

    def update_flavors_listbox(self):
        self.flavors_listbox.delete(0, tk.END)
        for flavor in self.ice_cream_stand.flavors:
            self.flavors_listbox.insert(tk.END, flavor)

    def add_flavor(self):
        flavor = self.entry_flavor.get()
        if flavor:
            self.ice_cream_stand.add_flavors(flavor)
            self.update_flavors_listbox()
            self.entry_flavor.delete(0, tk.END)
        else:
            messagebox.showwarning("Внимание", "Введите сорт мороженого!")

    def remove_flavor(self):
        selected_flavor = self.flavors_listbox.curselection()
        if selected_flavor:
            flavor = self.flavors_listbox.get(selected_flavor)
            self.ice_cream_stand.remove_flavors(flavor)
            self.update_flavors_listbox()
        else:
            messagebox.showwarning("Внимание", "Выберите сорт мороженого для удаления!")

if __name__ == "__main__":
    ice_cream_stand = IceCreamStand("Frozen Delights", "Кафе-мороженое", "ул. Пушкина, д. 10", "с 10:00 до 22:00", 4.2)
    ice_cream_stand.add_flavors("Шоколадное", "Ванильное", "Клубничное", "Фисташковое")

    root = tk.Tk()
    app = IceCreamStandApp(root, ice_cream_stand)
    root.mainloop()
