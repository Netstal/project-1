from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.animation import Animation
import random
import string
import webbrowser

class PasswordGenerator(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.password_label = Label(text='Сгенерированный пароль будет здесь', size_hint=(1, 0.2))
        self.length_input = TextInput(text='12', multiline=False, input_type='number', background_color=(1, 1, 1, 1), size_hint=(1, 0.1))

        generate_button = Button(text='Сгенерировать пароль', on_press=self.generate_password, size_hint=(1, 0.1), background_color=(0.4, 0.8, 0.2, 1))
        copy_button = Button(text='Скопировать пароль', on_press=self.copy_password, size_hint=(1, 0.1), background_color=(0.8, 0.2, 0.4, 1))
        contact_dev_button = Button(text='Связь с разработчиком', on_press=self.contact_developer, size_hint=(1, 0.1), background_color=(0.2, 0.6, 0.9, 1))

        developer_label = Label(text='Разработчик: Алексей Руденко', size_hint=(1, 0.1))

        layout.add_widget(self.password_label)
        layout.add_widget(self.length_input)
        layout.add_widget(generate_button)
        layout.add_widget(copy_button)
        layout.add_widget(contact_dev_button)
        layout.add_widget(developer_label)

        return layout

    def generate_password(self, instance):
        # Анимация изменения цвета кнопки "Сгенерировать пароль"
        anim = Animation(background_color=(0.2, 0.8, 0.2, 1), duration=0.5) + Animation(background_color=(0.4, 0.8, 0.2, 1), duration=0.5)
        anim.start(instance)

        # Реализация генерации пароля
        if not self.length_input.text.isdigit():
            self.password_label.text = 'Ошибка! Введите длину пароля числом.'
            return

        length = int(self.length_input.text)
        if length < 8:
            self.password_label.text = 'Длина пароля должна быть не менее 8 символов.'
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.text = f'Сгенерированный пароль: {password}'

    def copy_password(self, instance):
        # Реализация копирования пароля с анимацией
        password = self.password_label.text.split(': ')[-1]
        Clipboard.copy(password)

        # Анимация изменения цвета кнопки копирования
        anim = Animation(background_color=(0.8, 0.2, 0.4, 1), duration=0.5) + Animation(background_color=(0.8, 0.2, 0.4, 1), duration=0.5)
        anim.start(instance)

        # Показать всплывающее окно с сообщением
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text='Пароль скопирован!'))
        popup = Popup(title='', content=popup_content, size_hint=(None, None), size=(400, 150), auto_dismiss=True)
        popup.open()
        Clock.schedule_once(popup.dismiss, 2.0)

    def contact_developer(self, instance):
        # Реализация связи с разработчиком
        developer_username = '@Admt_450'
        webbrowser.open(f'https://t.me/Admt_450')

if __name__ == '__main__':
    PasswordGenerator().run()