import numpy as np
import matplotlib.pyplot as plt

pop1 = 500
pop2 = 500

ppl_tall = 28 + 4 * np.random.randn(pop1)
ppl_short = 24 + 4 * np.random.randn(pop2)


plt.hist([ppl_tall, ppl_short],width=1.0, stacked=True, color=['r', 'b'])
plt.show()
