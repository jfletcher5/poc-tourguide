from langchain import OpenAI, LLMChain, PromptTemplate

# Initialize OpenAI LLM
llm = OpenAI(model_name="gpt-4o", streaming=False, max_tokens=1000)

# Define a prompt template
prompt_template = PromptTemplate(template="What is the capital of {country}?")

# Create an LLMChain with the LLM and the prompt template
chain = LLMChain(llm=llm, prompt_template=prompt_template)

# Run the chain with the input variables
result = chain.run({"country": "France"})
print(result)
