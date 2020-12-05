class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        range1 = self.width
        range2 = self.height

        if(range1>50 or range2>50):
            return "Too big for picture."

        elif(range1<=0 or range2<=0):
            return "Wrong infromation"

        else:
            for i in range(range1):
                if(i==0):
                    pass
                else:
                    print('')
                for j in range(range2):
                    print('*',end='')

    def __str__(self):
        result = 'Rectangle(width={0}, height={1})'.format(self.width,self.height)
        return result

class Square(Rectangle):
    def __init__(self,side):
        self.width = side
        self.height = side

    def set_side(self,side):
        self.width = width











