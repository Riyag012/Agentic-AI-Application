# YouTube Video Summarizer Using Phidata & Google API

This project uses **Phidata**, **Google Gemini API**, and the **YouTube Transcript API** to summarize YouTube videos. The user provides a YouTube URL, and the
application fetches the video transcript, generates a summary, and presents it in a user-friendly format.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Tools & Libraries Used](#tools--libraries-used)
- [How It Works](#how-it-works)
- [API Key Configuration](#api-key-configuration)
- [Error Handling](#error-handling)

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add your **Google API Key** to the `.env` file:

     ```bash
     GOOGLE_API_KEY=your-google-api-key-here
     ```

---

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. In the web interface, paste the **YouTube video URL** into the input box.

3. Click the **"🔍 Summarize Video"** button. The application will:
   - Fetch the video’s transcript using the **YouTube Transcript API**.
   - Use **Phidata** and **Google Gemini 1.5 Flash** to summarize the transcript.
   - Display the summarized content to the user.

---

## Tools & Libraries Used

- **Phidata**: A multimodal agent framework that allows seamless integration with AI models. It is used to interact with **Google Gemini** for summarizing content.
- **Google Generative AI API (Gemini 1.5 Flash)**: A powerful AI model for generating and summarizing content. It processes the transcript generated from YouTube videos.
- **YouTube Transcript API**: Fetches the transcript (if available) from YouTube videos, which is then used for summarization.
- **Streamlit**: The web framework used for building the interactive front-end interface.
- **dotenv**: Loads environment variables securely, including the **API key** for Google’s API.

---

## How It Works

1. **User Input**: The user provides a **YouTube video URL** in the input box.
2. **Video ID Extraction**: The application extracts the unique video ID from the URL.
3. **Transcript Fetching**: The transcript is fetched for the video using the **YouTube Transcript API**.
4. **Summarization**: The transcript is passed to the **Google Gemini** model for summarization using **Phidata**.
5. **Display**: The summarized content is displayed on the webpage.

---

## API Key Configuration

To use the **Google Generative AI API**, you need to configure the **API Key**. Here are the steps:

1. Obtain your **Google API Key** by creating a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Google Generative AI API**.
3. Add your **API Key** to the `.env` file:

   ```bash
   GOOGLE_API_KEY=your-google-api-key-here
   ```

This allows your application to securely access the API and use the **Gemini model** for summarization.

---

## Error Handling

The application handles the following errors:

- **No Transcript Available**: If the video doesn’t have a transcript, an error message will be displayed.
- **Video Unavailable**: If the video is unavailable or deleted, an error message will appear.
- **General Errors**: Any other unexpected errors are caught and shown to the user in a user-friendly message.
  

