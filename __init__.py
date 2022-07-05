from mycroft import MycroftSkill, intent_file_handler


class AnswerPhoneAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.phone.answer.intent')
    def handle_assistant_phone_answer(self, message):
        self.speak_dialog('assistant.phone.answer')


def create_skill():
    return AnswerPhoneAssistant()

