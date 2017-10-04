import sqlite3

class system(object):
    '''
    To get action
    '''
    def __init__(self):
        self.all_courses = 'course'
        self.all_surveys = 'survey'
        self.add_question = 'add'
        self.createSuvery = 'creatSurvey'
        self.logout =   'logout'

    def get_action(self,action):
        if action == self.all_courses:
            return self.all_courses
        elif action == self.all_surveys:
            return self.all_surveys
        elif action == self.add_question:
            return self.add_question
        elif action == self.createSurvey:
            return self.createSurvey

class questionList(object)
    
    def __init__(self):
        self.questions = []
    
    def add_multiple_choice(self,quesName,answer1,answer2,answer3)
        



