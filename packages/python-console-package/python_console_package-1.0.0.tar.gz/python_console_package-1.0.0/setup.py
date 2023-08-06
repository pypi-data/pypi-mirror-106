from setuptools import find_packages, setup

with open("README.md","r") as readme_file:
    long_description = readme_file.read()

#Maybe not the best way to handle the version number, but it works fine
exec(open("python_console_package/__init__.py").read())

setup(
    name='python_console_package',
    version = __version__,
    include_package_data = True,
    python_requires = '>=3',
    description = 'A small template for building and distibuting python console applications',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "Markus Peitl",
    author_email = 'office@markuspeitl.com',
    url = 'https://github.com/MarkusPeitl/python-console-template',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=["argparse"],
    entry_points = {
        'console_scripts':['python_console_package = python_console_package.entrypoint:main']
    },
    packages = find_packages()
)