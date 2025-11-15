#include "Menu.h"
#include <iostream>
#include <string>

void displayMenu() {
    std::cout << "\n=== Меню работы с Машиной Поста ===" << std::endl;
    std::cout << "1. Загрузить программу из файла" << std::endl;
    std::cout << "2. Загрузить состояние ленты из файла" << std::endl;
    std::cout << "3. Добавить команду вручную" << std::endl;
    std::cout << "4. Просмотреть все команды программы" << std::endl;
    std::cout << "5. Изменить значение на ленте" << std::endl;
    std::cout << "6. Запуск полной интерпретации программы" << std::endl;
    std::cout << "7. Выполнить один шаг (++)" << std::endl;
    std::cout << "8. Сбросить состояние (--)" << std::endl;
    std::cout << "9. Показать текущее состояние" << std::endl;
    std::cout << "0. Выход" << std::endl;
    std::cout << "Выберите действие: ";
}

void autoRun(int argc, char* argv[], PostMachine& machine) {
    std::string programFile, tapeFile;
    bool logging = false;

    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];
        if (arg == "-log") {
            logging = true;
            machine.enableLogging();
            std::cout << "Логирование включено" << std::endl;
        } else {
            if (programFile.empty()) {
                programFile = arg;
            } else if (tapeFile.empty()) {
                tapeFile = arg;
            }
        }
    }

    if (programFile.empty() || tapeFile.empty()) {
        std::cout << "Использование: " << argv[0] << " <файл_программы> <файл_ленты> [-log]" << std::endl;
        std::cout << "Пример: " << argv[0] << " program.txt tape.txt -log" << std::endl;
        return;
    }

    machine.loadProgramFromFile(programFile);
    machine.loadTapeFromFile(tapeFile);
    machine.start();
}