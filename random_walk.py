# 每次决策使用choice决定使用哪边
from random import choice

class RandomWalk():
    '''生成随即漫步数据'''
    def __init__(self,num_points=5000):
        self.num_points = num_points
        
        # 所有随即漫步始于 (0,0)
        self.x_value = [0]
        self.y_value = [0]
    
    # 决定每次漫步方向
    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            # 决定前进方向与距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
                
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            
            self.x_value.append(next_x)
            self.y_value.append(next_y)
        
