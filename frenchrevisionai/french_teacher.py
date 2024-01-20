import logging
from frenchrevisionai.communicator import Communicator
from frenchrevisionai.french_teaching_assistant import FrenchTeachingAssistant
from frenchrevisionai.news_retriever import NewsRetriever


class FrenchTeacher:
    """Gives a french lesson from today's sport headlines in France"""

    def __init__(
        self,
        news: NewsRetriever,
        assistant: FrenchTeachingAssistant,
        communicator: Communicator
    ) -> None:
        self._news = news
        self._assistant = assistant
        self._communicator = communicator

    def run(self) -> None:
        logging.info("Get ready for some French revision!")
        article_titles = self._news.get_todays_sport_headlines()
        logging.info("Today's sport headlines in France: %s", article_titles)
        lesson = self._assistant.provide_lesson_from_headlines(article_titles)
        summary = lesson["summary"]
        language_lesson = lesson["languageLesson"]
        self._communicator.read_out_loud(summary)
        self._communicator.communicate_lesson(summary, language_lesson)