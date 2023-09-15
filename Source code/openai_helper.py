import openai
import keys

openai.api_type = keys.OpenAI_type
openai.api_base = keys.OpenAI_base
openai.api_version = keys.OpenAI_version
openai.api_key = keys.openAIKey

def complete_openai(prompt):
  
    try:
            response = openai.ChatCompletion.create(                
                messages=prompt,
                engine=keys.engine,
                temperature=0.7
            )
            return response
            
    except Exception as e:
        print("An exception of type", type(e), "occurred with the message:", e)
