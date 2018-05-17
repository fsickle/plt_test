from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []
for rooll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_side + die_2.num_side
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 可视化
hist = pygal.Bar()

hist.title = 'Result of rolling two D6 1000 times'
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')
