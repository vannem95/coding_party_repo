import numpy as np
import matplotlib.pyplot as plt
import time as tm


def main(argv=None):
	
	t0 = 0.0
	tf = 20.0
	tstep = 0.1
	time = np.arange(t0 , tf , tstep)

	r1 = 1
	r2 = 2
	th = 0

	for t in time:

		# increase th by 1 degrees
		th += 2*np.pi/180.0

		cx = (r1 + r2)*np.cos(th)
		cy = (r1 + r2)*np.sin(th)

		plt.cla()
		circle1 = plt.Circle((0, 0), r1, color='b')
		circle2 = plt.Circle((cx, cy), r2, color='r', fill=False)

		plt.plot([0,cx],[0,cy],	linewidth=2.0)

		c2x = cx + (r2*np.cos((r1+r2)*th))
		c2y = cy + (r2*np.sin((r1+r2)*th))
		plt.plot([c2x,cx],[c2y,cy])

		plt.gca().add_patch(circle1)
		plt.gca().add_patch(circle2)
		plt.axis('equal')
		plt.axis(6*np.array([-1,1,-1,1]))
		plt.pause(.05)




if __name__ == "__main__":
	main()