 AirBnB_clone
The console based app for handling data storage of the Airbnb clone

## Project Overview
This project focuses on the backend of the AirBnB clone project, with the console interface and also utilizing the `cmd` module  in Pytho.

### Command Interpreter Description
The command line interpreter mimics the Bash Shell but is tailored for specific commands relevant to the AirBnB website. Serving as the frontend of the web app, users can interact with the backend developed using Python OOP programming.

### Available Commands

- `quit` or `EOF`: Exits the program.
- `help`: Provides information on how to use a command.
- `create`: Creates a new instance of a valid class and saves it to the JSON file.
- `show`: Prints the string representation of an instance based on the class name and ID.
- `destroy`: Deletes an instance based on the class name and ID.
- `all`: Prints all string representations of instances based on the class name.
- `update`: Updates an instance based on the class name and ID by adding or updating attributes.
- `count`: Retrieves the number of instances of a class.

The command line interpreter, coupled with the backend and file storage system, supports various actions, including creating new objects, retrieving objects, performing operations, updating attributes, and destroying objects.

## Getting Started

### Installation

Clone the repository from GitHub:

```bash
git clone https://github.com/Mmeso1/AirBnB_clone.git
### Project Files

The project includes the following essential files:

- `console.py`: The main executable of the project, serving as the command interpreter.
- `models/engine/file_storage.py`: Class for serializing instances to a JSON file and deserializing from JSON.
- `models/__init__.py`: Unique FileStorage instance for the application.
- `models/base_model.py`: Class defining common attributes/methods for other classes.
- Additional classes: `user.py`, `state.py`, `city.py`, `amenity.py`, `place.py`, `review.py`.

### Usage

The program can run in two modes: Interactive and Non-interactive.

### Interactive Mode

```bash
./console.py
```

In this mode, a prompt (hbnb) appears, allowing users to enter commands.

### Non-Interactive Mode

```bash
echo "help" | ./console.py
```

In this mode commands can be piped into the shell for non-interactive mode.

```(hbnb)
Documented commands (type help <topic>):
========================================

EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

### Format of Command Input

Commands must be piped through `echo` in non-interactive mode. In interactive mode, commands are entered directly when the prompt appears.

## Arguments

Most commands support various options or arguments. Ensure proper spacing when entering parameters.
