from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset


def clean_name(name):
    return "".join([c for c in name if c.isalpha()])

class ValidateTopicForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_topic_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Validate `topicget1` value."""

        # If the name is super short, it might be wrong.
        search_topic = tracker.get_slot("topicget1")
        name = clean_name(search_topic)
        if len(name) == 0:
            dispatcher.utter_message(text="Give a valid topic.")
            dispatcher.utter_message(text="To add topics, type - 'ok go' ")
            return [SlotSet("topicget1", None)]
        else:
            dispatcher.utter_message(text="ok, thanks.")
            dispatcher.utter_message(text=f"your search topic is- {search_topic}")
            dispatcher.utter_message(text=f"type-  'search' - search topics && 'change' - change/delete entered topics")
            return [SlotSet("topicget1", search_topic)]

        # return [SlotSet("topicget1", name)]
        