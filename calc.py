ans = 0
prompt = ""
while prompt.lower() != "q":
    prompt = input("enter num:")
   
    prompt = prompt.strip()
    if prompt[0] == "+":
            ans = ans + int(prompt[1:])
    elif prompt[0] == "-":
        ans = ans - int(prompt[1:])
    elif prompt[0] == "*":
        ans = ans * int(prompt[1:])
    elif prompt[0] == "/":
        ans = ans / int(prompt[1:])
    print(ans)



