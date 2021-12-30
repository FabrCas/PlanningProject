from problems.envs import getEnv
from algorithms import getLRTA
from novel_algorithms import getNovelLRTA

# exe options
PROBLEMS = ["BarrierEnv1","BarrierEnv2","Escape","8_puzzle"]
TYPE_ALGORITHMS =["classical","novel"]
NOVELTIES = ["f(n)_disambiguity", "dynamic_depth_limit","gaussian_restart"]

if __name__ == "__main__":
    
    # choose the problem
    problem = PROBLEMS[2]
    # choose whether use classical or a new approach
    type_algorithm = TYPE_ALGORITHMS[1]
    
    # choose the new features to use
    if type_algorithm =="novel":
        novelties_selected = [NOVELTIES[2]]
    else:
        novelties_selected = []
    
    # configure the problem and create the environment 
    env = getEnv(problem)(load_h = False)
    env.create_env()
    
    
    # LRTA* algorithm definition
    lrta_star = getLRTA(problem)(env,) if type_algorithm=="classical" else getNovelLRTA(problem)(env, novelties= novelties_selected)
    
    # launch the algorithm
    
    """ execute(simluation + optimal execution) or just run the algorithm with forward """
    # lrta_star.forward(save_h = False , verbose = True)
    # lrta_star.simulate(save_h = False , verbose = True)
    
    
    """ simulation + final forward """
    lrta_star.execution() 
    
    
    # time = 32.210394620895386 [s] | number of simulations = 112
    # f(n) dis, 8 puzzle easy2
    # time = 45.00187587738037 [s] | number of simulations = 110
    
    
    # time = 0.028105974197387695 [s] | number of simulations = 20