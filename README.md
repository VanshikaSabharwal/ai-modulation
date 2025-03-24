# AI Content Moderation Toolkit

## Overview

The **AI Content Moderation Toolkit** is a web-based application built using Gradio and AI Agents that provides two key functionalities:

1. **Spam Detection** - Identifies whether a given text is spam or not.
2. **Fact Checking** - Verifies the truthfulness of a claim based on provided evidence.

This project is designed to help automate content moderation, ensuring reliability and accuracy in digital communication.

---

## Features

- **Spam Detection**:
  - Accepts user input text.
  - Classifies it as spam or not spam.
  - Provides a confidence score for classification.

- **Fact Checking**:
  - Accepts a claim and supporting evidence.
  - Determines whether the evidence supports or refutes the claim.
  - Returns a confidence score for classification.

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- Required dependencies listed in `requirements.txt`

### Clone the Repository

```bash
git clone https://github.com/VanshikaSabharwal/plugins.git
cd ai
```
### Install venv
1. For Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3-venv
```
2. For Mac
```bash
python3 -m ensurepip --default-pip

```

3. For Windows

venv is included with Python 3, so no extra installation is needed.

### Create a Virtual Environment
Navigate to your project directory and run:
```bash
python3 -m venv venv
```
This will create a venv folder in your project.

### Activate the Virtual Environment


1. For Linux/macOS
```bash
source venv/bin/activate
```

2. For Windows (Command Prompt)
```bash
venv\Scripts\activate
```

3. For Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

The application will launch and open in your web browser.

---

## Usage Guide

### Spam Detection

1. Navigate to the **Spam Detection** tab.
2. Enter the text to analyze.
3. Click **Analyze**.
4. View the result displaying:
   - **Label**: Spam / Not Spam
   - **Confidence Score**

### Fact Checking

1. Navigate to the **Fact Checking** tab.
2. Enter the **Claim** and **Supporting Evidence**.
3. Click **Verify**.
4. View the result displaying:
   - **Label**: Supports / Refutes
   - **Confidence Score**

---

## Examples

### Supports

| **Claim**                                             | **Evidence**                                       | **Expected Output** |
| ----------------------------------------------------- | -------------------------------------------------- | ------------------- |
| "The Eiffel Tower is in Paris."                       | "The Eiffel Tower is a landmark in Paris, France." | **Supports**        |
| "Albert Einstein developed the theory of relativity." | "Historical records confirm this."                 | **Supports**        |

### Refutes

| **Claim**                        | **Evidence**                                              | **Expected Output** |
| -------------------------------- | --------------------------------------------------------- | ------------------- |
| "The Eiffel Tower is in London." | "The Eiffel Tower is in Paris, not London."               | **Refutes**         |
| "Water freezes at 50°C."         | "Water freezes at 0°C under normal atmospheric pressure." | **Refutes**         |

---

## Technologies Used

- **Python**
- **Gradio**
- **Machine Learning Models** (for spam detection and fact-checking)
- **AI Agents**

---

## Contributing

Feel free to fork this repository and submit a pull request if you want to improve the project.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch (`feature-branch`)
3. Commit your changes.
4. Push the branch.
5. Open a pull request.

---



