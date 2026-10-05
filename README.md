# Автоматизация теста к API
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest
- Структура проекта
diplom/
│  configuration.py         # URL стенда и пути к API
│  data.py                  # Данные для запросов
│  test_order.py            # Тесты
│  README.md                # Этот файл
│  sender_stand_request.py  # Функции отправки POST и GET запросов
└── .venv/                  # Виртуальное окружение
└── .pytest_cache/          # Кэш Pytest
