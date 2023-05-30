import numpy
import random
import asyncio

""" 
Purpose: 
    To represent a 3d spacetime point's values which oscillate like quantum foam. A strong nuclear force will return
    the point to it's base vacuum state, which increases in attractive strength with the distance squared.
    
    Next major version should be a kernel that oscillates across a matrix, comprised of vectors of Point classes
    with a shared sense of force, as in a fabric.

Theory: 
    A spacetime point in total vacuum will be represented by a 1.0. The value will random "stretch" and "bend" in 
    the three vectors that represent point. When the kernel is implemented, a matrix of these points could be a fabric
    that is plucked, and the distance the center point that is plucked travels determines the shape of the matrix. The
    matrix would grow with the distance. Interesting throught, to try and make the strong nuclear force function
    responsible for determining the distance between points along oblique vectors across the matrix. How could you
    encode a sense of weight to a particle, if it is connected by nodes of force across the geometry of the kernel?
    I suppose the lines of force would be calculated as weights applied to the strong nuclear force, which can break.
    This makes intuitive sense.
    
    If you were to give each spacetime point a tensor which carried these vectors of force across its matrix of
    connections you could give each point a preference for how it moved in various directions in 3 dimensions. Then
    things like folds could appear if those lines of force across the matrices could be given a sense of spatial
    reference to each other.

Considerations:
    How would quantum events be represented in a matrix?
    
    Could states be added, each as an additional binary or one-hot vector? And if so would I need to "fit" a one-hot
    vector describing possible states into how many ticks of the time vector?
"""


class Point:
    def __init__(self):
        self.value = float(1.0)
        self.FORCE_APPLIED = False
        self.gv = 0.0 # the gamma variate result
        self.cs = 0.0 # the chi-squared result
        self.BLACK_SWAN = False
        self.BLACK_SWAN_P_VALUE = {
            "random_variable_inequality": "P(X>x)",
            ".1": 0.23026 # ~P(X>x)=.1 when beta is scale
        }
        # self.MAGNETIC_CONSTANT = .1



    def tick(self):
        """
        This doesn't represent an accelerative force being applied, rather a binary state of FORCE or NO FORCE,
        and it's influence on the point.
        """

        if self.FORCE_APPLIED:

            # various attempts at a distribution I liked
            # self.gv = random.gammavariate(1,.05)
            # self.value = self.value + self.gv
            #
            # self.cs = numpy.random.chisquare(df=.1,size=100)[0]
            # self.value = self.value + self.cs

            self.cs = numpy.random.weibull(1.0, size=None)
            self.value = self.value + self.cs

            # if an event with a p value of .1 occurs from a gamma distribution
            # set the black_swin attribute to true.

            if random.gammavariate(1, .1) > self.BLACK_SWAN_P_VALUE[".1"]:
                self.BLACK_SWAN = True
            else:
                self.BLACK_SWAN = False

        elif not self.FORCE_APPLIED:
            self.value = 1

    @staticmethod
    def strong_nuclear_force(distance):
        """
        Calculates and returns a strong nuclear force.

        Parameters:
            distance = Value magnitude from origin (like, self.value - 1.0).
        """
        force = (1.0 / distance ** 2)

class Clock:
    def __init__(self, rate: int):
        # tick rate in seconds
        self.rate = rate

        # should I add a value for starting point, as if time were a vector, or a single point in time and space with
        # no history?

    async def run(self):
        point = Point()
        point.FORCE_APPLIED = True
        point.tick()
        await asyncio.sleep(self.rate)
        print(f'Value: {point.value}')
        print(f'GV: {point.gv}')
        print(f'CS: {point.cs}')
        print(f'BS: {point.BLACK_SWAN}')
        print(f'-----------------')


for i in range(10):
    print(i,":")
    asyncio.run(Clock(1).run())

