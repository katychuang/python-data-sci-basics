from s5q2 import *


import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.style.use('ggplot')
colors=plt.rcParams['axes.color_cycle']

x = 1

# cotton_and_striped comes from s5q2.py
for tie in cotton_and_striped[1:]:
    ax.bar(x, float(tie[2]) ) 
    x += 1

ax.set_title('FILL THIS IN')
ax.set_ylabel('FILL THIS IN')
ax.set_xlabel('FILL THIS IN')

plt.grid(True)
fig.savefig('s5q3.png')

# code above this line is shown to student. They will fill in lines 16-18.
# -------------------------------------------------------------------------

# here is the answer:

ax.set_title('Cotton and Stripes')
ax.set_ylabel('Price')
ax.set_xlabel('Ties')

# See the example code snippet displayed [above]. We want to plot the price of the cotton and striped ties cotton_and_striped on a bar chart and set the title variable to be ‘Cotton and Stripes’. How would you fill in the strings that say 'FILL THIS IN'?




