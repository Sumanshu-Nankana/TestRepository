import time
class TestFunction():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    # format = "Test12dd4dd"

    def generate_insert_query(self):
        file = open('query.txt', 'w+')
        while self.start <= self.end:
            self.start_str = str(self.start)
            if len(self.start_str) < 4:
                self.temp = str('0'*(4-len(self.start_str)) + self.start_str)
            else:
                self.temp = self.start_str
            
            self.number = 'Test12'+self.temp[0:2]+'4'+self.temp[2:4]
            query = "INSERT INTO TABLE (ID, NAME, "+ self.number+");"
            file.write(query)
            file.write("\n")
            self.start = self.start + 1
        file.close()


if __name__ == '__main__':
    tf = TestFunction(0, 9999)
    tf.generate_insert_query()

