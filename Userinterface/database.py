import sqlite3 as sq


class PhoneBook:
    con = sq.connect('phonebook.sqlite3')

    def __init__(self):    # dunder   initializer
        try:
            self.cur = self.con.cursor()
            self.cur.execute(
                'Create table if not exists PHONEBOOK(name text,address text,mobile text unique) ')
            print(' Table created / already exists ')
        except Exception as e:
            print(f'Please fix this {e}')

    def addData(self, name, address, mobile):
        try:
            self.cur.execute(
                'insert into PHONEBOOK values(?,?,?)', (name, address, mobile))
            self.con.commit()
            # print('successfully added data ')
        except Exception as e:
            print(f'Please fix this {e}')

    def getData(self, mobile):
        try:
            self.cur.execute(
                ' select name,address,mobile from PHONEBOOK where mobile=(?)', (mobile,))
            self.data = self.cur.fetchone()

            print(self.data)
            # print(' retrieved some value ')
            return self.data
        except Exception as e:
            print(f'Please fix this {e}')

    def getRecord(self):
        try:
            self.cur.execute('select * from PHONEBOOK')
            self.data = self.cur.fetchall()
            for r in self.data:
                print(r)
            # print(' retrieved some value ')
            # return self.data
        except Exception as e:
            print(f'Please fix this {e}')


if __name__ == '__main__':
    phoneDiary = PhoneBook()
    phoneDiary.addData('rishit', 'Madhya Pradesh', '7890')
    phoneDiary.addData('amit', 'patna', '93341211')
    phoneDiary.addData('ankit', 'Delhi', '8238822')

    # print(phoneDiary.getData('8210638822'))

    result = phoneDiary.getData('8210638822')
    print(result)
    print(type(result))
