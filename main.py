import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation
import math

# First set up the figure and the axis
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])


### Read-in Abstract Machine from file
def read_file(filename):
	global abstract_machine, alphabet, title, initial_state, acceptable_states, states
	abstract_machine = dict()
	alphabet = []
	title = ""
	initial_state = ""
	acceptable_states = []
	with open(filename) as f:
		initialized = False
		for line in f:
			line = line.strip("\n")
			elements = line.split(",")
			if not initialized:
				title = elements[0]
				alphabet =  elements[1:]
				initialized = True
			else:	
				if elements[0].startswith("*"):
					elements[0] = elements[0].strip("*")
					acceptable_states.append(elements[0])
				abstract_machine[elements[0]] = elements[1:]
				if initial_state == "":
					initial_state = elements[0]

	states = list(abstract_machine.keys())
	print("Title:")
	print(title)
	print("Alphabet:")
	print(alphabet)
	print("Abstract Machine:")
	print(abstract_machine)	
	print("Initial State:")
	print(initial_state)
	print("Acceptable States")
	print(acceptable_states)

read_file("abstract_machine.am")

# Initialization
def init():
	objects=[]
	# Rectangles
	for i in range(len(states)):
		objects.append(patches.Circle((0.125 + i*0.25, 0.5), 0.05, facecolor="#ede980", edgecolor="Black"))
		plt.text(0.125 + i*0.25, 0.5, states[i], horizontalalignment="center", verticalalignment="center")

	for obj in objects:
		ax.add_patch(obj)

	return objects
init()
#anim = animation.FuncAnimation(fig, None, init_func=init, interval=0.01, blit=True)

plt.show()
