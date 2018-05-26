# helpful-security-lock
The Helpful Security lock was made for college project in my 2nd Year of B.Tech.

# Operating System:
It is made for Raspberry pi (tested on Pi 3).

# Requirements:

1. Python2.7
2. opencv
3. zbar-py ( http://github.com/zplab/zbar-py )
4. face_recognition ( http://github.com/ageitgey/face_recognition )
5. speechpy ( http://github.com/astorfi/speechpy )
6. pydtw ( http://github.com/shunsukeaihara/pydtw )
7. pyfingerprint ( http://github.com/bastianraschke/pyfingerprint )
8. snowboy hotword detection ( http://github.com/Kitt-AI/snowboy )

# Details of Running the Codes:

To start at a specific module, change the `startMain.py` and run the `init()` function after including the desired header file.
The default pin is '1234', which can be changed while running using `#` or in the program at the beginning.
The default passkey to change a module is '62018', which was only used for demonstration purpose, as in reality, a user will only choose one module.

For the Voice+Finger Recognition module, it is assumed that the snowboy hotword detection is cloned into home directory.