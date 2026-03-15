# Software Installer

A simple **Windows CMD-based Software Installer** that allows users to easily search, install, uninstall, and update software using **winget** (Windows Package Manager).

**Build by AKBBProject**  
**Published by ComputerPoint**

---

# Features

✔ Search software by name  
✔ Install software quickly  
✔ Uninstall installed software  
✔ Update all installed software  
✔ Simple command-line interface  
✔ Automatic Python check using `run.bat`

---

# Requirements

Before running the project, your computer should have:

- Windows 10 or Windows 11
- Internet connection
- Python 3.x
- Winget (Windows Package Manager)

Most modern Windows systems already include **winget**.

The included **run.bat** file will automatically check if **Python** is installed and install it if missing.

---

# How to Download

### Method 1 (Recommended)

1. Go to the GitHub repository

https://github.com/AKBBProjects/Software-Installer

2. Click the **Code** button

3. Click **Download ZIP**

4. Extract the downloaded ZIP file

Example extracted folder:

Software-Installer-main

---

# Project Files

Software-Installer
│
├── software_installer.py
├── run.bat
└── README.md

---

# How to Run

### Step 1
Extract the project folder.

### Step 2
Double click:

run.bat

### Step 3

The script will:

1. Check if Python is installed
2. Install Python automatically if missing
3. Launch **Software Installer**

---

# Software Menu

============================================================
                     Software Installer
============================================================
                 Build by AKBBProject
              Published by ComputerPoint
============================================================

1. Search Software
2. Install Software
3. Uninstall Software
4. Update ALL Software
5. Exit

---

# Example Software You Can Install

Examples:

chrome  
vlc  
7zip  
telegram  
discord  
notepad++  
vscode  

Example usage:

Install → chrome

---

# Update All Software

Option **4** updates all installed apps using:

winget upgrade --all

This updates all applications installed via winget.

---

# Credits

Build by **AKBBProject**  
Published by **ComputerPoint**

---

# License

Free to use for personal and educational purposes.
