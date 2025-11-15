#!/bin/bash


echo "======================"
cd "$(dirname "$0")"
g++ -std=c++17 \
    main.cpp \
    PostMachineCommand.cpp \
    PostMachineTape.cpp \
    PostMachineHead.cpp \
    PostMachine.cpp \
    Menu.cpp \
    -o post_machine

# Проверяем успешность компиляции
if [ $? -ne 0 ]; then
    echo " Ошибка компиляции! Проверьте код."
    exit 1
fi

./post_machine

echo "======================"
