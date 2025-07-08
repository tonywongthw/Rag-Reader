📄 PDF RAG System
A simple Python application that uses LangChain to create a Retrieval-Augmented Generation (RAG) system for PDF documents. Ask questions about your PDFs and get AI-powered answers with source citations! 🤖
✨ Features

📁 Load and process PDF documents
💬 Interactive question-answering interface
📝 Source document citations
🔐 Secure API key management with .env files

📋 Prerequisites

🐍 Python 3.8 or higher
🔑 OpenAI API key

🚀 Setup Instructions
1. 📦 Install Dependencies
First, install the required Python packages:
bashpip install langchain openai faiss-cpu pypdf python-dotenv
2. 🔧 Set Up Environment Variables
Create a .env file in your project directory:
bashtouch .env
Add your OpenAI API key to the .env file:
OPENAI_API_KEY=your-actual-openai-api-key-here
⚠️ Important: Never commit your .env file to version control. Add it to your .gitignore:
bashecho ".env" >> .gitignore
3. 📄 Prepare Sample PDF
For testing, you can use any PDF file. Here's how to set up a sample gas bill PDF:
Option A: Use your own PDF 📁

Place any PDF file in your project directory
Rename it to gasbill.pdf (or use any name you prefer)

Option B: Create a sample PDF ✍️

Create a simple text document with sample gas bill information
Convert it to PDF using any PDF converter
Save it as gasbill.pdf

Sample content for testing: 💡
Monthly Gas Bill - January 2024

Account Number: 12345-678-90
Service Address: 123 Main Street, Anytown, USA

Usage Summary:
- Previous Reading: 1,250 CCF
- Current Reading: 1,375 CCF
- Usage: 125 CCF

Charges:
- Gas Supply: $85.50
- Delivery Charge: $23.75
- Environmental Fee: $2.50
- Total Amount Due: $111.75

Due Date: February 15, 2024
4. 🏃 Run the Application
Execute the Python script:
bashpython rag_system.py
5. ❓ Ask Questions
Once the system is ready, you can ask questions about your PDF:
Your question: What is my account number?
Your question: How much is my total bill?
Your question: What is my gas usage this month?
Your question: quit
🎯 Example Usage
bash$ python rag_system.py
Loading PDF...
Split into 3 chunks
Creating embeddings...
Vector database created
Setting up RAG chain...

================================================================================
RAG System Ready! Type your questions below.
Type 'quit' or 'exit' to stop.
================================================================================

Your question: What is my total amount due?
Answer: According to the gas bill, your total amount due is $111.75.

Sources:
Source 1: Page 1
Content preview: Monthly Gas Bill - January 2024

Account Number: 12345-678-90
Service Address: 123 Main Street, Anytown, USA

Usage Summary:
- Previous Reading: 1,250 CCF
- Current Reading: 1,375 CCF...
🔧 Troubleshooting
⚠️ Common Issues

🔑 API Key Error

Make sure your .env file contains the correct OpenAI API key
Verify the key is valid and has sufficient credits


📄 PDF Loading Error

Check that the PDF file path is correct
Ensure the PDF is not password-protected or corrupted


📦 Import Errors

Verify all dependencies are installed: pip list
Try reinstalling packages if needed



🆘 Getting Help
If you encounter issues:

✅ Check that all dependencies are installed correctly
✅ Verify your OpenAI API key is valid
✅ Ensure your PDF file is accessible and not corrupted
✅ Try with a different PDF file to isolate the issue

📂 File Structure
your-project/
│
├── rag_system.py          # Main application file
├── .env                   # Environment variables (not in git)
├── gasbill.pdf           # Sample PDF file
├── .gitignore            # Git ignore file
└── README.md             # This file
🛡️ Security Notes

🚫 Never commit your .env file to version control
🔒 Keep your OpenAI API key secure and don't share it
💰 Monitor your OpenAI usage to avoid unexpected charges

🎯 Next Steps
Once you have the basic system working, you can:

📖 Try different PDF documents
🧪 Experiment with different question types
⚙️ Modify the chunk size and overlap parameters
📝 Add more sophisticated prompt templates