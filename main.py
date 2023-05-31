import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key'

def generate_chat_completion(prompt):
    # Set the engine and parameters
    engine = "davinci"
    max_tokens = 50

    # Generate a chat completion
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens
    )

    # Get the response text
    completion = response.choices[0].text.strip()

    return completion

def main():
    prompt = "What is the meaning of life?"

    # Generate a chat completion
    completion = generate_chat_completion(prompt)

    # Print the response
    print("Response:", completion)

if __name__ == '__main__':
    main()

