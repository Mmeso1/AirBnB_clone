# AirBnB Console

## Overview
This project provides a console-based application for managing data storage in the Airbnb clone. The primary focus is on the backend, featuring a command-line interface and utilizing Python's `cmd` module.

## Command Interpreter
The command interpreter acts as a frontend fot the Airbnb web app, allowing users to interact with the Python OOP backend. Key commands include:

- `quit` or `EOF`: Exit the program.
- `help`: Get information on command usage.
- `create`, `show`, `destroy`, `all`, `update`, `count`: Perform actions on instances.

## Getting Started
### Installation
Clone the repository:
```bash
git clone https://github.com/Mmeso1/AirBnB_clone.git
```

### Project Files
- `console.py`: Main executable for the command interpreter.
- `models/engine/file_storage.py`: Handles instance serialization to JSON and deserialization.
- `models/__init__.py`: Houses the unique FileStorage instance.
- `models/base_model.py`: Defines common attributes/methods for classes.
- Additional classes: `user.py`, `state.py`, `city.py`, `amenity.py`, `place.py`, `review.py`.

# Usage

### Interactive Mode
```bash
./console.py
```
Enter commands at the (hbnb) prompt.

### Non-Interactive Mode
```bash
echo "help" | ./console.py
```
Commands can be piped for non-interactive mode.
```bash
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
```

### Command Input
Commands can be entered directly in interactive mode or piped through `echo` in non-interactive mode. Ensure proper spacing for parameters.
