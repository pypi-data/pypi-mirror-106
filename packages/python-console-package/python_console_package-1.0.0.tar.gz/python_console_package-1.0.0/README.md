# Python console package

This is a small template for building, distributing and packaging a python console application.

**TODOS:**

- Do this
- Do that

## Installation

Can be easily installed from pypi with pip3.

```bash
pip3 install python_console_package
```

## Running from source

You can also alway clone the repo from [GitHub](https://github.com/MarkusPeitl/python_console_package) and run with python.

```bash
python3 launcher.py "this/is/my/source/path"
```

or by

```bash
python3 entrypoint.py "this/is/my/source/path"
```

If installed through pypi then executing the script name `python_console_package` essentially runs something like `python3 python_console_package/entrypoint.py` (this is specified through `entry_points` in **setup.py**),which is used in the further usage examples.

## FILES and their functions

### build.py

```bash
python3 build.py
```

to build and package the application using setuptools to the **dist** directory.  

### entrypoint.py

```bash
python3 entrypoint.py
```

this is a launcher for the main script, can be used interchangably with python_console_package/entrypoint.py.  

### install-dev.py

```bash
python3 install-dev.py
```

use the pip3 installer to install this project directory to the system. (Immediatly reflects the changes done to the scripts).  

### install.py

```bash
python3 install.py
```

Build the application and install the resulting package -> the installation is the same as if you would install the package from pypi.  

### LICENCE.txt

The License of your project, do your research and choose your License with care.  
(Here it is APACHE 2.0)  

### MANIFEST.in

Specifies additional non-python files that should be included into the distributed package.  

### publish.py

```bash
python3 publish.py
```

Build the application and upload to pypi using twine (make sure everything is working before as you can not replace a version once it is online).  
After you have published the package, tag your package version and push to your git repository.

1. Commit your changes `git commit -am "your message"`
2. Push your changes `git push`
3. Create a version tag in your repository `git tag 1.0.0`
4. Push the tag to your repository `git push --tags`

### README.md

Main description and documentation of your project.  

### RELEASE.md

A markdown file containing info about the release versions and their changes.  

### setup.py

The setuptools configuration, which contains all packaging information and some installation information for your project.
Make sure to replace the info before packaging your application.
Contains:

- Meta information like: author, version, classifiers, url, description
- Importent information about the structure and files of your package for installation: modules, entrypoints, name, dependencies

## Using the application

```bash
python_console_package --setup
```

If you want to provide a setup function to your users you can implement a function call when this options is specified.

```bash
python_console_package --version
```

Print out the version information of your package

```bash
python_console_package "test/path/source"
```

Call application with a positional text argument.

```bash
python_console_package "test/path/source" --option "my optional argument text"
```

Call application with a optional text argument.

```bash
python_console_package "test/path/source" --multiply 1 2 3 8 96
```

Call application with an optional argument list.

```bash
python_console_package "test/path/source" --printm
```

Call the application with an optional boolean option.

### If you like the project consider dropping me a coffee

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?hosted_button_id=BSFX8LCPHW2AE)
  
<br>  
<br>