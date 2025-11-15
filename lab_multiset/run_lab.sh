#!/bin/bash

echo "============================"
cd "$(dirname "$0")"
g++ -std=c++17 main.cpp Multiset.cpp -o multiset_app

if [ $? -ne 0 ]; then
    echo " Ошибка компиляции!"
    exit 1
fi
echo "============================"
./multiset_app
