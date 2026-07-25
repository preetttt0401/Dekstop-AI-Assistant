from models.llm import llm
from brain.prompt import SYSTEM_PROMPT

from utils.logger import logger


class Conversation:
    """
    Handles AI conversations using Gemini.
    """

    def __init__(self):

        logger.info("Conversation module initialized.")

    def ask(self, question: str) -> str:

        logger.info(f"Question: {question}")

        prompt = f"""
{SYSTEM_PROMPT}

User: {question}

Assistant:
"""

        response = llm.invoke(prompt)

        answer = response.content.strip()

        logger.info("Response generated successfully.")

        return answer