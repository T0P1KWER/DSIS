#ifndef POSTMACHINECOMMAND_H
#define POSTMACHINECOMMAND_H

class PostMachineCommand {
private:
    int id;
    bool condition;
    char action;
    int nextCommandId;

public:
    PostMachineCommand();
    PostMachineCommand(int cmdId, bool cond, char act, int nextId);
    
    int getId() const;
    bool getCondition() const;
    char getAction() const;
    int getNextCommandId() const;
};

#endif