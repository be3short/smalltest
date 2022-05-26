"""Bouncing ball model"""
import osdt
import math

class State():  # state
    def __init__(self, angle=1.0,velocity=0.0):
        self.angle = angle
        self.velocity = velocity

class Params():  # parameters
    def __init__(self, length=1.0, mass=1.0, gravity =9.81):
        self.length = length
        self.mass = mass
        self.gravity = gravity


def F(x, x_dot, hs):
    x_dot.angle = x.velocity
    x.acceleration = -(hs.params.gravity/hs.params.length)*math.sin(x.angle)
    x_dot.velocity = x.acceleration

def C(x,hs):
    return True


#if __name__ == "__main__":
def main():
    osdt.clear()
    system = create()

    # run the simulation
    osdt.run(time=10.0, jumps=20)

    # create a figure
    fig = osdt.create_fig(layout=[[1],[2]],
                                 title="Pendulum",
                                 width=1600, height=600)

    # plot the angle and velocity
    fig.plot(1,"angle")
    fig.plot(2,"velocity")
    osdt.plotting.display()
    # display all figures
   # osdt.display()




def create(state=State(),params=Params(),c=C,f=F,u=None,y=None,initialize=None,routine=None,id="pendulum"): # create a new system
    return osdt.create_sys(x=state,params=params,c=c,f=f,u=u,y=y,initialize=initialize,routine=routine,id=id)



