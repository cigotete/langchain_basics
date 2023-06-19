from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from decouple import config

from third_parts.gutendex import scrape_gutendex

if __name__ == '__main__':
    print("Starting...")

    # Scrape books from gutendex
    gutendex_data = scrape_gutendex(page=1, limit=2)

    summary_template = """
        given the {books_information} about books, I want to create:
        1. what do you think about the book
        2. Kind of person who would like the book
        3. Kind of moment to read the book
        4. Some creative words to start a conversation talking about the book
    """

    summary_prompt_template = PromptTemplate(
        input_variables=['books_information'],template=summary_template
    )

    openai_api_key = config("OPENAI_API_KEY")
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(books_information=gutendex_data))