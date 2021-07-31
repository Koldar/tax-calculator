# Introduction
 
Allows a regime forfettario partita IVA to compute the taxes it needs to pay to the Italian Government.
 
# User 
 
## Installation
 
```
pip install tax-calculator
```
 
For a help, use:
 
```
tax-calculator --help
``` 

To compute taxes:

```
tax-calculator compute-forfettario --ateco="62.02.00" --ricavi=15000
```

For additional options, consult the help of the subparser:

```
tax-calculator compute-forfettario --help
```

## Features

 * Allows you to compute regime forfettario taxes;

# Developer

## Test

Just tox it:

```
tox
```

## Uploading

First create in your HOME folder the file `.pypirc`, with the following content:

```
[pypirc]
servers = pypi
[server-login]
username:<your pypi username>
password:<your pypi password>
```

Then perform your contribution. To test, update the version automatically, upload to pypi and create 
a new tag on the git repo do the following:

```
python setup.py test update_version_patch bdist_wheel upload push_tag
```

There are also `update_version_minor` and `update_version_major` which increase the minor and major version
number, respectively.   
 