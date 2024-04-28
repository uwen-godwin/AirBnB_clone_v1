# AirBnB Clone - The Console

The console is the first segment of the AirBnB project at Holberton School that collectively covers fundamental concepts of higher-level programming. The goal of the AirBnB project is to eventually deploy our server as a simple copy of the AirBnB Website (HBnB). A command interpreter is created in this segment to manage objects for the AirBnB (HBnB) website.

## Functionalities of this Command Interpreter:

- Create a new object (e.g., a new User or a new Place)
- Retrieve an object from a file, a database, etc.
- Perform operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

## Table of Contents

1. [Environment](#environment)
2. [Installation](#installation)
3. [File Descriptions](#file-descriptions)
4. [Usage](#usage)
5. [Examples of Use](#examples-of-use)
6. [Bugs](#bugs)
7. [Authors](#authors)
8. [License](#license)

## Environment

This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3).

## Installation

1. Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
2. Access the AirBnb directory: `cd AirBnB_clone`
3. Run the console interactively: `./console` and enter commands
4. Run the console non-interactively: `echo "<command>" | ./console.py`

## File Descriptions

### `console.py`

The console contains the entry point of the command interpreter. It supports various commands such as create, destroy, show, all, and update for managing objects.

### Models Directory

- `base_model.py`: The BaseModel class from which future classes will be derived. It contains initialization, string representation, save, and to_dict methods.
- Classes inherited from BaseModel:
  - `amenity.py`
  - `city.py`
  - `place.py`
  - `review.py`
  - `state.py`
  - `user.py`

### Models/Engine Directory

- `file_storage.py`: Serializes instances to a JSON file & deserializes back to instances. It contains methods like all, new, save, and reload.

### Tests Directory

Contains all unit test cases for this project:

- `test_models/test_base_model.py`
- `test_models/test_amenity.py`
- `test_models/test_city.py`
- `test_models/test_file_storage.py`
- `test_models/test_place.py`
- `test_models/test_review.py`
- `test_models/test_state.py`
- `test_models/test_user.py`

## Usage

```bash
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit

## Bugs

No known bugs at this time.
