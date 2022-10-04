import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("binary_calculator.py",
                                    base=base,
                                    icon="binary.ico",
                                    targetName="Binary_calculator")]

cx_Freeze.setup(
    name="Binary_calculator",
    options={"build_exe": {"packages": ["tkinter"],
                           "include_files": ["binary.ico",
                                             "click_me.png",
                                             "math.ico"]}},
    version="1.0",
    description="A simple way to convert decimal into binary",
    executables=executables
)