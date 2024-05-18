# WiFi Cracker

## Description
WiFi Cracker is a Python script that allows you to perform a dictionary attack on WiFi networks to recover the network's password. This script uses the PyWiFi library to connect to and test passwords on WiFi networks. It provides an easy way to perform a dictionary attack on a target WiFi network.

## Prerequisites
- Python 3.7 or higher
- PyWiFi library
- Termcolor library (for colorful console output)
- A dictionary file containing a list of potential passwords (dictionary.txt)

## Installation
1. Clone or download the repository to your local machine.
2. Make sure you have Python 3.7 or higher installed.

### Required Python Libraries
You can install the necessary Python libraries using pip. Run the following commands in your terminal or command prompt:

```shell
pip install pywifi
pip install termcolor
```

#Usage
Open your terminal or command prompt.

Navigate to the directory where the wifi.py script is located.

Run the script with the following command:
```shell
python wifi.py
```

The script will display a list of available WiFi networks. Select the network you want to perform a dictionary attack on by entering the corresponding number when prompted.

The script will start the dictionary attack. It will use the passwords listed in the dictionary.txt file to attempt to connect to the selected network.

If a correct password is found, the script will display it on the console and exit. If no password is found, it will continue running until you manually stop it.

#Customization
You can customize the dictionary file by replacing dictionary.txt with your own list of potential passwords.

You can modify the PyWiFi configuration in the create_temp_profile method of the Cracker class if you need to use a different authentication method, encryption type, or security settings.