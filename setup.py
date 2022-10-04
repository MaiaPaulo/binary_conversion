from cx_Freeze import setup, Executable

base = None
executables = [Executable("YOUR_FILE_NAME.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "YOUR_PROGRAM_NAME",
    options = options,
    version = "VERSION_NUMBER e.g. 0.1",
    description = 'YOUR_PROGRAM_DESCRIPTION',
    executables = executables
)