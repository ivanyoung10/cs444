import sys
from agent import Agent
from parse import parse_file



#arguments

#expected arguments:
#main.py [FILE_NAME] [START_CITY] [GOAL_CITY] [ALGORITHM]

if len(sys.argv) <= 1:
    print("Usage: main.py [FILE_NAME] -optional[START_CITY] -optional[GOAL_CITY] -optional[ALGORITHM]")
    sys.exit()
elif len(sys.argv) == 2:
    solutions_file = open("solutions.txt", "w")
    #calling parse function
    file_name = sys.argv[1]
    map, coordinates = parse_file(file_name)
    agent = Agent("brest", "nice", map, coordinates)
    solutions_file.write("Brest --> Nice\n")
    solutions_file.write("--------------------------------\n")
    agent_bfs_results = agent.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent_bfs_results[0]}\ncost:{agent_bfs_results[1]}\nnodes explored:{agent_bfs_results[2]}\nnodes expanded:{agent_bfs_results[3]}\nnodes maintained:{agent_bfs_results[4]}")
    solutions_file.write("\n")
    agent_dls_results = agent.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent_dls_results[0]}\ncost:{agent_dls_results[1]}\nnodes explored:{agent_dls_results[2]}\nnodes expanded:{agent_dls_results[3]}\nnodes maintained:{agent_dls_results[4]}")
    solutions_file.write("\n\n")
    agent_ucs_results = agent.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent_ucs_results[0]}\ncost:{agent_ucs_results[1]}\nnodes explored:{agent_ucs_results[2]}\nnodes expanded:{agent_ucs_results[3]}\nnodes maintained:{agent_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent_astar_results = agent.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent_astar_results[0]}\ncost:{agent_astar_results[1]}\nnodes explored:{agent_astar_results[2]}\nnodes expanded:{agent_astar_results[3]}\nnodes maintained:{agent_astar_results[4]}\n")
    solutions_file.write("\n\n")

    agent2 = Agent("montpellier", "calais", map, coordinates)
    solutions_file.write("Montpellier --> Calais\n")
    solutions_file.write("--------------------------------\n")
    agent2_bfs_results = agent2.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent2_bfs_results[0]}\ncost:{agent2_bfs_results[1]}\nnodes explored:{agent2_bfs_results[2]}\nnodes expanded:{agent2_bfs_results[3]}\nnodes maintained:{agent2_bfs_results[4]}\n")
    solutions_file.write("\n")
    agent2_dls_results = agent2.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent2_dls_results[0]}\ncost:{agent2_dls_results[1]}\nnodes explored:{agent2_dls_results[2]}\nnodes expanded:{agent2_dls_results[3]}\nnodes maintained:{agent2_dls_results[4]}")
    solutions_file.write("\n\n")
    agent2_ucs_results = agent2.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent2_ucs_results[0]}\ncost:{agent2_ucs_results[1]}\nnodes explored:{agent2_ucs_results[2]}\nnodes expanded:{agent2_ucs_results[3]}\nnodes maintained:{agent2_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent2_astar_results = agent2.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent2_astar_results[0]}\ncost:{agent2_astar_results[1]}\nnodes explored:{agent2_astar_results[2]}\nnodes expanded:{agent2_astar_results[3]}\nnodes maintained:{agent2_astar_results[4]}\n")
    solutions_file.write("\n\n")
    agent3 = Agent("strasbourg", "bordeaux", map, coordinates)
    solutions_file.write("Strasbourg --> Bordeaux\n")
    solutions_file.write("--------------------------------\n")
    agent3_bfs_results = agent3.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent3_bfs_results[0]}\ncost:{agent3_bfs_results[1]}\nnodes explored:{agent3_bfs_results[2]}\nnodes expanded:{agent3_bfs_results[3]}\nnodes maintained:{agent3_bfs_results[4]}\n")
    solutions_file.write("\n")
    agent3_dls_results = agent3.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent3_dls_results[0]}\ncost:{agent3_dls_results[1]}\nnodes explored:{agent3_dls_results[2]}\nnodes expanded:{agent3_dls_results[3]}\nnodes maintained:{agent3_dls_results[4]}")
    solutions_file.write("\n\n")
    agent3_ucs_results = agent3.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent3_ucs_results[0]}\ncost:{agent3_ucs_results[1]}\nnodes explored:{agent3_ucs_results[2]}\nnodes expanded:{agent3_ucs_results[3]}\nnodes maintained:{agent3_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent3_astar_results = agent3.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent3_astar_results[0]}\ncost:{agent3_astar_results[1]}\nnodes explored:{agent3_astar_results[2]}\nnodes expanded:{agent3_astar_results[3]}\nnodes maintained:{agent3_astar_results[4]}\n")
    solutions_file.write("\n\n")
    agent4 = Agent("paris", "grenoble", map, coordinates)
    solutions_file.write("Paris --> Grenoble\n")
    solutions_file.write("--------------------------------\n")
    agent4_bfs_results = agent4.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent4_bfs_results[0]}\ncost:{agent4_bfs_results[1]}\nnodes explored:{agent4_bfs_results[2]}\nnodes expanded:{agent4_bfs_results[3]}\nnodes maintained:{agent4_bfs_results[4]}\n")
    solutions_file.write("\n")
    agent4_dls_results = agent4.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent4_dls_results[0]}\ncost:{agent4_dls_results[1]}\nnodes explored:{agent4_dls_results[2]}\nnodes expanded:{agent4_dls_results[3]}\nnodes maintained:{agent4_dls_results[4]}")
    solutions_file.write("\n\n")
    agent4_ucs_results = agent4.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent4_ucs_results[0]}\ncost:{agent4_ucs_results[1]}\nnodes explored:{agent4_ucs_results[2]}\nnodes expanded:{agent4_ucs_results[3]}\nnodes maintained:{agent4_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent4_astar_results = agent4.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent4_astar_results[0]}\ncost:{agent4_astar_results[1]}\nnodes explored:{agent4_astar_results[2]}\nnodes expanded:{agent4_astar_results[3]}\nnodes maintained:{agent4_astar_results[4]}\n")
    solutions_file.write("\n\n")
    agent5 = Agent("grenoble", "paris", map, coordinates)
    solutions_file.write("Grenoble --> Paris\n")
    solutions_file.write("--------------------------------\n")
    agent5_bfs_results = agent5.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent5_bfs_results[0]}\ncost:{agent5_bfs_results[1]}\nnodes explored:{agent5_bfs_results[2]}\nnodes expanded:{agent5_bfs_results[3]}\nnodes maintained:{agent5_bfs_results[4]}\n")
    solutions_file.write("\n")
    agent5_dls_results = agent5.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent5_dls_results[0]}\ncost:{agent5_dls_results[1]}\nnodes explored:{agent5_dls_results[2]}\nnodes expanded:{agent5_dls_results[3]}\nnodes maintained:{agent5_dls_results[4]}")
    solutions_file.write("\n\n")
    agent5_ucs_results = agent5.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent5_ucs_results[0]}\ncost:{agent5_ucs_results[1]}\nnodes explored:{agent5_ucs_results[2]}\nnodes expanded:{agent5_ucs_results[3]}\nnodes maintained:{agent5_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent5_astar_results = agent5.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent5_astar_results[0]}\ncost:{agent5_astar_results[1]}\nnodes explored:{agent5_astar_results[2]}\nnodes expanded:{agent5_astar_results[3]}\nnodes maintained:{agent5_astar_results[4]}\n")
    solutions_file.write("\n\n")
    agent6 = Agent("brest", "grenoble", map, coordinates)
    solutions_file.write("Brest --> Grenoble")
    solutions_file.write("--------------------------------")
    agent6_bfs_results = agent6.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent6_bfs_results[0]}\ncost:{agent6_bfs_results[1]}\nnodes explored:{agent6_bfs_results[2]}\nnodes expanded:{agent6_bfs_results[3]}\nnodes maintained:{agent6_bfs_results[4]}\n")
    solutions_file.write("\n")
    agent6_dls_results = agent6.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent6_dls_results[0]}\ncost:{agent6_dls_results[1]}\nnodes explored:{agent6_dls_results[2]}\nnodes expanded:{agent6_dls_results[3]}\nnodes maintained:{agent6_dls_results[4]}")
    solutions_file.write("\n\n")
    agent6_ucs_results = agent6.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent6_ucs_results[0]}\ncost:{agent6_ucs_results[1]}\nnodes explored:{agent6_ucs_results[2]}\nnodes expanded:{agent6_ucs_results[3]}\nnodes maintained:{agent6_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent6_astar_results = agent6.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent6_astar_results[0]}\ncost:{agent6_astar_results[1]}\nnodes explored:{agent6_astar_results[2]}\nnodes expanded:{agent6_astar_results[3]}\nnodes maintained:{agent6_astar_results[4]}\n")
    solutions_file.write("\n\n")
    agent7 = Agent("grenoble", "brest", map, coordinates)
    solutions_file.write("Grenoble --> Brest")
    solutions_file.write("--------------------------------")
    agent7_bfs_results = agent7.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent7_bfs_results[0]}\ncost:{agent7_bfs_results[1]}\nnodes explored:{agent7_bfs_results[2]}\nnodes expanded:{agent7_bfs_results[3]}\nnodes maintained:{agent7_bfs_results[4]}\n")
    solutions_file.write("\n")
    agent7_dls_results = agent7.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent7_dls_results[0]}\ncost:{agent7_dls_results[1]}\nnodes explored:{agent7_dls_results[2]}\nnodes expanded:{agent7_dls_results[3]}\nnodes maintained:{agent7_dls_results[4]}")
    solutions_file.write("\n\n")
    agent7_ucs_results = agent7.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent7_ucs_results[0]}\ncost:{agent7_ucs_results[1]}\nnodes explored:{agent7_ucs_results[2]}\nnodes expanded:{agent7_ucs_results[3]}\nnodes maintained:{agent7_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent7_astar_results = agent7.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent7_astar_results[0]}\ncost:{agent7_astar_results[1]}\nnodes explored:{agent7_astar_results[2]}\nnodes expanded:{agent7_astar_results[3]}\nnodes maintained:{agent7_astar_results[4]}\n")
    solutions_file.write("\n\n")
    agent8 = Agent("nice", "nantes", map, coordinates)
    solutions_file.write("Nice --> Nantes")
    solutions_file.write("--------------------------------")
    agent8_bfs_results = agent8.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent8_bfs_results[0]}\ncost:{agent8_bfs_results[1]}\nnodes explored:{agent8_bfs_results[2]}\nnodes expanded:{agent8_bfs_results[3]}\nnodes maintained:{agent8_bfs_results[4]}\n")
    solutions_file.write("\n")
    agent8_dls_results = agent8.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent8_dls_results[0]}\ncost:{agent8_dls_results[1]}\nnodes explored:{agent8_dls_results[2]}\nnodes expanded:{agent8_dls_results[3]}\nnodes maintained:{agent8_dls_results[4]}")
    solutions_file.write("\n\n")
    agent8_ucs_results = agent8.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent8_ucs_results[0]}\ncost:{agent8_ucs_results[1]}\nnodes explored:{agent8_ucs_results[2]}\nnodes expanded:{agent8_ucs_results[3]}\nnodes maintained:{agent8_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent8_astar_results = agent8.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent8_astar_results[0]}\ncost:{agent8_astar_results[1]}\nnodes explored:{agent8_astar_results[2]}\nnodes expanded:{agent8_astar_results[3]}\nnodes maintained:{agent8_astar_results[4]}\n")
    solutions_file.write("\n\n")
    agent9 = Agent("caen", "strasbourg", map, coordinates)
    solutions_file.write("Caen --> Strasbourg\n")
    solutions_file.write("--------------------------------")
    agent9_bfs_results = agent9.run('bfs')
    solutions_file.write("BFS\n")
    solutions_file.write(f"path:{agent9_bfs_results[0]}\ncost:{agent9_bfs_results[1]}\nnodes explored:{agent9_bfs_results[2]}\nnodes expanded:{agent9_bfs_results[3]}\nnodes maintained:{agent9_bfs_results[4]}\n")
    solutions_file.write("\n")
    agent9_dls_results = agent9.run("dls")
    solutions_file.write("DLS\n")
    solutions_file.write(f"path:{agent9_dls_results[0]}\ncost:{agent9_dls_results[1]}\nnodes explored:{agent9_dls_results[2]}\nnodes expanded:{agent9_dls_results[3]}\nnodes maintained:{agent9_dls_results[4]}")
    solutions_file.write("\n\n")
    agent9_ucs_results = agent9.run("ucs")
    solutions_file.write("UCS\n")
    solutions_file.write(f"path:{agent9_ucs_results[0]}\ncost:{agent9_ucs_results[1]}\nnodes explored:{agent9_ucs_results[2]}\nnodes expanded:{agent9_ucs_results[3]}\nnodes maintained:{agent9_ucs_results[4]}\n")
    solutions_file.write("\n")
    agent9_astar_results = agent9.run("astar")
    solutions_file.write("A_STAR\n")
    solutions_file.write(f"path:{agent9_astar_results[0]}\ncost:{agent9_astar_results[1]}\nnodes explored:{agent9_astar_results[2]}\nnodes expanded:{agent9_astar_results[3]}\nnodes maintained:{agent9_astar_results[4]}\n")
    solutions_file.write("\n\n")
    solutions_file.write("_____________________________________\n")
    solutions_file.write("_____________________________________\n")
    solutions_file.write(f"Average nodes explored for BFS: {(agent_bfs_results[2] + agent2_bfs_results[2] + agent3_bfs_results[2] + agent4_bfs_results[2] + agent5_bfs_results[2] + agent6_bfs_results[2] + agent7_bfs_results[2] + agent8_bfs_results[2] + agent9_bfs_results[2]) / 9}\n")
    solutions_file.write(f"Average nodes expanded for BFS: {(agent_bfs_results[3] + agent2_bfs_results[3] + agent3_bfs_results[3] + agent4_bfs_results[3] + agent5_bfs_results[3] + agent6_bfs_results[3] + agent7_bfs_results[3] + agent8_bfs_results[3] + agent9_bfs_results[3]) / 9}\n")
    solutions_file.write(f"Average nodes maintained for BFS: {(agent_bfs_results[4] + agent2_bfs_results[4] + agent3_bfs_results[4] + agent4_bfs_results[4] + agent5_bfs_results[4] + agent6_bfs_results[4] + agent7_bfs_results[4] + agent8_bfs_results[4] + agent9_bfs_results[4]) / 9}\n")
    solutions_file.write(f"Average nodes explored for DLS: {(agent_dls_results[2] + agent2_dls_results[2] + agent3_dfs_results[2] + agent4_dfs_results[2] + agent5_dfs_results[2] + agent6_dfs_results[2] + agent7_dfs_results[2] + agent8_dfs_results[2] + agent9_dfs_results[2]) / 9}\n")
    solutions_file.write(f"Average nodes expanded for DLS: {(agent_dls_results[3] + agent2_dfs_results[3] + agent3_dfs_results[3] + agent4_dfs_results[3] + agent5_dfs_results[3] + agent6_dfs_results[3] + agent7_dfs_results[3] + agent8_dfs_results[3] + agent9_dfs_results[3]) / 9}\n")
    solutions_file.write(f"Average nodes maintained for DLS: {(agent_dfs_results[4] + agent2_dfs_results[4] + agent3_dfs_results[4] + agent4_dfs_results[4] + agent5_dfs_results[4] + agent6_dfs_results[4] + agent7_dfs_results[4] + agent8_dfs_results[4] + agent9_dfs_results[4]) / 9}\n")
    solutions_file.write(f"Average nodes explored for BFS: {(agent_bfs_results[2] + agent2_bfs_results[2] + agent3_bfs_results[2] + agent4_bfs_results[2] + agent5_bfs_results[2] + agent6_bfs_results[2] + agent7_bfs_results[2] + agent8_bfs_results[2] + agent9_bfs_results[2]) / 9}\n")
    solutions_file.write(f"Average nodes expanded for BFS: {(agent_bfs_results[3] + agent2_bfs_results[3] + agent3_bfs_results[3] + agent4_bfs_results[3] + agent5_bfs_results[3] + agent6_bfs_results[3] + agent7_bfs_results[3] + agent8_bfs_results[3] + agent9_bfs_results[3]) / 9}\n")
    solutions_file.write(f"Average nodes maintained for BFS: {(agent_bfs_results[4] + agent2_bfs_results[4] + agent3_bfs_results[4] + agent4_bfs_results[4] + agent5_bfs_results[4] + agent6_bfs_results[4] + agent7_bfs_results[4] + agent8_bfs_results[4] + agent9_bfs_results[4]) / 9}\n")
    solutions_file.write(f"Average nodes explored for A*: {(agent_astar_results[2] + agent2_astar_results[2] + agent3_astar_results[2] + agent4_astar_results[2] + agent5_astar_results[2] + agent6_astar_results[2] + agent7_astar_results[2] + agent8_astar_results[2] + agent9_astar_results[2]) / 9}\n")
    solutions_file.write(f"Average nodes expanded for A*: {(agent_astar_results[3] + agent2_astar_results[3] + agent3_astar_results[3] + agent4_astar_results[3] + agent5_astar_results[3] + agent6_astar_results[3] + agent7_astar_results[3] + agent8_astar_results[3] + agent9_astar_results[3]) / 9}\n")
    solutions_file.write(f"Average nodes maintained for A*: {(agent_astar_results[4] + agent2_astar_results[4] + agent3_astar_results[4] + agent4_astar_results[4] + agent5_astar_results[4] + agent6_astar_results[4] + agent7_astar_results[4] + agent8_astar_results[4] + agent9_astar_results[4]) / 9}\n")
    solutions_file.close()

elif len(sys.argv) == 3:
    print("Usage: main.py [FILE_NAME] [START_CITY] [GOAL_CITY] [ALGORITHM]")
    sys.exit()
elif len(sys.argv) == 4:
    file_name = sys.argv[1]
    map, coordinates = parse_file(file_name)
    agent = Agent(sys.argv[2], sys.argv[3], map, coordinates)
    print(agent.run(sys.argv[4]))

#calling parse function
file_name = sys.argv[1]
map, coordinates = parse_file(file_name)


#Agent stuff
start = (list(map.keys()))[1]
goal = (list(map.keys()))[5]
heuristic = 0
bfs = 1
dls = 0
ucs = 0
astar = 0





#Putting stuff in a solution file
