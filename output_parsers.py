from typing import List

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class BookIntel(BaseModel):
    title: str = Field(description="Title of the book")
    suitable_topics: bool = Field(description="Boolean Suitability of the book")
    suitable_topics_details: str = Field(description="Why is suitability? details of why the book is suitable or not suitable for someone")
    

suitability_parser = PydanticOutputParser(
    pydantic_object=BookIntel
    )