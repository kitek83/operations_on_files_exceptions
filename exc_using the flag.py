prompt = 'Tell me soth cool'
prompt += '\nor write "quit" to end the program:'
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
        print('Goodbye')
    else:
        print(message)