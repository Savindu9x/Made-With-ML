import streamlit 
import langchain


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI()

llm = OpenAI(openai_api_key="YOUR_API_KEY", openai_organization="YOUR_ORGANIZATION_ID")

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

llm_chain.run(question)
