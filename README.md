# Loading Progress Simulator ⏳

A simple animated loading progress bar built with Python and CustomTkinter.

## Features

- Animated progress bar from 0% to 100%.
- Live percentage counter.
- Start Loading button.
- Button is disabled while loading.
- Button becomes available when loading is completed.
- Dark mode interface.

## Requirements

- Python 3.10 or newer
- CustomTkinter

## Installation

Install the required library:

```bash
pip install customtkinter
```

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the application:

```bash
python main.py
```

## Technologies Used

- Python
- CustomTkinter

## How It Works

The application updates the progress bar using the `after()` method. The progress increases by 1% every 30 milliseconds until it reaches 100%.

## License

This project is free to use for learning and personal projects.
