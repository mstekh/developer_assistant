#try entering starting with "write python program that..."
import openai

openai.api_key = "your_api_key"
openai.Model.list()

# init chat 
chat_messages = [{
    "role": "system", 
    "content": "You are a helpful programmers assistant that write only row python syntax programs."}]

while True:
    #infinite loop, type "exit" to quite
    message = input("Enter your message: ")
    if message == "exit":
        break
    print("user:", message)
    chat_messages.append({"role": "user", "content": message})

    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_messages
    )

    assistant_answer = completions.choices[0].message.content
    print("assistant:", assistant_answer)
    print(type(assistant_answer))

    #write python program from your text request
    text = assistant_answer.split("\n")
    file = open("example.py", "w")

    #write only python sintax to file from answer 
    write = False
    for line in text:
        print(type(line))
        if line == "```python":
            write = True
            continue
        if line == "```":
            write = False
            break
        if write:
            file.write(line)
            file.write("\n")
    # Close the file
    file.close()

    #read program strting with '''python until '''
    with open("example.py", "r") as f:
            code = f.read()
            exec(code)

print("Chiao")