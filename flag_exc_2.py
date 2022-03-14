prompt = 'Please tell me sth interesting or'
prompt += '/n write "quit" to end the program:'
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
        print('Program is finished')
    else:
        print(message)
