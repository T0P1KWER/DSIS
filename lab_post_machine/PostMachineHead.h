#ifndef POSTMACHINEHEAD_H
#define POSTMACHINEHEAD_H

#include "PostMachineTape.h"

class PostMachineHead {
private:
    int currentPosition;
    PostMachineTape& tapeRef;

public:
    PostMachineHead(PostMachineTape& tape);
    int getCurrentPosition() const;
    void setPosition(int position);
    bool read() const;
    void write(bool value);
    void moveLeft();
    void moveRight();
};

#endif