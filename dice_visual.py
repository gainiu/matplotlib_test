from die import Die
import pygal

die_1= Die()
die_2= Die()

results=[die_1.roll()+die_2.roll() for roll_num in range(1000)]
# for roll_num in range(1000):
#     result=die_1.roll()+die_2.roll()
#     results.append(result)


max_result=die_1.num_sides+die_2.num_sides
frequencies=[results.count(value) for value in range(2,max_result+1)]
# for value in range(2,max_result+1):
#     frequency=results.count(value)
#     frequencies.append(frequency)

#对结果进行可视化
hist=pygal.Bar()

hist.title='Results of rolling two D6 1000 times'
hist.x_labels=[str(result) for result in range(2,die_1.num_sides+die_2.num_sides+1)]
hist.x_title='Result'
hist.y_title='Frequency of Result'

hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')