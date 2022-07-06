from collections import namedtuple
from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.common_query_skill import CommonQuerySkill, CQSMatchLevel

Query = namedtuple("Query", ["query", "spoken_answer", "display_text", "image"])
# Set default values to None.
# Once Python3.7 is min version, we can switch to:
# Query = namedtuple('Query', fields, defaults=(None,) * len(fields))
Query.__new__.__defaults__ = (None,) * len(Query._fields)

class AnswerPhoneAssistant(CommonQuerySkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self._last_query = self._cqs_match = Query()

    @intent_file_handler('assistant.phone.answer.intent')
    def handle_assistant_phone_answer(self, message):
        self.speak_dialog('assistant.phone.answer')
        self.log.info(self._last_query)

    def CQS_match_query_phrase(self, utt):
        self.log.info("WolframAlpha query: " + utt)


def create_skill():
    return AnswerPhoneAssistant()

