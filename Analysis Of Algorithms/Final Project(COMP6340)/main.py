from PIL import Image
import time
from make_maze import Maze
#from factory import SolverFactory
import os.path
from os import path
from os import system
import sys
Image.MAX_IMAGE_PIXELS = None

# Read command line arguments - the python argparse class is convenient here.
import argparse
def createsolver(type):
        if type == "dijkstra":
            import dijkstra
            return ["Dijkstra's Algorithm", dijkstra.solve]
        elif type == "astar":
            import astar
            return ["A-star Search", astar.solve]
        else:
            import dijkstra
            return ["Dijkstra's Algorithms", dijkstra.solve]

def astar(method,maze):
    # creating the solver for A* Algorithim
    # Create and run solver
    [title, solver] = createsolver(method)
    print ("Starting Solve:", "")

    t0 = time.time()
    [result, stats] = solver(maze)
    t1 = time.time()

    total = t1-t0

    # Print solve stats
    print ("Nodes explored: ", stats[0])
    if (stats[2]):
        print ("Path found, length", stats[1])
    else:
        print ("No Path Found")
    print ("Time elapsed: ", total, "\n")

def dijkstra(method, maze):
    # creating the solver for A* Algorithim
    # Create and run solver
    [title, solver] = createsolver(method)
    print ("Starting Solve:", "")

    t0 = time.time()
    [result, stats] = solver(maze)
    t1 = time.time()

    total = t1-t0

    # Print solve stats
    print ("Nodes explored: ", stats[0])
    if (stats[2]):
        print ("Path found, length", stats[1])
    else:
        print ("No Path Found")
    print ("Time elapsed: ", total, "\n")
    return result


def solve(input_file, output_file):
    # Load Image
    print ("Loading Image")
    im = Image.open(input_file)

    # Create the maze (and time it) - for many mazes this is more time consuming than solving the maze
    print ("Creating Maze")
    t0 = time.time()
    maze = Maze(im)
    t1 = time.time()
    print ("Node Count:", maze.count)
    total = t1-t0
    print ("Time elapsed:", total, "\n")

    print("---------------------------------------------------------------------------------------")
    print("-------------------------------Solving The Maze----------------------------------------\n")
    
    print("*******************************Dijkstra's Algorithm************************************\n")
    result = dijkstra("dijkstra",maze)

    print("--------------------------------A* Algorithm-------------------------------------------\n")    

    astar("astar", maze)
    print("---------------------------------------------------------------------------------------")   
    
    """
    Create and save the output image.
    This is simple drawing code that travels between each node in turn, drawing either
    a horizontal or vertical line as required. Line colour is roughly interpolated between
    blue and red depending on how far down the path this section is.
    """

    print ("Saving Image")
    im = im.convert('RGB')
    impixels = im.load()

    resultpath = [n.Position for n in result]

    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        # Blue - red
        r = int((i / length) * 255)
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Ys equal - horizontal line
            for x in range(min(a[1],b[1]), max(a[1],b[1])):
                impixels[x,a[0]] = px
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0],b[0]), max(a[0],b[0]) + 1):
                impixels[a[1],y] = px

    im.save(output_file)

def createOut(inp):
    prefix ="output_"

    return prefix + inp

def main():
    #print("Choose The Algorithm you want to use. (astar or dijkstra)")
    while True:
        #items = ["astar", "dijkstra"]
       # print("Enter 'exit' to quit program")
       # method = input("Enter Solving Method  :> ")
        #if method =="exit":
        #    sys.exit()
        input_file = input("Enter Maze Input Image File :> ")

        if (os.path.exists(input_file) == True ):
            break
       
        else:
            print(" Error on Inputs")
            system('cls')
    #output_file = input("Enter Maze Output File :> ")

    solve(input_file, createOut(input_file))
    time.sleep(5)
    im = Image.open(createOut(input_file))
    width, height = im.size
    im.show()
if __name__ == "__main__":
    main()