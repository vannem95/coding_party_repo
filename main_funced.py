import numpy as np
import matplotlib.pyplot as plt
import time as tm

def euler_step(state,dt):

	th = state[0]
	dth = state[1]

	m = 1.0
	g = 9.8
	L = 1.0

	ddth = - m * g * L * np.sin(th)
	dth2 = dth + ddth*dt
	th2 = th + dth2*dt

	state2 = [th2, dth2]
	return state2

def main(argv=None):
	
	t0 = 0.0
	tf = 2.0
	tstep = 0.05
	time = np.arange(t0 , tf , tstep)

	pendL = 1.0
	pendTH = np.pi/3.0
	dTH = 0.0
	pendM = 1.0
	g = 9.8

	lim = 1.5

	for t in time:

		# ddTH = -pendM*g*pendL*np.sin(pendTH)
		# dTH += ddTH*tstep
		# pendTH += dTH*tstep

		[pendTH,dTH] = euler_step([pendTH,dTH],tstep)

		pendX = pendL*np.sin(pendTH)
		pendY = -pendL*np.cos(pendTH)
		plt.cla()
		plt.plot([0.0,pendX],[0.0,pendY])
		circle1 = plt.Circle((pendX, pendY), 0.1, color='r')
		plt.gca().add_patch(circle1)
		plt.axis(lim*np.array([-1,1,-1,1]))
		plt.pause(.001)



if __name__ == "__main__":
	main()