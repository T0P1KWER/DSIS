#!/bin/bash

# Переходим в директорию скрипта (на случай, если запущен из другого места)
cd "$(dirname "$0")" || exit 1

echo " Активация виртуального окружения..."
source .venv/bin/activate

echo "Проверка и установка coverage (если нужно)..."
if ! python -c "import coverage" &> /dev/null; then
    echo "   Установка coverage..."
    pip install coverage
else
    echo "   coverage уже установлен."
fi

echo " Запуск тестов с покрытием..."
python -m coverage run -m unittest tests.test_all

echo -e "\n Отчёт о покрытии:"
python -m coverage report -m

echo -e "\n Готово! Покрытие показано выше."