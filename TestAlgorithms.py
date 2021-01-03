import pyomo.environ as pe
from pyomo.core.base.block import generate_cuid_names

from pyomo.opt import SolverFactory
from pyomo.opt import SolverStatus, TerminationCondition


from BoxConstrainedGO_Algorithms import *
from CirclePacking2 import *
import random
import time


#Testing PRS vs Multistart
def main1():
    n = 10
    Multi_n_iter = n*100
    PRS_n_iter = Multi_n_iter*n*60

    seed1 = 42

    gen_multi = random.Random()

    # chosing the solver
    localsolver = create_solver('knitro')
    
    #mymodel = Rastrigin(n, -5.12, 5.12)
    #mymodel = Griewank(n, -600,600)
    mymodel = CirclePacking(4,0,1)

    #needed to retrieve variable names
    labels = generate_cuid_names(mymodel)

    tech_time = time.process_time()

    logfile = open("mylog.txt", 'w')

    gen_multi.seed(seed1)
    # launching multistart
    FoundSolution = multistart(mymodel, Multi_n_iter, gen_multi, localsolver, labels, logfile)

    multistart_time = time.process_time()

    print("-----------------\n\n")
        
    #restarting from same seed
    gen_multi.seed(seed1)
    purerandomsearch(mymodel, PRS_n_iter, gen_multi, labels, logfile)

    prs_time = time.process_time()

    print("\n--------------\nLoading... ", tech_time)
    print("Multistart ", multistart_time - tech_time)

    print("PRS ", prs_time - multistart_time)
    print("Total ", prs_time)

# Testing Multistart
def main3():
    
    infofile = open("infoMStart.txt", 'w')
    infofile.write("N R_FOUND    SOLUTION   PERC_ERR   TIME_MBH\n")
    Rfile = open("real_R.txt", 'r')
    lines = Rfile.readlines()
    
    n_min = 2
    n_max = 50
    
    real_R = [0]*n_max
    
    for i in range(n_min, n_max): 
        real_R[i] = lines[i-1].split()[1]
        
    for i in range(n_min, n_max):
        n = 6
        
        max_no_improve = n*2
    
        seed1 = 123
        seed2 = 48
    
        gen = random.Random()
        pert = random.Random()
        
        # chosing the solver
        localsolver = create_solver('knitro')
        
        # mymodel = Rastrigin(n, -5.12, 5.12)
        # mymodel = Griewank(n, -600,600)
        mymodel = CirclePacking(i,0,1)
        # mymodel = CubeCirclePacking(8,0,1)
    
        #needed to retrieve variable names
        labels = generate_cuid_names(mymodel)
    
        tech_time = time.process_time()
    
        gen.seed(seed1)
        pert.seed(seed2)
        delta = 0.8
    
        logfile = open("mylog.txt", 'w')
        
        
        # launching multistart
        r = float(real_R[i])
        FoundSolution = multistart(mymodel, gen, localsolver, labels, max_no_improve, pert, delta, logfile, infofile, i, r)
    
        multistart_time = time.process_time()
        infofile.write("{0:8.8f} \n".format(multistart_time - tech_time))
        
        logfile.close()
        
        print("\n--------------\nLoading... ", tech_time)
        print("MBH ", multistart_time - tech_time)
    
    
        print("Total ", mbh_time)
    
    infofile.close()
    
    
# Testing MBH
def main2():
    
    infofile = open("info.txt", 'w')
    infofile.write("N R_FOUND    SOLUTION   PERC_ERR   TIME_MBH\n")
    Rfile = open("real_R.txt", 'r')
    lines = Rfile.readlines()
    
    n_min = 5
    n_max = 15
    
    real_R = [0]*n_max
    
    for i in range(n_min, n_max): 
        real_R[i] = lines[i-1].split()[1]
        
    for i in range(n_min, n_max):
        n = 6
        
        max_no_improve = n*2
    
        seed1 = 123
        seed2 = 48
    
        gen = random.Random()
        pert = random.Random()
        
        # chosing the solver
        localsolver = create_solver('knitro')
        
        # mymodel = Rastrigin(n, -5.12, 5.12)
        # mymodel = Griewank(n, -600,600)
        mymodel = CirclePacking(i,0,1)
        # mymodel = CubeCirclePacking(8,0,1)
    
        #needed to retrieve variable names
        labels = generate_cuid_names(mymodel)
    
        tech_time = time.process_time()
    
        gen.seed(seed1)
        pert.seed(seed2)
        delta = 0.8
    
        logfile = open("mylog.txt", 'w')
        
        
        # launching multistart
        r = float(real_R[i])
        FoundSolution = MBH(mymodel, gen, localsolver, labels, max_no_improve, pert, delta, logfile, infofile, i, r)
    
        mbh_time = time.process_time()
        infofile.write("{0:8.8f} \n".format(mbh_time - tech_time))
        
        logfile.close()
        
        print("\n--------------\nLoading... ", tech_time)
        print("MBH ", mbh_time - tech_time)
    
    
        print("Total ", mbh_time)
    
    infofile.close()


    

# Testing MBH
def main4():
    
    infofile = open("infoMStart.txt", 'w')
    infofile.write("N R_FOUND    SOLUTION   PERC_ERR   TIME_MBH\n")
    Rfile = open("real_R.txt", 'r')
    lines = Rfile.readlines()
    
    n_min = 2
    n_max = 50
    
    real_R = [0]*n_max
    
    for i in range(n_min, n_max): 
        real_R[i] = lines[i-1].split()[1]
        
    for i in range(n_min, n_max):
        n = 6
        
        max_no_improve = n*2
    
        seed1 = 123
        seed2 = 48
    
        gen = random.Random()
        pert = random.Random()
        
        # chosing the solver
        localsolver = create_solver('knitro')
        
        # mymodel = Rastrigin(n, -5.12, 5.12)
        # mymodel = Griewank(n, -600,600)
        mymodel = CirclePacking(i,0,1)
        # mymodel = CubeCirclePacking(8,0,1)
    
        #needed to retrieve variable names
        labels = generate_cuid_names(mymodel)
    
        tech_time = time.process_time()
    
        gen.seed(seed1)
        pert.seed(seed2)
        delta = 0.8
    
        logfile = open("mylog.txt", 'w')
        
        
        # launching multistart
        r = float(real_R[i])
        FoundSolution = MBH(mymodel, gen, localsolver, labels, max_no_improve, pert, delta, logfile, infofile, i, r)
    
        mbh_time = time.process_time()
        infofile.write("{0:8.8f} \n".format(mbh_time - tech_time))
        
        logfile.close()
        
        print("\n--------------\nLoading... ", tech_time)
        print("MBH ", mbh_time - tech_time)
    
    
        print("Total ", mbh_time)
    
    infofile.close()
    
if __name__ == '__main__':
    main2()
