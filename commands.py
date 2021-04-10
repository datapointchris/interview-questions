# MAIN OPTIONS


class QuitCommand():
    def execute(self, data=None):
        sys.exit()


# CREATE TABLES


class CreateTableJobs():
    def execute(self, data=None):
        db.create_table('jobs', {
            'id': 'integer primary key autoincrement',
            'job': 'text not null',
        })


class CreateTableQuestions():
    def execute(self, data=None):
        db.create_table('questions', {
            'id': 'integer primary key autoincrement',
            'question': 'text not null',
        })


class CreateTableAnswers():
    def execute(self, data=None):
        db.create_table('answers', {
            'id': 'integer primary key autoincrement',
            'answer': 'text not null',
        })


class CreateTableTips():
    def execute(self, data=None):
        db.create_table('tips', {
            'id': 'integer primary key autoincrement',
            'tip': 'text not null',
        })


class CreateTableNotes():
    def execute(self, data=None):
        db.create_table('notes', {
            'id': 'integer primary key autoincrement',
            'note': 'text not null',
        })



# QUESTIONS

class AddQuestion():
    def execute(self, data):
        pass 


class DeleteQuestion():
    def execute(self, data):
        pass 


class DeleteAllQuestions():
    def execute(self, data):
        pass 


class ResetQuestions():
    def execute(self, data):
        pass 


class EditQuestion():
    def execute(self, data):
        pass 


class ViewAllQuestions():
    def execute(self, data):
        pass 


class ViewAnsweredQuestions():
    def execute(self, data):
        pass 


class ViewUnansweredQuestions():
    def execute(self, data):
        pass 

# ANSWERS

class ViewAnswer():
    def execute(self, data):
        pass 


class AddAnswer():
    def execute(self, data):
        pass 


class EditAnswer():
    def execute(self, data):
        pass 


class DeleteAnswer():
    def execute(self, data):
        pass 


class DeleteAllAnswers():
    def execute(self, data):
        pass 

# TIPS

class ViewTips():
    def execute(self, data):
        pass 


class AddTip():
    def execute(self, data):
        pass 


class EditTip():
    def execute(self, data):
        pass 


class DeleteTip():
    def execute(self, data):
        pass 


class DeleteAllTips():
    def execute(self, data):
        pass 


class ResetTips():
    def execute(self, data):
        pass 

# NOTES

class ViewNotes():
    def execute(self, data):
        pass 


class AddNote():
    def execute(self, data):
        pass 


class EditNote():
    def execute(self, data):
        pass 


class DeleteNote():
    def execute(self, data):
        pass 


class DeleteAllNotes():
    def execute(self, data):
        pass 


class ResetNotes():
    def execute(self, data):
        pass 
