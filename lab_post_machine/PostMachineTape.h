#ifndef POSTMACHINETAPE_H
#define POSTMACHINETAPE_H

#include <map>
#include <iostream>

class PostMachineTape {
private:
    std::map<int, bool> cells;

public:
    PostMachineTape();
    bool getValue(int pos) const;
    void changeValue(int pos, bool value);
    void loadFromStream(std::istream& is);
    void setValue(int pos, bool mark);
    void printTapeState(int from = -10, int to = 10) const;
};

#endif