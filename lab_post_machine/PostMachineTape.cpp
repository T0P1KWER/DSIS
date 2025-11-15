#include "PostMachineTape.h"

PostMachineTape::PostMachineTape() {
    for (int i = -50; i <= 50; i++) {
        cells[i] = false;
    }
}

bool PostMachineTape::getValue(int pos) const {
    return cells.at(pos);
}

void PostMachineTape::changeValue(int pos, bool value) {
    cells[pos] = value;
    std::cout << "Ячейка " << pos << " изменена на: " << (value ? "1 (метка)" : "0 (пусто)") << std::endl;
}

void PostMachineTape::loadFromStream(std::istream& is) {
    std::string tapeData;
    is >> tapeData;
    for (int i = 0; i < tapeData.length(); i++) {
        setValue(i, tapeData[i] == '1');
    }
}

void PostMachineTape::setValue(int pos, bool mark) {
    cells[pos] = mark;
}

void PostMachineTape::printTapeState(int from, int to) const {
    std::cout << "Состояние ленты: ";
    for (int i = from; i <= to; i++) {
        std::cout << (getValue(i) ? "1" : "0");
    }
    std::cout << std::endl;
}