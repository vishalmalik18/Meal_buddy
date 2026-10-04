import ollama

system_intrection="""
You are an assistant who creates personalized food schedules.
Some users have allergies, so you must create the plan according to their dietary restrictions.
Users can also provide a list of ingredients they have, so you will build their schedule using those items based on the number of days they plan to follow the routine.
Present the entire food schedule as a clean, well-structured table so it is easy and peaceful for the user to read and follow.
Do not include any medical disclaimers, warnings, or legal fine print in your output.
"""

convo_history = [] #storing convo

def generate_response(human_input):
    try:
        """taking human_input & setting up system prompt"""

        convo_history.append({
            "role":"user",
            "content":human_input
        })

        message = [
            {
                "role":"system",
                "content":system_intrection
                }
            ]

        message.extend(convo_history) #adding previous convo with system instruction
        
        response = ollama.chat(
            model='gemma4',
            messages=message #supplying
            )

        convo_history.append({
            'role':"assistant",
            'content':response['message']['content']
        })
        
        # print(convo_history) #checking status

        if len(convo_history)>10:
            """if convo history goes beyond 5 remove first occurance"""
            convo_history.pop(0)
            convo_history.pop(0)
    except Exception:
        return "Sorry we have backend problem thank you"
    return response['message']['content'] #presenting output


def re_running_code(human_input): #used for if your not using stremlit
    """using while loop continuing the converstaion"""
    while True:
        if human_input == 'exit':
            print("Thank you")
            break
        response = generate_response(human_input)
        print(response)
    

