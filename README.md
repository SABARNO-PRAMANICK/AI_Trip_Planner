# AI Travel Planner

Welcome to the **AI Travel Planner** project! This repository contains a Python-based application designed to assist users in planning personalized travel itineraries using AI-driven tools. The project leverages modern Python package management with `uv` for a streamlined development experience, along with libraries like `pandas` for data processing, `streamlit` for interactive web interfaces, and `FastAPI` (via `uvicorn`) for building a robust API. This README provides detailed instructions for setting up, configuring, and running the project on a Windows system.

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- **Python**: Version 3.10 or higher is recommended for compatibility with the project dependencies.
- **uv**: A fast and modern Python package and environment manager, used for dependency management and virtual environment creation.
- **Git**: For cloning the repository (optional, if you are downloading the code manually).
- A Windows operating system (the instructions below are tailored for Windows).

## Installation and Setup

Follow these steps to set up the AI Travel Planner project on your local machine.

### Step 1: Install `uv`

`uv` is a lightweight and efficient tool for managing Python packages and virtual environments. To install `uv`, run the following command in your terminal or command prompt:

```bash
pip install uv
```

To verify that `uv` is installed correctly, check its path:

```bash
python -c "import shutil; print(shutil.which('uv'))"
```

If the output shows a valid path (e.g., `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python310\Scripts\uv.exe`), `uv` is installed successfully.

### Step 2: Initialize the Project

Create a new project directory named `AI_Travel_Planner` using `uv`. This command sets up a basic project structure with a `pyproject.toml` file for dependency management.

```bash
uv init AI_Travel_Planner
```

Navigate to the project directory:

```bash
cd AI_Travel_Planner
```

### Step 3: Verify Python Environments

Check the available Python versions on your system to ensure compatibility:

```bash
uv python list
```

If the desired Python version (e.g., CPython 3.10.18) is not available, install it using `uv`:

```bash
uv python install cpython-3.10.18-windows-x86_64-none
```

Verify the installation by listing Python versions again:

```bash
uv python list
```

### Step 4: Create a Virtual Environment

Create a virtual environment named `env` using the specified Python version. This isolates project dependencies from your global Python environment.

```bash
uv venv env --python cpython-3.10.18-windows-x86_64-none
```

If you have Anaconda installed, ensure you deactivate any active Conda environment before creating the virtual environment to avoid conflicts:

```bash
conda deactivate
```

### Step 5: Activate the Virtual Environment

Activate the virtual environment to use its isolated Python environment. On Windows, run the activation script:

```bash
C:\Users\<YourUsername>\AI_Travel_Planner\env\Scripts\activate.bat
```

After activation, your terminal prompt should change to indicate that the virtual environment is active (e.g., `(env) C:\Users\<YourUsername>\AI_Travel_Planner>`).

### Step 6: Install Project Dependencies

Add the required dependencies to the project. For example, to install `pandas` for data manipulation:

```bash
uv add pandas
```

To view the installed packages in the virtual environment:

```bash
uv pip list
```

Additional dependencies (e.g., `streamlit` and `fastapi`) will be installed automatically based on the `pyproject.toml` configuration or can be added manually using `uv add <package>`.

## Running the Application

The AI Travel Planner includes two main components: a **Streamlit web interface** for user interaction and a **FastAPI backend** for handling API requests.

### Running the Streamlit Web Interface

To launch the Streamlit application, ensure the virtual environment is activated and run:

```bash
streamlit run streamlit_app.py
```

This starts a local web server, and you can access the application by opening the provided URL (typically `http://localhost:8501`) in your browser. The Streamlit app provides an interactive interface for generating travel itineraries, viewing recommendations, and more.

### Running the FastAPI Backend

To start the FastAPI backend, ensure the virtual environment is activated and run:

```bash
uvicorn main:app --reload --port 8000
```

- `main:app`: Refers to the FastAPI application instance defined in `main.py`.
- `--reload`: Enables auto-reload for development, so the server restarts when code changes are detected.
- `--port 8000`: Specifies the port to run the server on (default is 8000).

You can access the API at `http://localhost:8000`. The API documentation is available at `http://localhost:8000/docs` (powered by Swagger UI).

## Project Structure

Here’s an overview of the key files and directories in the project:

- `pyproject.toml`: Defines project metadata and dependencies, managed by `uv`.
- `streamlit_app.py`: The main script for the Streamlit web interface.
- `main.py`: The main script for the FastAPI backend.
- `env/`: The virtual environment directory containing isolated Python and package installations.
- `README.md`: This file, providing setup and usage instructions.

## Troubleshooting

- **Conda Conflicts**: If you encounter issues with Conda environments, always run `conda deactivate` before creating or activating the `uv` virtual environment.
- **Python Version Issues**: Ensure the correct Python version is installed and used by `uv`. Use `uv python list` to verify available versions.
- **Port Conflicts**: If port 8000 (FastAPI) or 8501 (Streamlit) is in use, change the port by modifying the `--port` flag (e.g., `--port 8001`).
- **Dependency Errors**: Run `uv pip list` to verify installed packages. If a package is missing, install it with `uv add <package>`.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.
