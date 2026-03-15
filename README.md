# FilmDetector MVP

Minimal local web app for image classification with Gradio and Hugging Face.

The application:
- accepts an image from the user
- sends it to a Hugging Face image model
- returns the top-3 predictions
- shows the result in a local web interface

## Stack

- Python 3.10+
- Gradio
- Transformers
- Torch
- Pillow

## Installation

Create and activate a virtual environment.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies.

```powershell
pip install -r requirements.txt
```

## Run

Start the local application.

```powershell
python app.py
```

By default, Gradio runs on `http://127.0.0.1:7860`.

## Docker

Build the image:

```powershell
docker build -t filmdetector .
```

Run the container:

```powershell
docker run --rm -p 7860:7860 filmdetector
```

After start, open `http://127.0.0.1:7860`.

## Project Structure

```text
FilmDetector/
|-- app.py
|-- README.md
|-- requirements.txt
|-- src/
|   |-- config.py
|   |-- model.py
|   |-- service.py
|   |-- ui.py
|   `-- utils.py
`-- check_list.md
```

## Modules

- `app.py` - application entry point
- `src/config.py` - project constants
- `src/model.py` - model loading and inference
- `src/service.py` - validation and formatting logic
- `src/ui.py` - Gradio interface
- `src/utils.py` - helper formatting functions
