from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

import pandas as pd
import datetime

# Test call transcript
call = "Hi, I was trying to book a slot yesterday but the payment failed, can you help me with this, thank you"

class EmotionAnalysis:
    def __init__(self):
        self.llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
    def analyze(self,call):
        try:
            prompt = ChatPromptTemplate.from_template("""
Analyze the following call transcript and classify its overall sentiment and tone. 
Provide a single-word main category (Positive, Negative, or Neutral) and a specific sub-category that best describes the tone. 
Additionally, write a concise summary of the key points discussed in the call.
**Main Categories:**
- Positive
- Negative
- Neutral
**Sub-Categories:**
- For Negative: Calm, Frustrated, Irritated, Angry, Disappointed, Confused
- For Positive: Calm, Happy, Satisfied, Grateful, Relieved
- For Neutral: Informational, Routine, Inquisitive
**Transcript:**
{call}
**Output Format:**
Main Category: [Your answer]
Sub-Category: [Your answer]
Summary: [Your concise summary of the call]
""")
    
            inp = prompt.format(call=call)
            output = self.llm.invoke(inp)
        
        # Print the output
            # print("LLM Response:")
            # print(output.content)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        if hasattr(output,'content'):
            return output
    def extract(self, output, buffer=None):
        n1 = output.content.split("\n")
        column = [i.split(":")[0].strip() for i in n1]
        row = [i.split(":")[1].strip() for i in n1]
        
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
        
        df = pd.DataFrame([row], columns=column)
        
        if buffer:
            df.to_csv(buffer, index=False)
        else:
            filename = f"call_analysis_{formatted_datetime}.csv"
            try:
                df.to_csv(filename, index=False)
            except Exception as e:
                print(f"Error saving to CSV: {e}")
if __name__=="__main__":
    ea=EmotionAnalysis()
    output=ea.analyze(call)
    ea.extract(output)

        
        

