# SuperProcessor

> the perfect wrapper for subprocess.run

## Description 

This module is meant to ease use of `subprocess.run`,
minimizing and reducing all possible edge cases that
are prone to come with use of traditional `run()`.

## Goal

Write Shell commands in Python with ease!

## Dependencies

None! This module relies on zero external dependencies, 
making use of only the builtin module `subprocess`.

## Installation

Install either over Pypi with 

    pip3 install superprocessor
    
or over git-pip

    pip3 install git+https://github.com/samocorp/superprocessor.git
    

## Usage

This module is famous for the `cmd` function, which has a signature of 

    cmd(* args: str) -> Tuple(stdout: str, stderr: Union[str, None])

As you can see, this function implements a Golang-style error handling, of returing
both the std output and error of the command in the shell.

If no error is encountered, the second value of the returned tuple is of NoneType.

Importing and using the function is easy.

    from superprocessor import cmd
    
    cmd('mkdir -p ', NEW_DIR_P, \
    '&& cd', NEW_DIR_P, \
    '&& npm install')

## License

This project is governed by the MIT License.

Copyright SamoCorp 2021.

All Rights Reserved.
