# python enimga

This project was designed for one task only, and that task is to create an encrypted message

Here is the end goal:
1) You have an ID, and whoever you are sending the message to knows your ID. Your ID can be anything, it could be your name, or even hvduijsbfmuido3284109.. This means that the reciprocant can choose to only read messages send from your ID, or they can choose not to reply to them.
   
2) And every time you send a message, no matter what you do, the enigma will always send a different encrypted message. This is because it generates a new plug combination every time you want to send a message.
   
3) When sending a message, the script will generate a "token" which you can then use to decode the message. Because the plugs are generated at random, we need a way to get back those plug combos. This is where a seed comes into place, a seed where you can trace back when it was made. 

4) Once you have that seed, lets say plugs 'CX LE HZ SG MT QF OL EK HJ MC' equal '9124879709799869538'. I can use said generated seed, to trace back what the plugs were. But for the sake of everything secret, I would have to make a weird algorithm to keep it seemingly random.

5) ??? I have not gotten this far yet.
