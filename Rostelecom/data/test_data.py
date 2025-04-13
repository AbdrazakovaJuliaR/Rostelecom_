# data/test_data.py
import os
from dotenv import load_dotenv

if not load_dotenv():
    print("Ошибка загрузки .env файла!")

valid_email = os.getenv("EMAIL")
valid_phone = os.getenv("PHONE")
valid_login = os.getenv("LOGIN")
valid_password = os.getenv("PASSWORD")

invalid_password = "WrongPass123"

valid_account = "123456789012"  # тестовый лицевой счёт

#TC-12
new_email = "new_user@example.com"
new_phone = "+79009998877"
new_first_name = "Тест"
new_last_name = "Пользователь"
new_password = "Qwerty123"

#для страницы восстановления
recovery_email = "test_user@example.com"
recovery_phone = "+79001112233"

#Код из СМС / почты
otp_email = "otp_test@example.com"
otp_phone = "+79001112233"

