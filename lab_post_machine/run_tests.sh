#!/bin/bash

echo "🧪 ЗАПУСК ТЕСТОВ МАШИНЫ ПОСТА С ПОКРЫТИЕМ"
echo "========================================"

# Переходим в папку скрипта
cd "$(dirname "$0")"

# Очистка предыдущих данных
echo "🧹 Очистка старых файлов..."
rm -rf coverage_tests coverage_report.html
find . -name "*.gcda" -delete 2>/dev/null
find . -name "*.gcno" -delete 2>/dev/null

echo "🔨 Компиляция тестов с покрытием кода..."
# Компилируем с флагами покрытия
g++ -std=c++17 -fprofile-arcs -ftest-coverage \
    -I/opt/homebrew/include -L/opt/homebrew/lib \
    tests.cpp \
    PostMachineCommand.cpp \
    PostMachineTape.cpp \
    PostMachineHead.cpp \
    PostMachine.cpp \
    Menu.cpp \
    -o coverage_tests -lgtest -lgtest_main -pthread

# Проверяем успешность компиляции
if [ $? -ne 0 ]; then
    echo "❌ Ошибка компиляции тестов!"
    exit 1
fi

echo "✅ Тесты успешно скомпилированы"
echo "🧪 Запуск тестов..."
echo "----------------------------------------"

# Запускаем тесты
./coverage_tests

echo "----------------------------------------"
echo "📊 Генерация отчета покрытия..."

# Проверяем установлен ли gcovr
if command -v gcovr &> /dev/null; then
    echo "📈 Создание HTML отчета..."
    gcovr -r . --html --html-details -o coverage_report.html
    
    echo "📊 Статистика покрытия:"
    gcovr -r .
    
    # Открываем отчет в браузере
    echo "🌐 Открываю отчет в браузере..."
    open coverage_report.html
else
    echo "⚠️  gcovr не установлен, устанавливаю..."
    pip install gcovr
    
    if [ $? -eq 0 ]; then
        echo "📈 Создание HTML отчета..."
        gcovr -r . --html --html-details -o coverage_report.html
        echo "📊 Статистика покрытия:"
        gcovr -r .
        open coverage_report.html
    else
        echo "❌ Не удалось установить gcovr"
        echo "📄 Создаю текстовые отчеты через gcov..."
        gcov *.cpp 2>/dev/null
        echo "📋 Текстовые отчеты созданы в файлах *.gcov"
    fi
fi

echo "========================================"
echo "🎉 ТЕСТИРОВАНИЕ ЗАВЕРШЕНО!"
echo "📁 Отчет покрытия: coverage_report.html"
