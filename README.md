## Installation
Install [Python3](https://www.python.org/) if you hasn't done it yet.

### Windows

Open _PowerShell_ and type

```shell
git clone https://github.com/GlebAkunenko/IamSoLazy.git
cd .\IamSoLazy\
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy the `confing.py` file to the project folder.

### macOS

It should work but I didn't try it!

```shell
git clone https://github.com/GlebAkunenko/IamSoLazy.git
cd IamSoLazy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy the `confing.py` file to the project folder.

## How it works

There is the tasks.txt file with the task list. There are 2 kinds of line:
1. the due line that starts with `!` symbol;
2. the task line that defines a task with the appropriate name and the above-mentioned date.

Before running script you need to activate the venv:
1. `.\venv\Scripts\Activate.ps1` on Windows (PowerShell);
2. `source venv/bin/activate` on macOS.

Then just run the `main.py`
```shell
python main.py
```
