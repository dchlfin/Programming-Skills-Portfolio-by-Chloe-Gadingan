# Exercise 3: Glossary 2

dict = {"Function":"   A piece of pre-written code that performs a specific operation\n",
        "String":"   Any written message enclosed in single or double quotation marks.\n",
        "Variable":"   A name that represents a value stored in the computer memory.\n",
        "Whitespace":"   Any string of text composed only of spaces, tabs, or line breaks.\n",
        "Compiler":"   A special program that translates a programming language\'s source code into machine code or another programming language.\n",
        "Mutable":"   The state in which an object can be modified after it is created.\n",
        "Immutable":"   The state in which an object cannot be changed after it has been created.\n",
        "Tuple":"   An ordered sequence of values.\n",
        "Dictionary":"   An object that stores a collection of data.\n",
        "Index Value":"   A method that finds the first occurence of the specified value.\n"
        }

for key, val in dict.items():
    print(f"{key}\n{val}")
