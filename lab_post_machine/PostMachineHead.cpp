#include "PostMachineHead.h"

PostMachineHead::PostMachineHead(PostMachineTape& tape) : currentPosition(0), tapeRef(tape) {}

int PostMachineHead::getCurrentPosition() const {
    return currentPosition;
}

void PostMachineHead::setPosition(int position) {
    currentPosition = position;
}

bool PostMachineHead::read() const {
    return tapeRef.getValue(currentPosition);
}

void PostMachineHead::write(bool value) {
    tapeRef.setValue(currentPosition, value);
}

void PostMachineHead::moveLeft() {
    currentPosition--;
}

void PostMachineHead::moveRight() {
    currentPosition++;
}