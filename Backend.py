#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################

import os
import sqlite3

############static variables#####################




class User_data:
    def __init__(self):
        super(User_data, self).__init__()
        self.__user_data = {}

    def init(self, user_id):
        if user_id not in self.__user_data:
            self.__user_data.update({user_id: []})


class DB:
    def __init__(self, path):
        super(DB, self).__init__()
        self.__db_path = path
        self.cursor = None
        self.db = None
        self.init()

    def init(self):
        if not os.path.exists(self.__db_path):
            self.db = sqlite3.connect(self.__db_path, check_same_thread=False)
            self.cursor = self.db.cursor()
            self.cursor.execute('''CREATE TABLE users(
                    name text,
                    year text,
                    janre text,
                    rate text,
                    country text,
                    watchtime text,
                    desc text,
                    link text,
                    cover BLOB
                    )
                    ''')
            self.db.commit()
        else:
            self.db = sqlite3.connect(self.__db_path, check_same_thread=False)
            self.cursor = self.db.cursor()