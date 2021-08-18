# Python best practices
## Practices, similar to other languages
- Readability:
    + Use meaningful variable names
    + Indentation of the code with blank lines
    + Limits on the line size (79 chars recommended by [PEP8](https://pep8.org))
    + Write modular code 
      (use relatively-short functions instead of monolith)
- Use the same code style inside the project
    + Python naming convention (also described in [PEP8](https://pep8.org))
    + [PEP8](https://pep8.org) - special code standard for Python language
    + [Zen of Python (PEP20)](https://www.python.org/dev/peps/pep-0020/#id2) - what should be valued in Python programming
    + Linter usage to ensure that the style is the same
- Documentation:
    + Use comments properly
    + Docstrings for Python
    + README.md
- Usage of the optimal algorithms and solutions
- Testing

## Unique practices

### Virtual environment
Python language is famous for the number of its libraries. 
However, some of them are compatible only with version of python or other libs.
To handle this situation properly the [python virtual environments](https://docs.python.org/3/tutorial/venv.html)
should be used for each project.

### requirement.txt file
This file is a log of the libraries' versions used in the project. 
It is used to make the process of project execution simpler for the first time 
(for instance, when Docker runs the app).