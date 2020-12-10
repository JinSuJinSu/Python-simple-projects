import random

class Hat:
    def __init__(self,**kwargs):
        self.contents  = []
        content_color =  list(kwargs.keys())
        content_number = list(kwargs.values())

        for i in range(len(content_color)):
            for j in range(content_number[i]):
                self.contents.append(content_color[i])

    def draw(self,num):
        draw_array = []
        choiceLIst = random.sample(self.contents, num)
        for i in choiceLIst:
            self.contents.remove(i)
            draw_array.append(i)

        return draw_array


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    #create new_hat_contents variable

    new_hat_contents=[]

    for i in hat.contents:
        new_hat_contents.append(i)
        
    ball_count = 0

    for i in range(num_experiments):

        # create choosen_balls variable to check probability

        choosen_balls = []

        if(num_balls_drawn>=len(new_hat_contents)):
            return 1.0

        else:
            for i in range(num_balls_drawn):
                choose_ball = random.choice(new_hat_contents)
                choosen_balls.append(choose_ball)
                new_hat_contents.remove(choose_ball)

        #init new_hat_contents

        new_hat_contents=[]

        for i in hat.contents:
            new_hat_contents.append(i)
        
        color_count = 0

        for key,value in expected_balls.items():
            if(choosen_balls.count(key))>=value:
               color_count+=1

        if(color_count==len(expected_balls)):
            ball_count+=1

    return ball_count/num_experiments







      


 
  