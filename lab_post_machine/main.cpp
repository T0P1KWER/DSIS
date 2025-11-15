#include <iostream>
#include "PostMachine.h"
#include "Menu.h"

int main(int argc, char* argv[]) {
    setlocale(LC_ALL, "Russian");
    PostMachine machine;

    if (argc > 1) {
        autoRun(argc, argv, machine);
        return 0;
    }

    int choice;
    do {
        displayMenu();
        std::cin >> choice;
        std::cin.ignore();

        switch (choice) {
        case 1: {
            std::string filename;
            std::cout << "Введите имя файла с программой: ";
            std::getline(std::cin, filename);
            machine.loadProgramFromFile(filename);
            break;
        }
        case 2: {
            std::string filename;
            std::cout << "Введите имя файла с состоянием ленты: ";
            std::getline(std::cin, filename);
            machine.loadTapeFromFile(filename);
            break;
        }
        case 3: {
            int id, nextId;
            bool condition;
            char action;
            std::cout << "Введите номер команды: ";
            std::cin >> id;
            std::cout << "Введите условие (0-пусто, 1-метка): ";
            std::cin >> condition;
            std::cout << "Введите действие (V-метка, X-стереть, L-влево, R-вправо): ";
            std::cin >> action;
            std::cout << "Введите следующую команду (0-стоп): ";
            std::cin >> nextId;
            machine.addCommand(PostMachineCommand(id, condition, action, nextId));
            break;
        }
        case 4:
            machine.printAllCommands();
            break;
        case 5: {
            int cell;
            bool value;
            std::cout << "Введите ячейку которую хотите поменять: ";
            std::cin >> cell;
            std::cout << "Введите значение (0-пусто, 1-метка): ";
            std::cin >> value;
            machine.changeTapeValue(cell, value);
            break;
        }
        case 6:
            machine.start();
            break;
        case 7:
            std::cout << "Выполняю один шаг программы..." << std::endl;
            ++machine;
            break;
        case 8:
            std::cout << "Сбрасываю состояние машины..." << std::endl;
            --machine;
            break;
        case 9:
            machine.printCurrentState();
            break;
        case 0:
            std::cout << "Выход из программы." << std::endl;
            break;
        default:
            std::cout << "Неверный выбор!" << std::endl;
        }
    } while (choice != 0);

    return 0;
}