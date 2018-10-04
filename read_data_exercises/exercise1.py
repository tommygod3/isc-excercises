print("---------- Exercise 1 script ----------")

print("Question 1:")
def read_header(filename):
    dic = {}
    with open(filename, "r") as reader:
        for i in range(0,3):
            line = reader.readline().strip().split(":")
            (key, value) = line
            dic[key] = value
    return dic
print(f"Header:\n{read_header('data/weather_meta.csv')}")

def read_data(filename):
    data = {}
    with open(filename, "r") as reader:
        for i in range(0, 3):
            reader.readline()
        col_names = reader.readline().strip().split(",")
        for name in col_names:
            data[name] = []
        for line in reader.readlines():
            values = line.strip().split(",")
            for (i, value) in enumerate(values):
                col_name = col_names[i]
                data[col_name].append(value)
    return data
print(f"Data:\n{read_data('data/weather_meta.csv')}")

print("Question 2:")
class Weather(object):

    def __init__(self, filename):
        self.filename = filename
        self.read_header()
        self.read_data()

    def read_header(self):
        dic = {}
        with open(self.filename, "r") as reader:
            for i in range(0,3):
                line = reader.readline().strip().split(":")
                (key, value) = line
                dic[key] = value
        self.header = dic
        
    def read_data(self):
        data = {}
        with open(self.filename, "r") as reader:
            for i in range(0, 3):
                reader.readline()
            col_names = reader.readline().strip().split(",")
            for name in col_names:
                data[name] = []
            for line in reader.readlines():
                values = line.strip().split(",")
                for (i, value) in enumerate(values):
                    col_name = col_names[i]
                    data[col_name].append(value)
        self.data = data

weather = Weather("data/weather_meta.csv")
print(f"Header:\n{weather.header}")
print(f"Data:\n{weather.data}")
