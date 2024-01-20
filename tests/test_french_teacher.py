import unittest
from unittest.mock import Mock
from frenchrevisionai.french_teacher import FrenchTeacher


class FrenchTeacherTest(unittest.TestCase):

    _LESSON_SUMMARY = "bonjour"
    _LANGUAGE_LESSON = "that means hello fyi"

    def setUp(self):
        self._news_mock = Mock()
        self._assistant_mock = Mock()
        self._communicator_mock = Mock()
        self._subject_under_test = FrenchTeacher(
            self._news_mock, self._assistant_mock, self._communicator_mock
        )

    def test_french_lesson_plays_audio_and_communicates_lesson(self):
        self._given_we_get_news_headlines()
        self._given_assistant_provides_lesson()
        self._when_french_lesson_is_run()
        self._then_the_summary_is_read_out_loud()
        self._then_the_lesson_is_communicated()
   
    def _given_we_get_news_headlines(self):
        self._news_mock.get_todays_sport_headlines.return_value = "headline1\nheadline2"

    def _given_assistant_provides_lesson(self):
        self._assistant_mock.provide_lesson_from_headlines.return_value = {
            "summary": FrenchTeacherTest._LESSON_SUMMARY,
            "languageLesson": FrenchTeacherTest._LANGUAGE_LESSON,
        }

    def _when_french_lesson_is_run(self):
        self._subject_under_test.run()

    def _then_the_summary_is_read_out_loud(self):
        self._communicator_mock.read_out_loud.assert_called_once_with(FrenchTeacherTest._LESSON_SUMMARY)

    def _then_the_lesson_is_communicated(self):
        self._communicator_mock.communicate_lesson.assert_called_once_with(
            FrenchTeacherTest._LESSON_SUMMARY, FrenchTeacherTest._LANGUAGE_LESSON
        )