from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import wikipedia
import os


def clean_name(name):
    return "".join([c for c in name if c.isalpha()])

def store_topics_in_file(search_topic):
    
    fo = open("list_of_topics.txt", "r+")
    line = fo.read()
    fo.close()
    print (line)
    search_topics_set= set(())

    ### check inside list_of_topics.txt file empty or not #######
    if line == '':
        search_topics_set.add(search_topic)
        print("___________________________________")
    else:
        for a in line.split(','):
            if a != '' :
                search_topics_set.add(a)
        search_topics_set.add(search_topic)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    ### delete old file and create new file and store ##########
    os.remove("list_of_topics.txt")
    
    with open(f"list_of_topics.txt","w") as file:
        print("<<<<<<<<>>>>>>>>>")
        for item in search_topics_set:
            file.write(item+",")
    print("first **************************************")
    return search_topics_set



#set_topic= set(())
class ValidateTopicForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_topic_form"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        ######## Validate `topicget1` value. ########
        search_topic = tracker.get_slot("topicget1")

        name = clean_name(search_topic)
        if len(name) == 0:
            dispatcher.utter_message(text="Give a valid topic.")
            dispatcher.utter_message(text="To add topic, type - 'ok go' ")
            return [SlotSet("topicget1", None)]
        else:
            # check in wiki ####
            
            try:
                info = wikipedia.summary(name, auto_suggest=False)

                ## save into a file ###
                with open(f"{search_topic}.txt","w") as file:
                    file.write(info)
                    
                print("going correct path")

                set_topics= store_topics_in_file(search_topic)

                dispatcher.utter_message(text="ok, thanks.")
                dispatcher.utter_message(text="your topics :")
                for item in set_topics:
                    dispatcher.utter_message(item+ ',')


                dispatcher.utter_message(text=f"type: \n 'search' - search topics \n 'delete' - delete entered topic \n 'ok go' - add more topics")
                
                return [SlotSet("topicget1", None)]

            except:
                print("false input value given")
                try:
                    ## wiki without with auto suggesion
                    info= wikipedia.summary(name)

                    with open(f"{search_topic}.txt","w") as file:
                        file.write(info)

                    set_topicss= store_topics_in_file(search_topic)
                    dispatcher.utter_message(text="ok, thanks.")
                    dispatcher.utter_message(text="your topics :")
                    for items in set_topicss:
                        dispatcher.utter_message(items+ ',' )

                    dispatcher.utter_message(text=f"type: \n 'search' - search topics \n 'delete' - delete entered topic \n 'ok go' - add more topics")

                    return [SlotSet("topicget1", None)]
                except:
                    dispatcher.utter_message(text="false input value is given")
                    dispatcher.utter_message(text="Add topic type- ok go")
                    return [SlotSet("topicget1", None)]
