#include <iostream>
#include "speaker.h"

Speaker::Speaker(string name){
    this->name = name;
    score[0] = 0;
    score[1] = 0;
}
Speaker::Speaker(){
    this->name = " ";
    score[0] =0;
    score[1] = 0;
    
}