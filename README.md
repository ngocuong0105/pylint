## Pylint notes

Pylint is a tool that checks for errors in Python code. Pylint makes sure your code runs and follows the [PEP8](https://www.python.org/dev/peps/pep-0008/#string-quotes) style guide. Pylint is a code linter, i.e. a program which inspects your code and gives you feedback.
"Generally, you shouldn't expect Pylint to be totally quiet about your code, so don't necessarily be alarmed if it gives you a hell lot of messages for your project!"

There are 5 kind of message types:
  * (C) convention, for programming standard violation
  * (R) refactor, for bad code smell
  * (W) warning, for python specific problems
  * (E) error, for probable bugs in the code
  * (F) fatal, if an error occurred which prevented pylint from doing further processing.

## Commands
- to understand pylint messages run:
```
pylint --help-msg=missing-module-docstring
```
- to create your own rules for constant expressions run with [regex](https://docs.python.org/3/library/re.html):
```
pylint --const-rgx='[a-z_][a-z0-9_]{2,30}$' tutorial.py
```
- create a configuration file, instead of writing regex on command line with:
```
pylint --generate-rcfile 
```
- Pylint allows parallel execution if computer cas more cores:
```
pylint -j 4 mymodule1.py mymodule2.py mymodule3.py mymodule4.py
```
- get pylint result report
```
pylint playground.py  --output-format=json:somefile.json,colorized
```

### Questions:
- get rcfile?