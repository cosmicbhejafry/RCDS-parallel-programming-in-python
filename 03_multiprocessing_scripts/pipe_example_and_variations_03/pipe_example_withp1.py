import multiprocessing
import numpy

def calculate_sum(conn):
    # Wait to receive an array from the parent process
    array = conn.recv()
    # Calculate the sum of the array
    result = numpy.sum(array)
    # Send the result back to the parent process
    conn.send(result)

if __name__ == '__main__':
    # Create a Pipe() object
    # This function returns a pair of connection objects connected by a pipe
    # pipes -- symmetric

    # parent_conn here belongs to the main thread and the child is for the spawned process
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create a process and pass the child connection object to it
    # The process will implement the calculate_sum function

    # the args bit is assigning the pipe
    p = multiprocessing.Process(target=calculate_sum, args=(child_conn,))
    
    p1 = multiprocessing.Process(target=calculate_sum, args=(parent_conn,))

    # Start the process
    p.start()
    p1.start()

    # Send an array to the child process
    parent_conn.send(numpy.arange(1, 6))
    # Receive the result from the child process
    print(parent_conn.recv())
    # Wait until the process is finished
    p.join()
    p1.join()
    print('Main process is done')