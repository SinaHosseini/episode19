# Random Password Generator
Design by **Qt**

Coding by **Python**

## How work
- First, you choose the length of your password(8, 12 or 20), then press the generate button and receive your password

- Reset button to clear the text box 

- About button to show the function

## GUI
![GUI](https://github.com/SinaHosseini/episode19/blob/1ed2c13115f7bfc1641f036a07e12c27bf40a060/random_password_generator/rand_pass_shot.png?raw=true)

## Installation
```
pip install pyside6
```
## Usage
If you made some changes in the `mainwindow.ui` file, you need to run the following command:
```
pyside6-uic mainwindow.ui -o ui_mainwindow.py
```
You must run `pyside6-uic` again every time you make changes to the UI file.