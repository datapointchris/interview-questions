# MAIN OPTIONS


class QuitCommand():
    def execute(self, data=None):
        sys.exit()


class Jobs():
    def create_table(self, data=None):
        db.create_table('jobs', {
            'id': 'integer primary key autoincrement',
            'job': 'text not null',
        })

    def drop_table():
        pass

    def view():
        pass

    def view_reviewed():
        pass

    def view_not_reviewed():
        pass

    def view_all():
        pass
    
    def add():
        pass

    def edit():
        pass
    
    def delete():
        pass
    
    def delete_all():
        pass
    
    def reset():
        pass


class Questions():
    def create_table(self, data=None):
        db.create_table('questions', {
            'id': 'integer primary key autoincrement',
            'question': 'text not null',
        })

    def drop_table():
        pass

    def view():
        pass

    def view_answered():
        pass

    def view_not_answered():
        pass

    def view_all():
        pass
    
    def add():
        pass

    def edit():
        pass
    
    def delete():
        pass
    
    def delete_all():
        pass
    
    def reset():
        pass


# ANSWERS

class Answers():
    def create_table(self, data=None):
        db.create_table('answers', {
            'id': 'integer primary key autoincrement',
            'answer': 'text not null',
        })
    def drop_table():
        pass

    def view():
        pass

    def view_all():
        pass
    
    def add():
        pass

    def edit():
        pass
    
    def delete():
        pass
    
    def delete_all():
        pass
    
    def reset():
        pass



# TIPS

class Tips():
    def create_table(self, data=None):
        db.create_table('tips', {
            'id': 'integer primary key autoincrement',
            'tip': 'text not null',
        })
    def drop_table():
        pass

    def view():
        pass

    def view_reviewed():
        pass

    def view_not_reviewed():
        pass

    def view_all():
        pass
    
    def add():
        pass

    def edit():
        pass
    
    def delete():
        pass
    
    def delete_all():
        pass
    
    def reset():
        pass



# NOTES

class Notes():
    def create_table(self, data=None):
        db.create_table('notes', {
            'id': 'integer primary key autoincrement',
            'note': 'text not null',
        })

    def drop_table():
        pass

    def view():
        pass

    def view_reviewed():
        pass

    def view_not_reviewed():
        pass

    def view_all():
        pass
    
    def add():
        pass

    def edit():
        pass
    
    def delete():
        pass
    
    def delete_all():
        pass
    
    def reset():
        pass

