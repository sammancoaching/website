---
title: Martian Message
kata_name: martian_message
---

# Martin Message
In the film "The Martian" the hero who is stuck on Mars needs to communicate with Earth. He has a brilliant idea. He digs up the Pathfinder Rover, a primitive robot previously sent to the planet by NASA. He uses it to hack together a simple but usable communication channel. This kata is to reproduce the code that NASA would have written to send him messages.

The Pathfinder rover has a camera on the top of a long pole that can be rotated 360 degrees to take pictures of the martian terrain around it. It can send these pictures back to Earth. The hero on Mars can see which direction the camera is pointing in. That is the basis of the communication. 

Initially the hero activates the camera and puts a piece of paper with a written notice in front of it saying "Can you see this?" and then a similar paper notice on either side saying "Yes" and "No". NASA sees the pictures and is able to instruct the Pathfinder camera to point at the "Yes" notice. This is the breakthrough they need!

Rather than only being able to communicate via Yes/No questions, the hero switches the paper notices and makes a full circle of them around the camera. He decides all 26 letters of the alphabet would be too close together to distinguish between, so he instead puts signs for the numbers 0x0 - 0xF - that is the 16 first digits in Hex. NASA can point the camera at two hex numbers in sequence to indicate the ASCII code of a letter. The hero can decode it using an [ASCII-table](https://commons.wikimedia.org/wiki/File:ASCII-Table-wide.svg). In addition there is a "question card" to put at the end of a transmission, so 17 cards in total.

Your task is to write the code NASA would need to write to control the Pathfinder camera to send the hero the message:

    HOW ALIVE?

You can assume the Pathfinder rover contains a stepper motor that can move the camera either clockwise or anticlockwise. It begins pointing at 0x0. The camera should pause for 5 seconds pointing at each of the two Hex codes that make up a letter, and pause for 10 seconds between letters. Your solution should send the whole message clearly and without wasting time unnecessarily. This is some sample code in C showing the interface to the motor and a how to use it to control the speed and direction of the camera:

```c
// Stepper.h

// the number of steps to rotate a complete circle of 360 degrees
#define STEPS 2048

// the maximum motor speed in RPM
#define MAXIMUM_SPEED 15

class Stepper 
{
public:
    Stepper(const uint8_t pin1 = 8, const uint8_t pin2 = 9, const uint8_t pin3 = 10, const uint8_t pin4 = 11);
    
    // Set the speed of the motor in RPM. Maximum is defined above.
    void setSpeed(uint8_t);
    
    // move the indicated number of steps. The size of a step is defined above.
    void move_clockwise(uint8_t steps);
    void move_anticlockwise(uint8_t steps);
    
    // whether the motor is currently moving.
    bool isRunning();
}

// main.c
#include <Stepper.h> // Include the header file

// create an instance of the stepper class with suitable pins set up
Stepper stepper(8, 10, 9, 11);

// configure the stepper motor speed in RPM
stepper.setSpeed(10);

// move the motor the number of steps indicated by val
val = 42;
stepper.step(val);

// wait for the stepper to finish moving
while(stepper.isRunning()) {
    sleep(1);
}

```

## Quote from the movie

We’ll need to talk faster than yes/no questions every half hour. The camera can rotate 360 degrees, and I have plenty of antenna parts. Time to make an alphabet. But I can’t just use the letters A through Z. Twenty-six letters plus my question card would be twenty-seven cards around the lander. Each one would only get 13 degrees of arc. Even if JPL points the camera perfectly, there’s a good chance I won’t know which letter they meant.

So I’ll have to use ASCII. That’s how computers manage characters. Each character has a numerical code between 0 and 255. Values between 0 and 255 can be expressed as 2 hexadecimal digits. By giving me pairs of hex digits, they can send any character they like, including numbers, punctuation, etc.

...

So I’ll make cards for 0 through 9, and A through F. That makes 16 cards to place around the camera, plus the question card. Seventeen cards means over 21 degrees each. Much easier to deal with.