import tkinter as tk
from tkinter import scrolledtext, END
from blossom_ai import Blossom

# Инициализация AI (без токена — анонимный режим)
ai = Blossom()

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chat")
        self.root.geometry("600x500")
        self.root.resizable(True, True)

        # Поле чата (только для чтения)
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', bg="#f0f0f0")
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Поле ввода
        self.user_input = tk.Entry(root, font=("Arial", 12))
        self.user_input.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.user_input.bind("<Return>", self.send_message)

        # Кнопка отправки
        self.send_button = tk.Button(root, text="Отправить", command=self.send_message)
        self.send_button.pack(pady=(0, 10))

        self.add_message("Бот", "Привет! Я — Blossom AI. Задай мне любой вопрос 🌸")

    def add_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(END, f"{sender}: {message}\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview(END)

    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return

        self.add_message("Вы", user_text)
        self.user_input.delete(0, END)

        try:
            # Генерация ответа через Blossom AI
            response = ai.text.generate(user_text)
            self.add_message("Бот", response)
        except Exception as e:
            self.add_message("Бот", f"Ошибка: {str(e)}\nПопробуйте позже.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()