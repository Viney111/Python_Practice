'''
    @Author: Viney Khaneja
    @Date: 2022-04-12 11:50AM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : StopWatch Simulation
'''
import time

def stopwatch_simulation():
    '''
               Description: Calculating elapsing time & printing it
               Parameter: none
               Return: None, Just prints elapsed time.
           '''
    # Starting the timer
    input("Press ENTER to start the timer")
    start_time = time.time()

    # Stopping the timer
    input("Press ENTER to stop the timer")
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time is {elapsed_time}")

if __name__ == '__main__':
    stopwatch_simulation()

