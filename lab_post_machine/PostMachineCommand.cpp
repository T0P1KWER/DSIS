#include "PostMachineCommand.h"

PostMachineCommand::PostMachineCommand() : id(0), condition(false), action(' '), nextCommandId(0) {}

PostMachineCommand::PostMachineCommand(int cmdId, bool cond, char act, int nextId)
    : id(cmdId), condition(cond), action(act), nextCommandId(nextId) {}

int PostMachineCommand::getId() const { return id; }
bool PostMachineCommand::getCondition() const { return condition; }
char PostMachineCommand::getAction() const { return action; }
int PostMachineCommand::getNextCommandId() const { return nextCommandId; }