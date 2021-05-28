class RectProgram:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def input_data(self):
        self.length = float(input("enter the length of a rectangle \n"))
        self.width = float(input(" enter the width of a rectangle \n "))

    def output_result(self):
        print(" area of a rectangle is :\n", self.calc_area())
        print(" perimeter of a rectangle is :\n", self.calc_perimeter())

    def calc_area(self):
        return self.length * self.width

    def calc_perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    obj = RectProgram(6, 4)
    obj.output_result()
    obj2 = RectProgram(0, 0)
    obj2.input_data()
    obj2.output_result()
