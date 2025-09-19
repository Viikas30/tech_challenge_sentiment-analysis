# 📞 Call Transcript Sentiment Analyzer

This application analyzes call transcripts using an LLM to:  
- Detect overall sentiment  
- Classify the tone (Positive, Negative, Neutral with sub-categories)  
- Generate a concise summary  

---

## 🚀 Steps to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

2.**Set up environment variables**
Create a .env file in the project root and add:
GROQ_API_KEY=your_api_key_here

3.**Run the application**
   ```bash
   uvicorn main:app --reload
