Computer Representation Playground

A Python command-line application that explores how computers represent text, images, and sound using numerical values and binary data.

a project to explore fundamental computer science concepts through practical experiments.

Features

1. Text Representation

* Explore Unicode code points.
* Convert characters into decimal, hexadecimal, and binary representations.
* Display UTF-8 encoded bytes.
* Identify ASCII values for ASCII characters.

2. Image Representation

* Open and inspect images.
* Display image dimensions and total pixel count.
* Examine individual pixels using RGB values.
* Display hexadecimal colour codes.
* Convert RGB colour channels into binary.

3. Sound Representation

* Generate a WAV audio file.
* Configure the sample rate, duration, and bit depth.
* Calculate the total number of audio samples.
* Display the size of the raw audio data.
* Generate a 440 Hz sine wave.

Technologies Used

* Python 3 — Core programming language.
* Pillow — Image processing.
* Python Standard Library — math, struct, wave, and pathlib.

Prerequisites

Before getting started, ensure you have:

* Python 3 installed.
* Git installed.
* Visual Studio Code or another code editor (optional).

Check your Python installation:

python3 --version

Check your Git installation:

git --version

Installation and Setup

Follow these steps to set up the project using Python best practices.

Step 1: Clone the repository

Clone this repository to your local machine

Navigate into the project directory:

cd computer-representation-playground

Step 2: Create a virtual environment

Create an isolated Python environment for the project:

python3 -m venv .venv

A virtual environment keeps project dependencies separate from other Python projects on your computer.

Step 3: Activate the virtual environment

On macOS and Linux:

source .venv/bin/activate

On Windows using Command Prompt:

.venv\Scripts\activate.bat

On Windows using PowerShell:

.venv\Scripts\Activate.ps1

Once activated, your terminal prompt will usually display (.venv).

Step 4: Upgrade pip

Upgrade Python’s package installer inside the virtual environment:

python -m pip install --upgrade pip

Step 5: Install dependencies

Install Pillow, which is required for the image representation feature:

python -m pip install pillow

The text and sound features use Python’s standard library and do not require additional packages.

Step 6: Run the application

Run the program from the project directory:

python main.py

The application will display an interactive menu in your terminal.

Choose a feature and follow the instructions.

How to Use

When you start the program, you will see the following menu:

==========================================
   COMPUTER REPRESENTATION PLAYGROUND
==========================================
1. Explore Text Representation
2. Explore Image Representation
3. Explore Sound Representation
4. Exit
Choose an option:

Explore Text Representation

Choose option 1 and enter a text string.

The program displays each character’s Unicode code point, decimal value, hexadecimal value, binary representation, and UTF-8 bytes.

Explore Image Representation

Choose option 2 and enter the path to an image.

The program displays the image dimensions and lets you inspect an individual pixel’s RGB values and binary representation.

Pillow must be installed for this feature.

Explore Sound Representation

Choose option 3 and provide the sample rate, duration, and bit depth.

The program generates a 440 Hz sine wave and saves it as sample_tone.wav in the current working directory.

Exit

Choose option 4 to exit the application.

Project Structure

computer-representation-playground/
├── .venv/          # Local virtual environment (not committed)
├── main.py         # Application source code
├── README.md       # Project documentation
└── .gitignore      # Files Git should ignore

The .venv/ directory is generated locally and should not be uploaded to GitHub.

The sample_tone.wav file is generated when you use the sound feature.

Development Best Practices

This project follows several Python development best practices:

* Virtual environments: Isolate project dependencies.
* Dependency management: Install packages inside the active virtual environment.
* Version control: Use Git to track changes and GitHub to host the source code.
* Git hygiene: Exclude virtual environments, Python cache files, and generated files using .gitignore.
* Modular code: Separate text, image, and sound functionality into individual functions.
* Input validation: Handle invalid menu choices, image coordinates, and sound settings.
* Documentation: Use a README to explain the project, setup, and usage.

Deactivate the Virtual Environment

When you finish working on the project, deactivate the virtual environment:

deactivate

When you return to the project later, activate the environment again before running the application.

Computer Science Concepts

This project explores three fundamental concepts:

* Text: Characters have Unicode code points and can be encoded into bytes using UTF-8.
* Images: Pixels can be represented using numerical RGB colour values.
* Sound: Digital audio can be represented as a sequence of samples with a defined sample rate and bit depth.

It also demonstrates Python functions, loops, conditional statements, input validation, numerical conversions, and file handling.

Learning Objectives

* Understand how computers represent different types of information.
* Explore binary, decimal, and hexadecimal number systems.
* Learn about Unicode, ASCII, and UTF-8.
* Understand RGB pixels and digital image representation.
* Explore digital audio sampling and bit depth.
* Practise building and running a Python command-line application.
* Learn basic Python project setup and dependency management.

Future Improvements

* Display binary values grouped into eight-bit bytes.
* Compare UTF-8 byte lengths for different strings.
* Explore image file sizes and pixel data.
* Visualize audio samples as a waveform.
* Add interactive experiments about binary representation.

Author

Created as a personal learning project while studying computer science through CS50.
