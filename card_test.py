import strike

strikeObj = strike.Create("SHASHANK","http://www.fb.com").\
            Question("key1").\
            QuestionCard().\
            SetHeaderToQuestion(2,strike.HALF_WIDTH).\
            AddGraphicRowToQuestion(strike.PICTURE_ROW,["http://www.pop.com","http://valti.com"],["http://www.pop.com.tbn","http://valti.com.tbn"]).\
            AddGraphicRowToQuestion(strike.VIDEO_ROW,["http://www.pop.com","http://valti.com"],["http://www.pop.com.tbn","http://valti.com.tbn"]).\
            AddTextRowToQuestion(strike.H1,"some testing done here","blue",True).\
            Answer(True).\
            AnswerCardArray(strike.HORIZONTAL_ORIENTATION).\
            AnswerCard().\
            SetHeaderToAnswer(1,strike.HORIZONTAL_ORIENTATION).\
            AddGraphicRowToAnswer(strike.VIDEO_ROW,["http://www.pop.com","http://valti.com"],["http://www.pop.com.tbn","http://valti.com.tbn"])
    
print(strikeObj.ToJson())