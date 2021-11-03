class MTC
    def __innit__(self, sourname , name , fathers_name ,
                  date_of_birth , sex , connection_date , balance , rate)
        """
        
        :param sourname: first name of the user
        :param name: name of the user
        :param fathers_name: last name of the user
        :param date_of_birth: when was born the user
        :param sex: men or woman
        :param connection_date: date of connection
        :param balance: couner
        :param rate: what did user choose
        :return:
        """
        self.sourname = sourname
        self.name = name
        self.fathers_name = fathers_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.connection_date = connection_date
        self.balance = balance
        self.rate = rate
