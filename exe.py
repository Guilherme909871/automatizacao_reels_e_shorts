import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["pyautogui", "time"],
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="automatizar insta",
    version="0.1",
    description="auomatizar inst",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="main.py", base=base)],
)