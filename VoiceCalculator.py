#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Error during calculation"

def main():
    print("Voice-Integrated Calculator")
    while True:
        try:
            spoken_input = listen()
            print("You said:", spoken_input)
            
            if "exit" in spoken_input:
                print("Calculator exited.")
                break
            
            result = calculate(spoken_input)
            print("Result:", result)
            
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error requesting results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




