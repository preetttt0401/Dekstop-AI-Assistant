"""
Application Registry

Stores all supported desktop applications and their aliases.
"""


APPS = {
    "calculator": {
        "aliases": [
            "calculator",
            "calc",
            "math",
            "maths"
        ],
        "command": "calc.exe"
    },

    "notepad": {
        "aliases": [
            "notepad",
            "notes"
        ],
        "command": "notepad.exe"
    },

    "paint": {
        "aliases": [
            "paint",
            "drawing",
            "drawing app"
        ],
        "command": "mspaint.exe"
    },

    "command prompt": {
        "aliases": [
            "cmd",
            "command prompt",
            "terminal"
        ],
        "command": "cmd.exe"
    },

    "powershell": {
        "aliases": [
            "powershell"
        ],
        "command": "powershell.exe"
    },

    "wordpad": {
        "aliases": [
            "wordpad"
        ],
        "command": "write.exe"
    }
}