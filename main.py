import openai
#variables is a personal file to hold sensitive personal information. Create your own
# OpenAi API key to use for this file.
import variables
import tokenCounter
import userInput

# Set up your OpenAI API key
openai.api_key = variables.api_key
model = "gpt-3.5-turbo-0301"

def generate_chat_completion(messages):
    # Generate a chat completion
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0,
    )

    #Append the received message by the ai to our message thread
    messages.append({"role": response.choices[0]["message"]["role"],
                     "content": response.choices[0]["message"]["content"]})
    print("tokens used for this interaction: ", response.usage["total_tokens"], "\n")
    # Get the response text
    completion = response.choices[0]["message"]["content"]

    return completion

def main():
    system = "You are a SQL code generator. Your responses will only contain SQL code. Encapsulate all output in SQL comments."
    prompt = ""
    print("Input:")
    prompt = userInput.uInput("")
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]

    # Generate a chat completion
    while(prompt != "done"):
        tokens = tokenCounter.num_tokens_from_messages(messages, model)
        if tokens > 4095:
            print("Message string is too long, quitting program.")
            break
        else:
            print("This request will use", tokens, "tokens for your prompt.\n")
        completion = generate_chat_completion(messages)
        #print the response here
        print(completion, "\n\n\nInput:")
        prompt = userInput.uInput("")
        messages.append({"role": "user", "content": prompt})
    
    #print(messages)

if __name__ == '__main__':
    main()