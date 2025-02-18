# Lesson 2 - Basic Commands & Getting Started with Aider

---

## 📚 Project Overview
Welcome to **Lesson 2** in the TandemFlow's AI development course. This lesson covers **basic commands and project setup** for working with **Aider**, a command-line AI assistant. You'll learn how to:
- Clone a repository and set up an environment.
- Manage context using Aider's command set.
- Utilize Aider to generate and modify code efficiently.
- Use Aider for version control with Git commands.
- Build a simple Python project that fetches Wikipedia articles.

---

## 📌 Lesson Breakdown

### **1️⃣ Cloning the Repository & Setting Up the Environment**
- Navigate to the **GitHub page** and copy the repository link.
- Open a terminal and run:
  ```sh
  git clone <repo_link>
  ```
- Open the cloned folder in your **IDE**.
- Locate the `template.env` file. Your previous `.env` settings **won't carry over**.
- Create a new `.env` file and add the necessary API keys.

---

### **2️⃣ Understanding Aider’s Context Management**
- **Aider is a tool, not a replacement**—it helps speed up development.
- Too much or too little **context affects performance**.
- **Core context commands:**
  - `/add <filename>` → Adds a file to Aider's context.
  - `/drop <filename>` → Removes a file from the chat session.
  - `/clear` → Clears conversation history.
  - `/reset` → Completely resets Aider.
  - `/readonly <filename>` → Adds a file as **read-only**.

---

### **3️⃣ Adding & Managing Files in Aider**
- Example: Adding `WikipediaFetcher.py` to the chat using:
  ```sh
  /add WikipediaFetcher.py
  ```
- Example: Dropping all files from chat:
  ```sh
  /drop all
  ```
- **Read-only mode** allows Aider to reference files without modifying them.

---

### **4️⃣ Building a Simple Wikipedia Fetcher**
- A Python script that fetches Wikipedia articles and saves them as Markdown.
- Running the program:
  ```sh
  /run python WikipediaFetcher.py "Python_(programming_language)"
  ```
- This saves the raw Wikipedia article text into a `.md` file.

---

### **5️⃣ Aider & Git Version Control**
- **Undo changes:**
  ```sh
  /undo
  ```
- **Using Git commands inside Aider:**
  ```sh
  /git add .
  /git commit -m "Added WikipediaFetcher.py"
  ```

---

### **6️⃣ Advanced Aider Commands**
- **Asking questions about the project:**
  ```sh
  /ask "What is the error message when an article isn't found?"
  ```
- **Getting help on Aider commands:**
  ```sh
  /help "How do I add a file to the chat?"
  ```
- Aider provides **explanations in plain English**, making it useful for beginners.

---

### **7️⃣ Next Steps & Lesson 3 Preview**
- Practice using `/add`, `/drop`, `/reset`, `/run`, and `/undo`.
- Lesson 3 will introduce:
  - **Data analysis with Wikipedia fetcher.**
  - **Handling multiple files.**
  - **Advanced AI prompting techniques.**

🛠 **Action Item:** Try replicating this project to reinforce these commands before proceeding to Lesson 3!

---

## 🚀 Conclusion
By completing this lesson, you now understand how to:
✅ Set up a project with Aider.
✅ Manage context efficiently.
✅ Utilize Aider for coding, file management, and Git version control.
✅ Build a simple project using AI-driven development.

**Practice and experiment with Aider’s commands to improve your proficiency!** 

See you in Lesson 3! 🎯
