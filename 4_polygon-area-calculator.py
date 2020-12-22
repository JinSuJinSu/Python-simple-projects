#create a rectangle class
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
        range1 = self.height
        range2 = self.width

        result_picture=''


        if(range1>50 or range2>50):
            return "Too big for picture."

        elif(range1<=0 or range2<=0):
            return "Wrong infromation"

        else:
            for i in range(range1):
                    result_picture +=('*'*range2) + '\n'

            return result_picture


    def __str__(self):
        result = 'Rectangle(width={0}, height={1})'.format(self.width,self.height)
        return result

    def get_amount_inside(self,shape):
        initial_result = self.get_area()
        shape_result = shape.get_area()
        time = 0
        while shape_result<=initial_result:
            initial_result -= shape_result
            time +=1

        return time


# create a square class by inheriting the rectangle class
class Square(Rectangle):
    def __init__(self,side):
        self.width = side
        self.height = side

# the square has all same length
    def set_side(self,side):
        self.width = side
        self.height = side

    def __str__(self):
        result = 'Square(side={0})'.format(self.width)
        return result
















