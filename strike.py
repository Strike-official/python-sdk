import json

class Strike:

    def __init__(self):
        self.meta_response_object = {}

    def Create(self,actionHandler,nextActionHandler):
        self.meta_response_object["status"] = 200
        self.meta_response_object["body"] = {
            "actionHandler" : actionHandler,
            "nextActionHandler" : nextActionHandler
        }
        return self

    def Question(self,qContext):
        self.meta_response_object["body"].update({
            "questionArray":[{
                "question":{
                    "qContext":qContext
                }
            }] 
        })  
        return self 

    def QuestionCard(self):  
        self.meta_response_object["body"]["questionArray"][len(self.meta_response_object["body"]["questionArray"])-1]["question"].update(
            questionType="qCard"
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

    def ToJson(self):
        json_data = json.dumps(vars(self)["meta_response_object"])
        return json_data 

if __name__=="__main__":
    
    strikeObj = Strike()  
    strikeObj.Create("golu","http://www.fb.com").Question("key1").QuestionCard().SetHeaderToQuestion(2,"HALF").\
    AddGraphicRowToQuestion("pic_row",["http://www.pop.com","http://valti.com"],["http://www.pop.com.tbn","http://valti.com.tbn"]).\
    AddGraphicRowToQuestion("video_row",["http://www.pop.com","http://valti.com"],["http://www.pop.com.tbn","http://valti.com.tbn"]).\
    AddTextRowToQuestion("h1","some testing done here","blue",True)
    
    print(strikeObj.ToJson())      