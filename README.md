# talentscout-chatbot

🧠 Project Overview

**TalentScout Hiring Assistant** is a conversational AI tool designed to assist recruiters and hiring teams by automatically generating tailored technical interview questions based on a candidate’s profile. The assistant collects details like position, experience, and tech stack, and generates skill-specific questions using a large language model (LLM) hosted on OpenRouter. It also supports follow-up queries, context handling, and graceful exits.

🛠️ Installation Instructions-

1. Clone the Repository:

   git clone https://github.com/Nilesh5168/talentscout-chatbot.git

   cd talentscout-chatbot

2. Create a Virtual Environment (Recommended):

   python -m venv venv

   venv\Scripts\activate


3. Install Dependencies

   pip install -r requirements.txt

4. Run the Streamlit App

   streamlit run app.py

5. Configure OpenRouter API Key

   Open prompts.py and replace the API key placeholder:

   OPENROUTER_API_KEY = "sk-..."  # Replace with your OpenRouter key


🧑‍💻 Usage Guide

   Open the app in your browser (it will launch automatically after running).

   Enter candidate information:

   Full Name

   Email

   Phone

   Years of Experience

   Desired Position

   Tech Stack (comma-separated)

Click Start Chat to receive technical questions.

Use the chat interface to ask follow-ups.

Type exit, bye, or stop to end the chat.




🧠 Technical Details

Architecture

  Frontend: Streamlit UI for candidate data input and interactive chat

  Backend: Python script using HTTP API calls

  Model: google/gemma-3-4b-it:free via OpenRouter.ai


Libraries Used

  streamlit: Provides the chat interface and input forms.

  httpx: Makes secure HTTP requests to the OpenRouter API.




✍️ Prompt Design

Prompts are crafted to adapt dynamically to the candidate's input:

  Initial Prompting:
  The system generates targeted technical questions by analyzing the user's listed technologies and grouping 3–5 skill-based questions per technology.

  Follow-up Chat Prompts:
  Inputs from the user are passed directly to the LLM in an ongoing conversational format. Context is preserved, allowing follow-up questions to remain relevant. Exit detection is handled via command keywords.


🧩 Challenges & Solutions

During development, several key challenges were encountered:

Model Access: OpenAI and Hugging Face models were limited or required payment, so we switched to using OpenRouter, which provides free access to several high-quality LLMs like Gemma.

Skill-Specific Question Generation: Initially, the prompt returned generic or repetitive questions. To fix this, the prompt was refined to clearly request 3–5 grouped questions for each individual technology in the tech stack.

Empty or Error-Prone Responses: Occasionally, the LLM would return no JSON or an HTTP error. This was handled by checking status codes and catching exceptions with meaningful fallback messages.

Conversation Flow and Context: Managing the state of the conversation in Streamlit required using st.session_state to track both candidate inputs and back-and-forth chat messages.

Fallback & Exit Handling: Users may input unexpected prompts or want to exit at any time. We implemented keyword matching to gracefully end the conversation and offer a proper closing message.


📄 License
This project is licensed under the MIT License.
