# Numainda - The Legal and Parliamentary Facts Knowledge Bot

![Numainda Logo](logo.png)

## Project Overview

Numainda is a Knowledge bot designed to engage and educate on Pakistan's rich legal and parliamentary heritage. Drawing on the Constitution of Pakistan, the Elections Act 2017, and the latest parliamentary proceedings, Numainda shares fascinating legal and legislative facts in a fun, engaging manner. Our mission is to demystify Pakistan's legal documents and parliamentary proceedings, making them accessible and enjoyable.

## Features

- **Daily Tweets:** Numainda posts daily tweets that are concise, fact-filled, and engaging, using simple language and emojis to enhance readability. (Coming Soon)
- **Engagement with Questions:** The bot provides knowledgeable yet entertaining responses to questions about its knowledge base.
- **Bulletin Updates:** Shares insights into the latest debates, policies, and discussions directly from the heart of Pakistan's Parliament.
- **Chat UI:** A user-friendly chat interface that allows users to interact with the bot, ask questions, and receive informative responses.

## Prerequisites

- Python 3.9 or newer
- Twitter Developer Account and access to the Twitter v2 API 
- OpenAI API key for using GPT models

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourgithubusername/numainda.git
   cd numainda
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   Create a `.env` file in the project root and add your Twitter and OpenAI API keys:

   ```plaintext
   TWITTER_API_KEY=your_twitter_api_key
   TWITTER_API_SECRET=your_twitter_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

To run Numainda streamlit, execute:

```bash
streamlit run st_numainda.py
```

This script initiates the bot, allowing it to start tweeting and responding to queries.

## Contributing

We welcome contributions! If you have suggestions for new features, improvements, or bug fixes, feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your_feature_name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your_feature_name`)
5. Open a new Pull Request

## License

This project is licensed under the [MIT License](LICENSE).