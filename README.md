# Workshop Registration Management using Python

## About the Project

This Python program manages workshop registration records using basic Python data structures such as lists, tuples, sets, and dictionaries.

The program processes participant registrations and performs operations such as removing duplicate registrations, finding unique participants and workshops, counting registrations, comparing Morning and Evening sessions, finding the workshop with the highest registrations, and displaying participants registered for the Python Workshop.

## Technologies Used

* Python 3
* Lists
* Tuples
* Sets
* Dictionaries
* For loops
* If-else statements

No external libraries are required.

## Program Features

* Removes duplicate workshop registrations
* Displays all unique registrations
* Finds all unique participants
* Finds all unique workshops
* Counts registrations for each workshop
* Counts Morning and Evening participants
* Finds the workshop with the highest number of registrations
* Displays participants registered for the Python Workshop

## Python Concepts Used

### Lists

Lists are used to store multiple workshop registration records.

### Tuples

Each registration is stored as a tuple containing the participant, workshop, and session.

### Sets

Sets are used to remove duplicate registrations and identify unique participants and workshops.

### Dictionaries

A dictionary is used to count the number of registrations for each workshop.

### Loops

`for` loops are used to process registration records and display results.

### Conditional Statements

`if-else` statements are used for checking sessions, counting registrations, and finding the workshop with the highest registrations.

## Sample Data

The program uses workshop registration records containing:

* Participant name
* Workshop name
* Session timing

Example:

```python
("Anish", "Python Workshop", "Morning")
```

Here, `Anish` is the participant, `Python Workshop` is the workshop, and `Morning` is the session.

## How to Run

Make sure Python 3 is installed.

Check Python installation:

```bash
python --version
```

Run the program:

```bash
python "Workshop registration management.py"
```

On Windows, you can also use:

```bash
py "Workshop registration management.py"
```

## Project Structure

```text
Workshop-Management/
│
├── Workshop registration management.py
└── README.md
```

## Expected Output

The program displays:

* Unique registrations
* Unique participants
* Unique workshops
* Registration count for each workshop
* Number of Morning participants
* Number of Evening participants
* Workshop with the highest registrations
* Participants registered for the Python Workshop

The order of some unique records may vary because sets do not maintain a fixed order.

## Learning Objectives

This program helps in understanding:

* Working with lists and tuples
* Removing duplicate data using sets
* Finding unique values
* Counting data using dictionaries
* Processing records using loops
* Using conditions for filtering and comparison
* Performing basic data analysis using Python

## Conclusion

The Workshop Registration Management program is a simple Python-based data processing program that demonstrates how basic Python data structures can be used to organize, analyze, and extract useful information from workshop registration records.

## Author

Srujana

