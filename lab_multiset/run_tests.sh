#!/bin/bash
echo "=================================="
cd "$(dirname "$0")"
rm -rf coverage_tests coverage_report.html
find . -name "*.gcda" -delete
find . -name "*.gcno" -delete
echo "🔨 Сборка тестов..."
g++ -std=c++17 -fprofile-arcs -ftest-coverage -I/opt/homebrew/include -L/opt/homebrew/lib tests.cpp Multiset.cpp -o coverage_tests -lgtest -lgtest_main -pthread

if [ $? -ne 0 ]; then
 
    exit 1
fi

./coverage_tests

gcovr -r . --html --html-details -o coverage_report.html

if[ $? -eq 0 ]; then
    open coverage_report.html
else
    echo  " не установлен, установите: pip install gcovr"
    # Альтернатива через gcov
    gcov Multiset.cpp
    gcov tests.cpp
    echo " Текстовые отчеты созданы: *.gcov"
fi

echo "=================================="

