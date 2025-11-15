#ifndef POSTMACHINE_H
#define POSTMACHINE_H

#include <map>
#include <string>
#include "PostMachineCommand.h"
#include "PostMachineTape.h"
#include "PostMachineHead.h"

class PostMachine {
private:
    PostMachineTape tape;
    PostMachineHead head;
    std::map<int, PostMachineCommand> program;
    int currentCommandId;
    bool halted;  // ПЕРЕИМЕНОВАЛ isHalted -> halted
    bool logging;
    int stepCount;

public:
    PostMachine();
    void enableLogging();
    PostMachine& operator++();
    PostMachine operator++(int);
    PostMachine& operator--();
    PostMachine operator--(int);
    bool executeStep();
    void start();
    void reset();
    void printCurrentState() const;
    bool isHalted() const;  // Оставил метод с таким именем
    int getCurrentCommand() const;
    void changeTapeValue(int position, bool value);
    void addCommand(const PostMachineCommand& cmd);
    void loadProgramFromFile(const std::string& filename);
    void loadTapeFromFile(const std::string& filename);
    void printAllCommands();
};

#endif