# Story Writing App using LangChain, Gemini Pro Text and Streamlit

## Overview
This repo contains the code for building a story writing app, using the Gemini Pro Text model and LangChain. Built using a Streamlit web service, the app can create custom stories based on user inputs.

## Getting Started

### Prerequisites
- Python 3.10 or later
- A Gemini API key

### Installation

1. **Clone the Repository**
   ```bash
   git clone git@github.com:tahreemrasul/story_writing_app.git
   cd ./story_writing_app
  
2. **Set Up a Conda Environment (Recommended)**
* If you don't have Conda, install it first.
* Create a new Conda environment:
   ```bash
   conda create -n story_writing_app python=3.8
* Activate the environment:
   ```bash
   conda activate story_writing_app

3. **Install Dependencies**
* Install the required packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

4. **Set Up Your OpenAI API Key**
* Create a .env file in the root directory of the project.
* Add your OpenAI API key to the `.env` file:
   ```bash
   GOOGLE_API_KEY='Your-GOOGLE-API-Key-Here'

### Usage
To run the application, simply execute the `app.py` script:
   ```bash
   streamlit run app.py
```

## Running in GCP Cloud Run
Cloud Run in GCP is a managed compute platform that lets you run containers directly on top of Google's 
scalable infrastructure. You can run on GCP using either the source code or through the Dockerfile. For running with 
source code, use:
```shell
gcloud builds submit --tag gcr.io/PROJECT_ID/image_name .
gcloud run deploy SERVICE --region us-central1 --allow-unauthenticated --image gcr.io/PROJECT_ID/image_name
```

