def uInput(prompt):
    prompt = input()
    if prompt == "done":
        return prompt
    else:
        prompt = prompt + "\n"
    pcompletion = ""
    while prompt != "\n":
        pcompletion = pcompletion + prompt
        prompt = input() + "\n"
    return pcompletion

#prompt = ""
#prompt = uInput(prompt)
#print([*prompt])