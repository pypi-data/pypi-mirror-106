import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import display, Image
from matplotlib.animation import ArtistAnimation
import numpy as np
from matplotlib import pyplot as plt
import os
from matplotlib import animation, rc
from scipy.interpolate import interp1d
import numba as nb
from numba import jit, f8, int32,b1
import time
from tqdm import tqdm

class onedproblem:
    '''
    Make a 1D problem for the tutorial
    '''
    # You can add default probes here
    probe = {

    }
    mat_dict = {
        'conductor':{
            'k':40,
            'rho':1820,
            'cp':880,
            },
        'brick':{
            'k':1/1.25,
            'rho':1820,
            'cp':880,
            },
        'epf':{
            'k':0.035,
            'rho':24,
            'cp':1340,
            },
        'plywood':{
            'k':0.1,
            'rho':600,
            'cp':2500,
            },
        'rockwool':{
            'k':0.045,
            'rho':100,
            'cp':860,
            },
        'osb':{
            'k':0.5,
            'rho':600,
            'cp':1300,
            },
        'airgap':{
            'k':0.02,
            'rho':1.3,
            'cp':1000,
            },
        'plaster':{
            'k':0.2,
            'rho':750,
            'cp':830,
            }
        }

    def __init__(self,wall_mats,layer_thicknesses,B0=273.15,B1=273.15+21,debug=False):
        '''
        param wall_mats: list of wall materials (brick)
        param layer_thicknesses: list of thicknesses in (m)
        param B0: Outer boundary (K)
        param B1: Inner boundary (K)
        param debug: Turns off many iterations in the run_problem step.
        '''
        self.mats = wall_mats
        self.L    = layer_thicknesses
        self.B0   = B0
        self.B1   = B1
        self.debug = debug

    def setup_grid(self,nx,time,fps=24):
        '''
        This function sets up the whole grid.

        param nx: number of grid points
        param time: time of the simulation

        There exists a x grid:
        x_0     x_1     x_2     x_3    x_4   x_nx-1   x_nx     x_(nx+1)
         |-------|-------|-------|------|.....|-------|-------|
         mapping of the wall sections:
             |-------|-------|-------|............|-------|
             | wall                                  wall |
             | starts                                ends |
               cp_0                                cp_N-1
               rho_0                              rho_N-1
               k_0                                  k_N-1

         Boundaries are set on the x_0 and the x_(nx+1) node.
         B0                                                   B1

         How do we split with regard with material sections?
            Everything is just a oppinion and we might change this in the future
            but for now-> we do something simple like this:

             | mat 1           | mat 2 ->
        x_0     x_1     x_2     x_3    x_4   x_nx-1   x_nx    x_(nx+1)
         |-------|-------|-------|------|......|-------|-------|
            U_0     U_1     U_2     U_3           ...     U_nx
        T_0     T_1     T_2     T_3    T_4   T_nx-1   T_nx    T_(nx+1)
         |-------|-------|-------|------|......|-------|-------|
             |-------|-------|-------|.............|-------|
             | wall                                   wall |
             | starts                                 ends |
               cp_0     cp_1   cp_2               cp_(nx-1)
               rho_0    rho_1  rho_2             rho_(nx-1)
               k_0      k_1    k_2                 k_(nx-1)


        cp_0,rho_0,k_0, etc <- is simply set by x==x_mat bins
        Between x_3-\delta x/2 and x_3+\delta x/2 we cross over to a new
        material
            ratio = ( x_mat - (x_3-\delta x/2) ) / (\delta x)
            cp_2 = cp_mat1 * ratio  + cp_mat2 * (1-ratio)
            rho_2 = rho_mat1 * ratio  + rho_mat2 * (1-ratio)

        Between x_2 and x_3 we transition between a new material to deal with
        this from a conduction standpoint we simply consider a linear resistor
        network.
            U_0 = k_0 / \delta x
            U_nx = k_nx / \delta x
            for n=1..nx-1:
                U_n = 1/ (delta x/k_n +  delta x/k_(+1)) -> W/m2K
                in case of transition:
                    ratio = (x_mat-x_n) / \delta x
                    U_n = 1/ (  ( (delta x * ratio) / k_n +  (delta x * (1-ratio)) /k_(n+1) )  )

        '''

        self.nx=nx
        self.fps=fps
        self.nt=time*fps # number of frames

        # Build the x grid
        self.dx = sum(self.L)/nx
        self.x  = np.linspace(-self.dx/2,sum(self.L)+self.dx/2,nx+2)

        # Build the temperature series
        self.T = np.ones((self.nt,nx+2))*min(self.B0,self.B1) # a numpy array with nx elements all equal to 1.

        # Set the boundary conditions
        self.T[:,0]  = self.B0
        self.T[:,-1] = self.B1

        # mat array of length (nx)
        # and the mapping of cp,rho, k to the mid point grids
        # we also precalculate the m = cp*rho
        self.mat = []
        self.cp  = []
        self.rho = []
        self.m   = []
        self.k   = []
        L_ = [sum(self.L[:i+1]) for i in range(len(self.L))]
        k=0
        for x_ in self.x[1:-1]:
            # reset the ratio for the transition between materials
            if (x_-self.dx/2 <= L_[k]) and (x_+self.dx/2 > L_[k]):
                #print(x_-self.dx/2,'<',L_[k],'<',x_+self.dx/2)
                ratio = (  L_[k] - (x_-self.dx/2) ) / self.dx
                if k==len(L_)-1:
                    # because of the small rounding issue, it will report the
                    # final material to be an cross, using this it will just
                    # report the material itself.
                    self.mat.append(self.mats[k])
                else:
                    self.mat.append('cross')
            else:
                ratio = 1
                self.mat.append(self.mats[k])
            # Go to next material
            if x_ >= L_[k]:
                k+=1
            cp_ = self.mat_dict[self.mats[k]]['cp']*ratio+self.mat_dict[self.mats[k-1]]['cp']*(1-ratio)
            rho_= self.mat_dict[self.mats[k]]['rho']*ratio+self.mat_dict[self.mats[k-1]]['rho']*(1-ratio)
            self.cp.append( cp_)
            self.rho.append(rho_)
            self.m.append(cp_*rho_)
            self.k.append(self.mat_dict[self.mats[k]]['k'])

        self.U = np.zeros(nx+1)
        self.U[0]  = self.k[0]/self.dx
        self.U[-1] = self.k[-1]/self.dx
        k=0
        for i, x_ in enumerate(self.x[1:-2]):
            if x_+self.dx >= L_[k]:
                ratio = ( L_[k]-x_ ) / self.dx
                k+=1
            else:
                ratio=1
            self.U[i+1] = 1/ ((self.dx*ratio)/(self.k[i]) +  (self.dx*(1-ratio))/(self.k[i+1]))

    def setup_timestep(self):
        """
        This function calculates the timestep to use such that we don't have any stabilty.
        """
        # min nu
        self.nu = min([self.mat_dict[mat]['k']/(self.mat_dict[mat]['rho']*self.mat_dict[mat]['cp']) for mat in self.mats])
        self.dx = sum(self.L)/self.nx    # Delta X
        print("Size of the dx: ",np.round(self.dx,4))
        sigma = 0.4 # stability
        self.dt = sigma * self.dx**2 / self.nu # use this to time time step
        print('Timestep:', np.round(self.dt,1))

    def run_problem(self):
        """
        Start running the problem. We will always try to run the problem until we find steady state.
        """
        self.setup_timestep()
        start_time=time.time()
        # when do we reach steady state? - This is some random thing that I thought off.
        U_ = 1/(sum([1/uu for uu in self.U]))
        DT = np.mean(self.m) * 50 / U_
        print("Steady State will be in approximately: ",np.round(DT),"s. \n",
              'With timestep of:',np.round(self.dt,4), "\n",
              'So, we need ', np.round(DT/self.dt/self.nt), "extra timesteps")
        for n in tqdm(range(self.nt-1), desc="Solving problem ..."):  #iterate through time
            self.T[n+1,1:-1] = self.SolveSolid(n,self.T[n,:])
            # multiplier to make sure we show only 15 seconds
            if self.debug == False:
                extra_steps = int(np.round(DT/self.dt/self.nt))
                if extra_steps>0:
                    for multi_ in range(extra_steps):
                        self.T[n+1,1:-1] = self.SolveSolid(n,self.T[n+1,:])
        end_time = time.time()
        print('Calculation time: ', np.round((end_time-start_time)/60,1),'min' )

    @staticmethod
    @jit(f8[:] (f8[:],f8[:],f8[:],f8[:] ),nopython=True)
    def TDMAsolver(a, b, c, d):
        '''
        TDMA solver, a b c d can be NumPy array type or Python list type.
        refer to http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
        and to http://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_(Thomas_algorithm)
        '''
        nf = len(d)  # number of equations
        ac = np.copy(a)
        bc = np.copy(b)
        cc = np.copy(c)
        dc = np.copy(d)
        for it in range(1, nf):
            mc = ac[it - 1] / bc[it - 1]
            bc[it] = bc[it] - mc * cc[it - 1]
            dc[it] = dc[it] - mc * dc[it - 1]
        xc = bc
        xc[-1] = dc[-1] / bc[-1]

        for il in range(nf - 2, -1, -1):
            xc[il] = (dc[il] - cc[il] * xc[il + 1]) / bc[il]

        return xc

    def SolveSolid(self,t,T):
        '''
        This is a simplified version of the solid solver I used for my PhD
        thesis.

        param N: number of nodes
        isn: The temperature array in K in the next timestep array->length N
        sp: The temperature array in K of the current timestep array->length N
        M: c_p(x) x rho(x) array->length N
        U: resistance between the layers array->length N+1

        We solve the following type of equation:
        $ \frac[M_x ( T_x - \bar(T_x)][ \delta t] = - U_x ( T_(x-1) - T_x) - U_(x+1) ( T_(x+1) - T_x) $
        '''
        # Prepare material properties
        a = np.zeros(self.nx)
        b = np.zeros(self.nx)
        c = np.zeros(self.nx)
        d = np.zeros(self.nx)
        snext = np.zeros(self.nx)
        # Add a value at the end
        for j in range(self.nx):  # This will loop through 0 to N-1 which aligns with 1->N-1
            # Build tridagonal matrix coefficients 0->N
            a[j] = 0
            b[j] = self.m[j]/self.dt
            c[j] = 0
            d[j] = (self.m[j]/self.dt-self.U[j]-self.U[j+1])*T[j+1]+self.U[j]*T[j]+self.U[j+1]*T[j+2]
        # Solve the unknown matrix 1-> N-1
        snext = self.TDMAsolver(a[1:], b, c[:-1], d)
        return snext


    def add_probe(self,x,type):
        """
        Updates the probe libary

        param x: the location of the probe
        param type: Temp for temperature, Heat for q
        """
        n_ = len(self.probe)
        self.probe.update({f'probe {n_}':{'x':x,'type':type}})
        print(self.probe)

    def build_animation(self,scale="K",layers=True,filename='animation.mp4'):
        """
        This function builds the animation and pulished it as a mp4 file.

        param scale: Either "K", "C" for Kelvin or Celcius
        param layers: Turn on layer visualization using a dotted line.
        param filename: provide a different filename. Default is animation.mp4

        """
        # First set up the figure, the axis, and the plot element we want to animate
        fig, ax = plt.subplots(figsize=(6,4))
        if scale=="K":
            ax.set_ylabel("Temperature (K)")
            sub=0
        else:
            ax.set_ylabel("Temperature (C)")
            sub=273.15

        ax.set_xlim((0,sum(self.L)))
        ax.set_ylim((self.B0-sub, self.B1-sub))
        ax.set_xlabel("Wall Depth (m)")

        line, = ax.plot([], [], lw=2)
        anno = []
        probe = []
        if layers:
            L_ = [sum(self.L[:i+1]) for i in range(len(self.L))]
            for l_ in L_:
                probe.append(ax.axvline(x = l_, color = 'k', linestyle=':', label = 'mat'))

        for i, key in enumerate(self.probe.keys()):
            # get the probes
            if self.probe[key]['type']== "Temp":
                anno.append(ax.text(self.probe[key]['x']-self.probe[key]['x']*0.05, self.B1-3-sub, "Direction", ha="right", va="center",  size=15))
                probe.append(ax.axvline(x = self.probe[key]['x'], color = 'k', label = 'Temperature Probe'))
            if self.probe[key]['type']== "Heat":
                anno.append(ax.text(self.probe[key]['x']-self.probe[key]['x']*0.05, self.B1-6-sub, "Direction", ha="right", va="center",  size=15))
                probe.append(ax.axvline(x = self.probe[key]['x'], color = 'k', label = 'Heat Probe'))


        # initialization function: plot the background of each frame
        def init():
            line.set_data([], [])
            return (line,anno,probe)
        # animation function. This is called sequentially
        def animate(i):
            # Actual axis
            x = np.linspace(0, sum(self.L), self.nx+1)
            y = np.array([(T+self.T[i,n+1])/2 for n,T in enumerate(self.T[i,:-1])])-sub
            u = self.U
            y_interp = interp1d(x,y)
            u_interp = interp1d(x,u)
            line.set_data(x, y)
            for m, key in enumerate(self.probe.keys()):
                # get the probes
                if self.probe[key]['type']== "Temp":
                    temp_ = y_interp(self.probe[key]['x'])
                    if scale=="K":
                        add_="K$^\circ$"
                    else:
                        add_="C$^\circ$"
                    anno[m].set_text(f'T: {np.round(temp_,1)} {add_}')
                if self.probe[key]['type']== "Heat":
                    x_=self.probe[key]['x']
                    cond_ = u_interp(x_) * (y_interp(x_+self.dx/2) - y_interp(x_-self.dx/2)  )
                    anno[m].set_text(f'q: {np.round(cond_,2)} W/m$^2$')

            return (line,anno,probe)

        # # call the animator. blit=True means only re-draw the parts that have changed.
        anim = animation.FuncAnimation(fig, func=animate, init_func=init,
                                    frames=self.nt, interval=round(1000/self.fps), blit=False, repeat=False)
        # plt.show()

        start_time = time.time()
        basepath= os.path.dirname(__file__)
        filepath = os.path.join(basepath, filename)
        writervideo = animation.FFMpegWriter(fps=self.fps)
        anim.save(filepath, writer=writervideo)
        print("File saved!")
        end_time = time.time()
        print("Render time: ",np.round((end_time-start_time)/60,1),'min')
