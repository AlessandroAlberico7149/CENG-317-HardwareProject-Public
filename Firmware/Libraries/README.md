# What is contained here
**In the above folders a backup of the libraries has been uploaded**

# Qwiic motor driver

## Library
This library is required in order to make sure the qwiic motor to work with the rasp pi, currently only avaliable in Python. <br />
[Link to the Repo](https://github.com/sparkfun/Qwiic_SCMD_Py/blob/main/README.md#qwiic_scmd_py) <br />
This is a quick reference link to the which contains extended information and usage:
[Reference page](https://qwiic-scmd-py.readthedocs.io/en/latest/index.html)

## Installation
To install for all users use: `sudo pip3 install sparkfun-qwiic-scmd` <br />
Library is hosted online here: https://pypi.org/project/sparkfun-qwiic-scmd/ <br />

## Dependency
Since we are using python to install packages, pip and python are required: <br />
`sudo apt install python3 idle3` <br />
Note: might be pre-installed <br />
<br />
This library requires another library provided by sparkfun Qwiic I2C Py(see next paragraph): <br />
[Link to the Library repo](https://github.com/sparkfun/Qwiic_I2C_Py#installation) <br />
<br />

# Qwiic I2C Py

## Library
This library is required in order to have I2C connections with the qwiic motor. <br />
[Link to the Repo](https://github.com/sparkfun/Qwiic_SCMD_Py/blob/main/README.md#qwiic_scmd_py) <br />
This is a quick reference link to the which contains extended information and usage: 
[Reference page](https://qwiic-i2c-py.readthedocs.io/en/latest/index.html)

## Installation
To install for all users use: `sudo pip3 install sparkfun-qwiic-i2c` <br />
Library is hosted online here: https://pypi.org/project/sparkfun-qwiic-i2c/
<br />

## Dependency
In order for this library to function, smbus is required to be installed: <br />
Installation: pip install smbus <br />
[Link to library Repo](https://pypi.org/project/smbus/)
