from die import Die
import pygal
import matplotlib.pyplot as plt

die_1= Die()
die_2= Die()

results=[die_1.roll()+die_2.roll() for roll_num in range(1000)]

max_result=die_1.num_sides+die_2.num_sides
frequencies=[results.count(value) for value in range(2,max_result+1)]

x_values=[result for result in range(2,max_result+1)]

plt.plot(x_values,frequencies,linewidth=5)
plt.title('Results of rolling two D6 1000 times',fontsize=24)
plt.xlabel('Result',fontsize=14)
plt.ylabel('Frequency of Result',fontsize=14)
plt.show()

#对结果进行pygal可视化
# hist=pygal.Bar()

# hist.title='Results of rolling two D6 1000 times'
# hist.x_labels=[str(result) for result in range(1,max_result+1)]
# hist.x_title='Result'
# hist.y_title='Frequency of Result'

# hist.add('D6*D6',frequencies)
# hist.render_to_file('159_visual.svg')