client<llm> GPT35Client {
    provider baml-openai-completion
    options {
         model gpt-3.5-turbo-instruct
        temperature 0
        api_key env.OPENAI_API_KEY
        max_tokens 200
    }
}
 
client<llm> GPT4Client {
    provider baml-openai-chat
    options {
        model gpt-4
        temperature 0
        api_key env.OPENAI_API_KEY
    }
} 