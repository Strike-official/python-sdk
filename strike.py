import json

class Create:

    def __init__(self,actionHandler,nextActionHandler):
        self.meta_response_object = {
            "status":200,
            "body":{
                "actionHandler" : actionHandler,
                "nextActionHandler" : nextActionHandler,
                "questionArray": []
            }
        }

    def Question(self,qContext):
        self.meta_response_object["body"]["questionArray"].append(
            {
                "question":{
                    "qContext":qContext
                }
            })  
        return self 

    def QuestionCard(self):  
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["question"].update(
            questionType="Card"
        )  
        return self

    def SetHeaderToQuestion(self,context_index,width):
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["question"].update(
            qCard=[
                {
                    "type":"header",
                    "descriptor":{
                        "context-object":context_index,
                        "card-type":width
                    }
                }
            ]
        ) 

        return self

    def AddGraphicRowToQuestion(self,graphic_type,url,thumbnail_url):
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["question"]["qCard"].append(
            {"type":graphic_type,
             "descriptor":{
                "value":url,
                "thumbnail":thumbnail_url
            }
            }
        )            
        return self

    def AddTextRowToQuestion(self,row_type,value,color,bold):
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["question"]["qCard"].append(
            {"type":row_type,
             "descriptor":{
                "value":[value],
                "color":color,
                "bold":bold
            }
            }
        ) 
        return self
    
    def Answer(self,multiple_select):
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1].update(
                answer={
                    "multipleSelect":multiple_select
                }
        )

        return self 

    def AnswerCardArray(self,card_orientation):
        multipleSelectVal = self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["answer"]["multipleSelect"]
        
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1].update(
            answer={
                    "multipleSelect":multipleSelectVal,
                    "card-orientation":card_orientation,
                    "responseType":"Card",
                    "qCard":[]
                }
        )

        return self   

    def AnswerCard(self):

        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["answer"]["qCard"].append(
            []
        )

        return self 

    def SetHeaderToAnswer(self,card_context,width):

        q_card_array = self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["answer"]["qCard"]
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["answer"]["qCard"][len(q_card_array)-1].append(
            {   
                "type":"header",
                "descriptor":{
                    "context-object":card_context,
                    "card-type":width
                }
            }
        )

        return self

    def AddGraphicRowToAnswer(self,graphic_type,url,thumbnail_url):

        q_card_array = self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["answer"]["qCard"]
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["answer"]["qCard"][len(q_card_array)-1].append(
            {   
                "type":graphic_type,
                "descriptor":{
                    "value":url,
                    "thumbnail":thumbnail_url
                }
            }
        )

        return self    

    def ToJson(self):
        json_data = json.dumps(vars(self)["meta_response_object"])
        return json_data 

     