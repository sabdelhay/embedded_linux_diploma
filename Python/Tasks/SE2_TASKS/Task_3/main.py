#!/usr/bin/python3

import task3

if __name__ == '__main__':
    task3.open_vscode()

    required_extensions = ["clangd", "C++ TestMate", "C++ Helper","CMake", "CMake Tools"]
    try:
        for extension in required_extensions:
            task3.install_extensions(extension)

        print("Extensions installation is done!")
    except:
        print("Something went wrong!")

   