import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_key():
    # Получаем число, которое ввёл пользователь
    number = entry_number.get().strip()

    # Проверяем, что введено ровно 6 цифр
    if len(number) != 6 or not number.isdigit():
        messagebox.showerror(
            "Ошибка",
            "Введите ровно 6 цифр (десятичное число)."
        )
        return

    # Берём 4-ю, 5-ю и 6-ю цифры и перемешиваем их
    first_digits = list(number[3:6])
    random.shuffle(first_digits)
    first_number = ''.join(first_digits)

    # Берём 1-ю, 2-ю и 3-ю цифры и тоже перемешиваем
    second_digits = list(number[0:3])
    random.shuffle(second_digits)
    second_number = ''.join(second_digits)

    # Создаём по две случайные заглавные английские буквы
    first_letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    second_letters = ''.join(random.choices(string.ascii_uppercase, k=2))

    # Формируем первые два блока ключа
    first_block = first_number + first_letters
    second_block = second_number + second_letters

    # Складываем числа, получившиеся в первых двух блоках
    total = int(first_number) + int(second_number)

    # Записываем сумму четырьмя цифрами, добавляя нули слева
    third_block = str(total).zfill(4)

    # Собираем весь ключ в нужном формате
    key = first_block + "-" + second_block + " " + third_block

    # Показываем полученный ключ в поле результата
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.insert(0, key)
    entry_result.config(state="readonly")


# Создаём главное окно программы
window = tk.Tk()
window.title("Генератор ключей — вариант 10")
window.geometry("800x600")
window.resizable(False, False)

# Загружаем фоновую картинку из файла рядом с программой
try:
    background_image = tk.PhotoImage(file="1640456808_14-abrakadabra-fun-p-fon-fifa-mobail-14.png")
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except tk.TclError:
    # Если картинка не найдена, используем обычный цвет фона
    window.configure(bg="#dce6f2")
    messagebox.showwarning(
        "Фоновая картинка",
        "Файл 1640456808_14-abrakadabra-fun-p-fon-fifa-mobail-14.png не найден. Программа запустится без картинки."
    )

# Создаём светлую панель, чтобы текст был хорошо виден
frame = tk.Frame(window, bg="white", padx=25, pady=25)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Заголовок окна
title_label = tk.Label(
    frame,
    text="ГЕНЕРАТОР КЛЮЧЕЙ",
    font=("Arial", 20, "bold"),
    bg="white"
)
title_label.pack(pady=10)

# Подсказка для ввода числа
input_label = tk.Label(
    frame,
    text="Введите десятичное число из 6 цифр:",
    font=("Arial", 12),
    bg="white"
)
input_label.pack(pady=5)

# Поле для ввода исходного числа
entry_number = tk.Entry(frame, font=("Arial", 16), justify="center", width=15)
entry_number.pack(pady=8)

# Кнопка запуска генерации ключа
generate_button = tk.Button(
    frame,
    text="Сгенерировать ключ",
    font=("Arial", 12),
    command=generate_key
)
generate_button.pack(pady=12)

# Подпись поля с результатом
result_label = tk.Label(
    frame,
    text="Ваш ключ:",
    font=("Arial", 12),
    bg="white"
)
result_label.pack(pady=5)

# Поле, в котором будет отображаться готовый ключ
entry_result = tk.Entry(
    frame,
    font=("Arial", 16, "bold"),
    justify="center",
    width=25,
    state="readonly"
)
entry_result.pack(pady=8)

# Кнопка закрытия программы
exit_button = tk.Button(
    frame,
    text="Выход",
    font=("Arial", 12),
    command=window.destroy
)
exit_button.pack(pady=12)

# Запускаем обработку действий пользователя
window.mainloop()
