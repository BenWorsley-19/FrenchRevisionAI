import json
import logging
import os
from openai import OpenAI


class FrenchTeachingAssistant:
    """Wrapper round open ai to provide french lessons"""

    def __init__(self) -> None:
        self._client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def provide_lesson_from_headlines(self, headlines: str) -> dict:
        """Get 2 french sports headlines from today

        Returns:
            str: a json object with the following fields: "summary" (provided in french), "languageLesson" (provided in english)
        """
        prompt = f"""
        Return a JSON object. The JSON must have these fields: "summary" (provided in french), "languageLesson" (provided in english).
        For field "summary" write a short paragraph (convert numbers to french text) in french based around the following 2 headlines: \n{headlines}
        For field "languageLesson" write a short paragraph in english which teaches me something about the french language from the
        french paragraph provided in summary.
        """
        logging.debug("Making request to openai with prompt: %s", prompt)
        response = self._client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a French language teacher. The teacher is helpful, and very friendly.",
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
            functions=[{"name": "generate_json_response", "parameters": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string", "description": "A summary of the news articles written in french"},
                    "languageLesson": {"type": "string", "description": "A french lesson written in english which is centered around the summary "}
                }
            }}]
        )
        response_text = response.choices[0].message.function_call.arguments
        logging.debug("The response given from openai was: %s", response_text)
        return json.loads(response_text)