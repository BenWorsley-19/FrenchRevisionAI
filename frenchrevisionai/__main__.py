import logging
from frenchrevisionai.communicator import Communicator
from frenchrevisionai.french_teacher import FrenchTeacher
from frenchrevisionai.french_teaching_assistant import FrenchTeachingAssistant
from frenchrevisionai.news_retriever import NewsRetriever


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    news = NewsRetriever()
    assistant = FrenchTeachingAssistant()
    communicator = Communicator()
    french_lesson = FrenchTeacher(news, assistant, communicator)
    french_lesson.run()
