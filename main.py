import openai
#variables is a personal file to hold sensitive personal information. Create your own
# OpenAi API key to use for this file.
import variables

# Set up your OpenAI API key
openai.api_key = variables.api_key

def generate_chat_completion(messages):
    # Set the engine and parameters
    model = "gpt-3.5-turbo"
    max_tokens = 50

    # Generate a chat completion
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0
    )

    messages.append({"role": response.choices[0]["message"]["role"], "content": response.choices[0]["message"]["content"]})
    print(response.usage)
    # Get the response text
    completion = response.choices[0]["message"]["content"]

    return completion

def main():
    prompt = "Can you generate a random sql statement?"
    messages = [
        {"role": "user", "content": prompt}
    ]

    # Generate a chat completion
    while(prompt != "done"):
        completion = generate_chat_completion(messages)
        #print the response here
        print("Response:", completion)
        prompt = input()
        messages.append({"role": "user", "content": prompt})

    # Print the response
    #print("Response:", completion)
    #print("Messages: ", messages)

if __name__ == '__main__':
    main()

