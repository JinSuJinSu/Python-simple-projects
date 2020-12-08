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

  new_hat_contents = []

  # move hat.contents to new_hat_contents

  for i in hat.contents:
    new_hat_contents.append(i)

  # find count of expected balls

  ball_count = 0

  for i in range(num_experiments):
    # choose random balls
    chosen_balls = []
    if num_balls_drawn > len(new_hat_contents):
      return 1.0

    else:

      for i in range(num_balls_drawn):
        chose_ball = random.choice(new_hat_contents)
        chosen_balls.append(chose_ball)
        new_hat_contents.remove(chose_ball)


      # replace new_hat_contents

      new_hat_contents = []
      for i in hat.contents:
        new_hat_contents.append(i)


      # count the expected colors in chosen balls

      color_count = 0

      for key, value in expected_balls.items():
        if chosen_balls.count(key) >= value:
          color_count += 1


      # check if color count equals the expected ball colors

      if color_count == len(expected_balls):
        ball_count += 1


  return ball_count/num_experiments

hat =Hat(red=5,blue=2)
print(hat.draw(2))





    