from chatgptapi import chatgptapi

def main():
    try:
        newPrompt = ""
        previous = []
        while True:
            newPrompt = input(">>> ")
            output = chatgptapi("user",f'{newPrompt}', previous) #it returns a tuple (answer, usage)

            reply = output[0] #the first element of the tuple returned by the function
            usage = output[1] #the second element of the tuple returned by the function

            print(reply)
            print(f"(Usage: {usage})")

            # Continuously append new prompt and reply chains to the list
            previous.extend([{"role": "user", "content": newPrompt}, {"role": "assistant", "content": f'{reply}'}])
            
    
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == '__main__':
    main()
