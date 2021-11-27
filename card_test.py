import strike

strikeObj = strike.Create("SHASHANK","http://www.fb.com").\
            Question("key1").\
            QuestionCard().\
            SetHeaderToQuestion(2,"HALF").\
            AddGraphicRowToQuestion("pic_row",["http://www.pop.com","http://valti.com"],["http://www.pop.com.tbn","http://valti.com.tbn"]).\
            AddGraphicRowToQuestion("video_row",["http://www.pop.com","http://valti.com"],["http://www.pop.com.tbn","http://valti.com.tbn"]).\
            AddTextRowToQuestion("h1","some testing done here","blue",True).\
            Answer(True).\
            AnswerCardArray("HORIZONTAL").\
            AnswerCard().\
            SetHeaderToAnswer(1,"FULL").\
            AddGraphicRowToAnswer("pic_row",["http://www.pop.com","http://valti.com"],["http://www.pop.com.tbn","http://valti.com.tbn"])
    
print(strikeObj.ToJson())