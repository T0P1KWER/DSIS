#include "PostMachine.h"
#include <fstream>
#include <sstream>
#include <iostream>

PostMachine::PostMachine() : tape(), head(tape) {
    currentCommandId = 1;
    halted = false;
    logging = false;
    stepCount = 0;
}

void PostMachine::enableLogging() {
    logging = true;
}

PostMachine& PostMachine::operator++() {
    executeStep();
    return *this;
}

PostMachine PostMachine::operator++(int) {
    PostMachine temp = *this;
    executeStep();
    return temp;
}

PostMachine& PostMachine::operator--() {
    reset();
    return *this;
}

PostMachine PostMachine::operator--(int) {
    PostMachine temp = *this;
    reset();
    return temp;
}

bool PostMachine::executeStep() {
    if (halted || currentCommandId == 0) {
        if (logging) {
            std::cout << "Машина уже остановлена!" << std::endl;
        }
        return false;
    }

    if (program.count(currentCommandId) == 0) {
        std::cout << "Ошибка: команда " << currentCommandId << " не найдена!" << std::endl;
        halted = true;
        return false;
    }

    stepCount++;
    PostMachineCommand cmd = program[currentCommandId];
    bool condition = cmd.getCondition();
    char action = cmd.getAction();
    int nextCommand = cmd.getNextCommandId();

    if (logging) {
        std::cout << "\n=== Шаг " << stepCount << " ===" << std::endl;
        std::cout << "Команда: " << currentCommandId << std::endl;
        std::cout << "Позиция головки: " << head.getCurrentPosition() << std::endl;
        std::cout << "Условие: " << (condition ? "метка" : "пусто") << std::endl;
        std::cout << "Действие: " << action << std::endl;
        bool currentCell = head.read();
        std::cout << "Текущая ячейка: " << (currentCell ? "метка" : "пусто") << std::endl;
    }

    bool currentCell = head.read();

    if (currentCell == condition) {
        if (logging) {
            std::cout << "Условие выполнено! Выполняю действие..." << std::endl;
        }
        switch (action) {
        case 'V': case 'v':
            head.write(true);
            if (logging) std::cout << "Поставил метку в ячейке " << head.getCurrentPosition() << std::endl;
            break;
        case 'X': case 'x':
            head.write(false);
            if (logging) std::cout << "Стер метку в ячейке " << head.getCurrentPosition() << std::endl;
            break;
        case 'L': case 'l':
            head.moveLeft();
            if (logging) std::cout << "Двинулся влево -> позиция " << head.getCurrentPosition() << std::endl;
            break;
        case 'R': case 'r':
            head.moveRight();
            if (logging) std::cout << "Двинулся вправо -> позиция " << head.getCurrentPosition() << std::endl;
            break;
        default:
            if (logging) std::cout << "Неизвестное действие!" << std::endl;
            break;
        }
    } else {
        if (logging) {
            std::cout << "Условие не выполнено - пропускаю действие" << std::endl;
        }
    }

    currentCommandId = nextCommand;

    if (currentCommandId == 0) {
        halted = true;
        if (logging) {
            std::cout << "Программа завершена!" << std::endl;
        }
    }

    if (logging) {
        tape.printTapeState(head.getCurrentPosition() - 5, head.getCurrentPosition() + 5);
        std::cout << "Следующая команда: " << (currentCommandId == 0 ? "СТОП" : std::to_string(currentCommandId)) << std::endl;
    }

    return true;
}

void PostMachine::start() {
    std::cout << "Запуск полной интерпретации программы..." << std::endl;
    while (executeStep() && stepCount < 1000) {}
    std::cout << "\nИнтерпретация завершена. Выполнено шагов: " << stepCount << std::endl;
}

void PostMachine::reset() {
    currentCommandId = 1;
    halted = false;
    stepCount = 0;
    for (int i = -50; i <= 50; i++) {
        tape.changeValue(i, false);
    }
    head.setPosition(0);
    std::cout << "Состояние машины сброшено" << std::endl;
}

void PostMachine::printCurrentState() const {
    std::cout << "\nТекущее состояние машины:" << std::endl;
    std::cout << "Текущая команда: " << currentCommandId << std::endl;
    std::cout << "Позиция головки: " << head.getCurrentPosition() << std::endl;
    std::cout << "Состояние текущей ячейки: " << (head.read() ? "метка" : "пусто") << std::endl;
    std::cout << "Выполнено шагов: " << stepCount << std::endl;
    std::cout << "Статус: " << (halted ? "ОСТАНОВЛЕНА" : "РАБОТАЕТ") << std::endl;
}

bool PostMachine::isHalted() const {
    return halted;
}

int PostMachine::getCurrentCommand() const {
    return currentCommandId;
}

void PostMachine::changeTapeValue(int position, bool value) {
    tape.changeValue(position, value);
}

void PostMachine::addCommand(const PostMachineCommand& cmd) {
    program[cmd.getId()] = cmd;
    std::cout << "Команда " << cmd.getId() << " успешно добавлена!" << std::endl;
}

void PostMachine::loadProgramFromFile(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cout << "Ошибка: не удалось открыть файл " << filename << std::endl;
        return;
    }
    program.clear();
    std::string line;
    while (std::getline(file, line)) {
        if (line.empty()) continue;
        int id, nextId;
        bool condition;
        char action;
        std::istringstream iss(line);
        if (iss >> id >> condition >> action >> nextId) {
            addCommand(PostMachineCommand(id, condition, action, nextId));
        }
    }
    file.close();
    std::cout << "Программа загружена из файла: " << filename << std::endl;
}

void PostMachine::loadTapeFromFile(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cout << "Ошибка: не удалось открыть файл " << filename << std::endl;
        return;
    }
    tape.loadFromStream(file);
    file.close();
    std::cout << "Лента загружена из файла: " << filename << std::endl;
}

void PostMachine::printAllCommands() {
    if (program.empty()) {
        std::cout << "Программа пуста!" << std::endl;
        return;
    }
    std::cout << "Все команды в программе:" << std::endl;
    for (const auto& cmd : program) {
        std::cout << "Команда №" << cmd.first << ": ";
        std::cout << "усл=" << cmd.second.getCondition() << ", ";
        std::cout << "действие=" << cmd.second.getAction() << ", ";
        std::cout << "след=" << cmd.second.getNextCommandId() << std::endl;
    }
}