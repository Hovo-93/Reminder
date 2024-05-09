import os
import re
from datetime import datetime

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


class TextParser:
    @classmethod
    def analyze_text_and_extract_info(cls, text):
        """
          Извлекать информацию из текста
        :param text:
        """

        current_date = datetime.now().strftime("%Y-%m-%d")

        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                {
                    "role": "system",
                    "content": f"Please analyze the text and provide me with the date and time based on the current date. The current date is {current_date}.",
                },
                {"role": "user", "content": text},
                {
                    "role": "system",
                    "content": "You should display information extracted from the text you receive.You are a reminder system, and you should return information based on the current date.",
                },
                {
                    "role": "user",
                    "content": "Please return the response in the following Datetime format: YYYY-MM-DD HH:MM ",
                },
            ],
            max_tokens=500,
        )
        date_time_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}"
        extracted_info = response.choices[0].message.content
        match = re.search(date_time_pattern, extracted_info)
        if match:
            extracted_date = match.group()
            return extracted_date
        else:
            date_time_pattern = r"\d{4}-\d{2}-\d{2}"
            match = re.search(date_time_pattern, extracted_info)
            if match:
                extracted_date = match.group()
                return extracted_date


if __name__ == "__main__":
    parsed_text = str(input("Введите текст: "))
    result = TextParser().analyze_text_and_extract_info(parsed_text)
    print(result)
