import numpy as np
import matplotlib.pyplot as plt
import time as tm


def main(argv=None):
	
	t0 = 0.0
	tf = 10.0
	tstep = 0.1
	time = np.arange(t0 , tf , tstep)

	pendL = 1.0
	pendTH = np.pi/3.0
	dTH = 0.0
	pendM = 1.0
	g = 9.8

	for t in time:

		ddTH = -pendM*g*pendL*np.sin(pendTH)
		dTH += ddTH*tstep
		pendTH += dTH*tstep
		pendX = pendL*np.sin(pendTH)
		pendY = -pendL*np.cos(pendTH)
		plt.cla()
		plt.plot([0.0,pendX],[0.0,pendY])
		circle1 = plt.Circle((pendX, pendY), 0.2, color='r')
		plt.gca().add_patch(circle1)
		plt.axis([-2,2,-2,2])
		plt.pause(.05)




if __name__ == "__main__":
	main()