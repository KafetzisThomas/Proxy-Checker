<h1 align="center">Proxy-Checker</h1>

__What Is This?__ - A command-line tool that checks text files for good and bad proxies.

__How to Download__: Open the terminal on your system and type the following command:

```bash
git clone https://github.com/KafetzisThomas/Proxy-Checker.git
```

## Setup

### Set up Virtual Environment

```bash
➜ cd path/to/script/directory
$ python3 -m venv env/
$ source env/bin/activate
```

### Install Dependencies

```bash
$ pip3 install -r requirements.txt
```

### Prepare Your Proxies File

```bash
$ touch proxies.txt
$ nano proxies.txt
```

Add your proxies, one per line:
```bash
➜ http://192.168.1.100:8080  # Example proxy
➜ ...
```

Save changes and close the file.

### Run Python Script
```bash
$ python3 main.py <filename>
```
