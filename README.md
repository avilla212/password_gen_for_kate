# Password Generator

This is a simple password generator program written in Python for my Lovely girlfriend,Kate. It generates random passwords based on user-defined criteria and allows the option to save the generated passwords to a file.

## Requirements

- Use on a computer running Windows or Mac OS
- Python 3.x
- Link to download Python: [Link to download Python](https://www.python.org/downloads/)
- Beneath the "Download Python" button, you will see text that says "Looking for Python with a different OS?". Click on the link below that text to download Python for Mac OS. Choose your OS version from the list and download the installer.

- pandas (install using `pip install pandas`)
- Create a file and/or folder on your **desktop** to save the passwords to

## Usage

1. Download the code from the GitHub repository by following these steps:

   - Open a web browser and go to the GitHub repository: [Link to the repository](https://github.com/avilla212/password_gen_for_kate)

   - Click on the "Code" button and select "Download ZIP" to download the code as a ZIP file.

   - Extract the downloaded ZIP file to a location of your choice on your computer.

2. Open the terminal/command prompt on your computer:

   - **Windows**:
     - Press `Win + R` to open the Run dialog box.
     - Type `cmd` and press Enter.

   - **Mac**:
     - Press `Command + Space` to open Spotlight Search.
     - Type `Terminal` and press Enter.

3. Once in the terminal, navigate to the directory where the extracted code files are located using the `cd` command. For example:

   ```bash
   cd /path/to/password-generator
    ```

4. Then run the following command to start the program:

   ```bash
   python rand_pass.py
   ```
5. Enter the number of the password you want to generate and press Enter.
6. Enter the desired length of the password and press Enter.
7. The program will generate random passwords based on the criteria you entered and display them on the screen
8. You will be asked if you want to save the passwords to a file. Enter 'y' for yes or 'n' for no
9. If you choose to save the passwords, the program will prompt you to enter the file name for the password file
10. The passwords will be saved to a file in the same directory as the program file

Note
The passwords generated by this program meet the following criteria:

At least one lowercase letter
At least one uppercase letter
At least one special character (!@#$%^&*()_+)
At least one digit (0-9)
The length of the password is user-defined (between 13 and 128 characters).
The saved passwords are formatted in a table using the pandas library.

The generated passwords are not stored anywhere and are only displayed and saved based on user preference