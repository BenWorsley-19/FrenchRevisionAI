
import logging
import elevenlabs


class Communicator:
    """Wrapper around elevenlabs ai"""

    def read_out_loud(self, text_to_read: str) -> None:
        """Plays the text through your machine's speakers

        Args:
            text_to_read (str): the text to read out loud
        """
        logging.info("You will now hear a clip in french about recent sport headlines in France.")
        logging.debug("Making request to elevenlabs")
        audio = elevenlabs.generate(
            text=text_to_read,
            voice="Freya",
            model="eleven_multilingual_v1",
        )
        elevenlabs.play(audio)

    def communicate_lesson(self, summary: str, language_lesson: str) -> None:
        logging.info("The clip you just heard was: %s", summary)
        logging.info(
            "Your learnings from that script are: %s",
            language_lesson
        )