# AiAgent Integration with Chainlit UI 🤖

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Chainlit](https://img.shields.io/badge/Chainlit-Supported-brightgreen.svg)](https://chainlit.io/)  
[![OpenAI](https://img.shields.io/badge/OpenAI-Supported-blue.svg)](https://openai.com/)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-Supported-orange.svg)](https://gemini.google.com/)


A Modern AI Chat Assistant built with Chainlit, Google Gemini API, and the OpenAI Agent SDK.  Experience seamless asynchronous AI agent integration for dynamic and natural conversations✨


## Table of Contents

* [Description](#description)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)


## Description

Chainlit-AiAgent is a cutting-edge AI-powered chat assistant demonstrating the power of asynchronous AI agent integration using the OpenAI Agent SDK and the capabilities of Google's Gemini API. This project provides a practical example of building scalable and interactive AI chat applications.  It's a perfect resource for learning about Python async programming, AI model orchestration, and building robust AI systems.


## Features

* 🚀 **Asynchronous AI Agent Integration:** Leverage the OpenAI Agent SDK for efficient and responsive AI interactions.
* 🧠 **Google Gemini API Integration:** Utilize the power of Google Gemini for advanced generative AI capabilities.
* ⚡️ **Chainlit UI:** Enjoy a seamless and intuitive chat interface provided by Chainlit.
* 🛠️ **Extensible and Customizable:** Easily adapt and extend the AI assistant to suit your specific needs.
* 🔒 **Secure API Key Management:** Employ environment variables for secure storage of your API keys.
* 🔄 **Real-time Processing:** Experience dynamic user input processing for a responsive conversational flow.

## ✅ Prerequisites

| Tool / Requirement           | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Python 3.9+**             | Programming language used to build and run the project.                     |
| **Git**                     | Version control system to clone and manage the repository.                 |
| **Chainlit**                | Framework to build and serve the conversational UI.                        |
| **OpenAI Agent SDK**        | SDK to integrate and manage AI agents asynchronously.                      |
| **Google Gemini API Key**   | Required to access Gemini models. Get one from [here](https://aistudio.google.com/apikey). |
| **OpenAI API Key**          | Optional for integrating OpenAI models. Get one from [here](https://platform.openai.com/account/api-keys). |

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/waheed444/Chainlit-AiAgent.git
cd Chainlit-AiAgent
```

2. **Create and activate a Python virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install openai-agents chainlit
       # for UV User's
uv add openai-agents chainlit
```

4. **Configure API keys:** Create a `.env` file in the root directory and add your API keys:

 - > 📌 Make sure to store your API keys securely in a `.env` file in the root directory:


```bash
GEMINI_API_KEY = paste_your_gemini_api_key_here
               # OR
OPENAI_API_KEY = paste_your_openai_api_key_here
```


## Usage

1. **Start the Chainlit app:**

```bash
chainlit run agent.py  
    # for UV User's
uv run chainlit run agent.py -w
```

2. **Interact:** Open your web browser and interact with the AI assistant through the user-friendly Chainlit web UI.  The agent will process your messages asynchronously using the Gemini and OpenAI Agent SDKs.


## Contributing


We welcome contributions to improve this project! Please follow these steps:

1. **Fork** the repository.
2. **Create a new branch:** `git checkout -b feature-name`
3. **Make your changes** and ensure they adhere to the project's coding style and best practices.
4. **Commit your changes:** `git commit -m "Add feature"`
5. **Push to the branch:** `git push origin feature-name`
6. **Submit a pull request** with a clear description of your changes and their benefits.
If you find any issues or want to improve this project, feel free to open a [GitHub issue]([![License](https://img.shields.io/badge/License-MIT-blue.svg)https://github.com/waheed444/Chainlit-AiAgent/issues) or submit a pull request.

This repo is only for learning and exploring new things, feel free to fork it, explore, or give suggestions!

**Star ⭐ the repo if it helps you!**

---


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Let's Connect

<p align="left">
  <a href="https://www.linkedin.com/in/waheed444/?originalSubdomain=pk)" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin" alt="LinkedIn">
  </a>
  <a href="https://github.com/waheed444" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="waheedahmad5519@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Gmail">
  </a>
</p>

---
