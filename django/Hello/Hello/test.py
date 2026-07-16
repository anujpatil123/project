import google.generativeai as genai
# Make sure to configure your API key
genai.configure(api_key="AIzaSyA_x2uMnt-ObNovNlxpk9VbVj1YcR2ZCzw")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)