# chat-with-Data
A fun role-playing chatbot that utilizes the gpt-3.5-turbo model from OpenAI using Python and OpenAI's API. I do not own the character that is depicted in this chatbot!
Chat with Lieutenant Commander Data from Star Trek: Next Generation! Ask any questions about Star Trek in general or even just questions about the fantastical real world around us.

## How it works
This chatbot uses the new chat completion option for the OpenAI API. Since the endpoint accepts an array of messages that are labelled as either "User", "Assistant", and "System", I played with the "System" default message prompt and stored that as the initial message.

To aid the chat completion, I used a technique called few-shot prompting that utilizes examples of ways that I would like the model to respond. In this case, I wrote down a few of Data's quotes from episodes of the TV show and the movies, and then I matched each line with a new conversational question that I thought would fit with those responses in order to create question/answer pairs. With Data's real lines of dialogue as guidance, the model now has an example of Data's speaking patterns, and can answer your questions in that style.

After that initial "System" prompt message, The subsequent message history between the User and the Assistant are stored in memory in a list and recalled every time the user sends a new message. This list is not saved to the disk, so conversation history with this chatbot is limited to the session only.
## Next Generation Chatbots
In the future, I would like to implement a long-term and short-term memory system that utilizes a vector database for it's long-term memory, while storing the session conversation for short-term memory. When I show people this chatbot, the first thing they ask is usually Star Trek related, so in order to improve accuracy, I will "stuff" the prompt with relevant Star Trek information from the Star Trek fan wiki and embedded into a database like Weaviate for quick cosine similarity document retrieval.
