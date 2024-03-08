# geminiExplorer
## Overview
Gemini Explorer is a chat interface with Google's large language model Gemini integrated. The main purpose of this project is to educate and introduce the fusion of language models and user interfaces. The project uses Streamlit for the chat interface and VertexAI from Google Cloud to give us access to the Gemini API language model.

## Installation
### Prerequisites
To run Gemini Explorer, ensure that the following prerequisites are met:
 - Python 3.6 or higher
 - AI Platform
 - Streamlit
 - Google Cloud SDK

Include these prerequisites in your installation instructions to ensure that users have everything they need to run your project successfully.

### Step-by-Step Installation Guide
1. Clone the repository
    Start by cloning the repository to your local machine. Use the following command:
    ```bash
    git clone https://github.com/celsolopez14/geminiExplorer.git
    cd geminiExplorer

2. Set Up a Virtual Environment (Optional)
It's a good practice to create virtual environment when working with Python projects. This keeps your projects dependencies isolated. If you have virtualenv install create a new environment with:
    ```bash
    virtualenv env
    source venv/bin/activate

3. Install Dependencies
Inside the virtual environment, install all the dependencies necessary by running:
    ```bash
    pip install -r requirements.txt

4. Google Cloud Auth
To be able to use the google cloud services, you first need to auth with your google cloud credentials. You can do this by running either of the following commands:
    ```bash
    gcloud init
    gcloud auth application-default login
### Starting Gemini Explorer App
After the installation, you can start the Gemini Explorer App by simply running the python file. Navigate to the project directory and run:
    ```bash
    streamlit run gemini_explorer.py



