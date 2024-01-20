import logging
import os
import requests


class NewsRetriever:
    """Retrieves news headlines."""

    def get_todays_sport_headlines(self) -> str:
        """Get 2 french sports headlines from today

        Returns:
            str: the headlines separated by a newline
        """
        url = 'https://newsapi.org/v2/top-headlines'
        params = dict(
            country='fr',
            category='sports',
            apiKey=os.getenv('NEWS_API_KEY'),
        )
        logging.debug("Making request to news api")
        resp = requests.get(url=url, params=params, timeout=240)
        data = resp.json()
        logging.debug(data)
        article_titles = self._get_first_two_titles(data)
        return "\n".join(article_titles)

    def _get_first_two_titles(self, data: dict) -> list[str]:
        article_titles = []
        for index, json_obj in enumerate(data["articles"]):
            if index == 2:
                break
            article_titles.append(json_obj["title"])
        return article_titles
