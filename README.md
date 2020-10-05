# DevOps20 Python

## Setup

1. Create a virtual environment
2. Install requirements

### Virtual environment (venv)

see <https://docs.python.org/3/library/venv.html>

Linux / OSX

```sh
python -m venv .venv  # could also be python3
source .venv/bin/activate
```

Windows - cmd.exe

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

Windows - PowerShell

```PowerShell
# On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following PowerShell command:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

py -m venv .venv
.\.venv\Scripts\Activate.ps1

```

### Install requirements.txt

```bat
pip install -r requirements.txt
```

[disable cSpell]: (/*cSpell:disable*/)

## Kursmål

### Efter avslutad kurs ska den studerande

- kunna arbeta med socketsprogrammering i Python
- kunna skapa klientapplikationer som kommunicerar med en server via sockets
- kunna skapa enhetstester och applicera testdriven utveckling
- första hur versionshantering fungerar i utvecklingsprocessen och kunna använda något verktyg för versionshantering

### Kursens innehåll

- Socketsprogrammering.
- Grafiska gränssnitt i Python.
- Testdriven utveckling
- Versionshantering
- Enhetstestning och test cases
- Kunskaper om hur man deploya kod på en driftserver
