with open('test.txt','r') as file:
    content=file.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in content:
            writer.write(line)

