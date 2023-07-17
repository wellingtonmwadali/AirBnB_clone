## AirBnB clone

- The goal of the project is to deploy on your server a simple copy of the AirBnB website.

- This project is a web application composed by:


* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)



- This project application will not be built all at once, but step by step:


### (Step 1) The console:

* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)


- The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.


- This abstraction will also allow you to change the type of storage easily without updating all of your codebase.


- The console will be a tool to validate this storage engine

### How to start it
Run the console

```
$ ./console.py
```

### Testing
This project uses python library, `unittest` to run tests on all python files.
- Interactive tests
* `python3 -m unittest discover tests`

- Non-interactive test
* `echo "python3 -m unittest discover tests" | bash`


###examples
Some available commands are:

- show
- create
- update
- destroy
- count


### How to use it
In interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

In Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
