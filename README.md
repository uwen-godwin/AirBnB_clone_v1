# AirBnB Clone - The Console

The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher-level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

## Functionalities of this command interpreter:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

## Table of Content
1. [Environment](#environment)
2. [Installation](#installation)
3. [File Descriptions](#file-descriptions)
4. [Usage](#usage)
5. [Examples of use](#examples-of-use)
6. [Bugs](#bugs)
7. [Authors](#authors)
8. [License](#license)

## Environment

This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation

1. Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
2. Access AirBnb directory: `cd AirBnB_clone`
3. Run hbnb(interactively): `./console` and enter command
4. Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions

### console.py
The console contains the entry point of the command interpreter. List of commands this console current supports:
# AirBnB Clone - The Console

The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher-level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

## Functionalities of this command interpreter:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

## Table of Content
1. [Environment](#environment)
2. [Installation](#installation)
3. [File Descriptions](#file-descriptions)
4. [Usage](#usage)
5. [Examples of use](#examples-of-use)
6. [Bugs](#bugs)
7. [Authors](#authors)
8. [License](#license)

## Environment

This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation

1. Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
2. Access AirBnb directory: `cd AirBnB_clone`
3. Run hbnb(interactively): `./console` and enter command
4. Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions

### console.py
The console contains the entry point of the command interpreter. List of commands this console current supports:

- EOF - exits console
- quit - exits console
- <emptyline> - overwrites default emptyline method and does nothing
- create - Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id
- destroy - Deletes an instance based on the class name and id (save the change into the JSON file).
- show - Prints the string representation of an instance based on the class name and id.
- all - Prints all string representation of all instances based or not on the class name.
- update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

### models/engine directory
Contains File Storage class that handles JSON serialization and deserialization :


- EOF - exits console
- quit - exits console
- <emptyline> - overwrites default emptyline method and does nothing
- create - Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id
- destroy - Deletes an instance based on the class name and id (save the change into the JSON file).
- show - Prints the string representation of an instance based on the class name and id.
- all - Prints all string representation of all instances based or not on the class name.
- update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

### models/engine directory
Contains File Storage class that handles JSON serialization and deserialization :

- `file_storage.py`: serializes instances to a JSON file & deserializes back to instances
  - `all(self)`: returns the dictionary __objects
  - `new(self, obj)`: sets in __objects the obj with key .id
  - `save(self)`: serializes __objects to the JSON file (path: __file_path)
  - `reload(self)`: deserializes the JSON file to __objects

### tests directory
Contains all unit test cases for this project:

- `test_models/test_base_model.py` - Contains the TestBaseModel and TestBaseModelDocs classes TestBaseModelDocs class:
  - `setUpClass(cls)`: Set up for the doc tests
  - `test_pep8_conformance_base_model(self)`: Test that models/base_model.py conforms to PEP8
  - `test_pep8_conformance_test_base_model(self)`: Test that tests/test_models/test_base_model.py conforms to PEP8
  - `test_bm_module_docstring(self)`: Test for the base_model.py module docstring
  - `test_bm_class_docstring(self)`: Test for the BaseModel class docstring
  - `test_bm_func_docstrings(self)`: Test for the presence of docstrings in BaseModel methods

  - TestBaseModel class:
    - `test_is_base_model(self)`: Test that the instantiation of a BaseModel works
    - `test_created_at_instantiation(self)`: Test created_at is a pub. instance attribute of type datetime
    - `test_updated_at_instantiation(self)`: Test updated_at is a pub. instance attribute of type datetime
    - `test_diff_datetime_objs(self)`: Test that two BaseModel instances have different datetime objects

- `test_models/test_amenity.py` - Contains the TestAmenityDocs class:
  - `setUpClass(cls)`: Set up for the doc tests
  - `test_pep8_conformance_amenity(self)`: Test that models/amenity.py conforms to PEP8
  - `test_pep8_conformance_test_amenity(self)`: Test that tests/test_models/test_amenity.py conforms to PEP8
  - `test_amenity_module_docstring(self)`: Test for the amenity.py module docstring
  - `test_amenity_class_docstring(self)`: Test for the Amenity class docstring

- Similar tests exist for other models.

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
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050',

