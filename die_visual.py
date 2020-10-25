from die import Die
import pygal

die= Die()

results=[die.roll() for roll_num in range(1000)]
# for roll_num in range(1000):
#     result=die.roll()
#     results.append(result)

frequencies=[results.count(value) for value in range(1,die.num_sides+1)]
# for value in range(1,die.num_sides+1):
#     frequency=results.count(value)
#     frequencies.append(frequency)

#对结果进行可视化
hist=pygal.Bar()

hist.title='Results of rolling one D6 1000 times'
hist.x_labels=[result for result in range(1,die.num_sides+1)]
hist.x_title='Result'
hist.y_title='Frequency of Result'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')