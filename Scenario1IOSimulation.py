import time
import threading
import multiprocessing


def execute_sequential():
	sequential_counter = 0
	start_time = time.time()
	# Do the waiting task 50 times, one by one. It is very slow.
	for i in range(50):
		time.sleep(0.1) # Simulate I/O delay
		sequential_counter = sequential_counter + 1

	end_time = time.time()

	total_time = end_time - start_time

	print("Sequential Execution -> Counter: ", sequential_counter, " / Time:", total_time, " seconds")

def thread_task(thread_lock, thread_counter_list):
	for i in range(10):
		time.sleep(0.1) # Wait for a short time

		# I use with here. It opens and closes the lock automatically.
		# This is very safe and prevents deadlock problems.
		with thread_lock:
			thread_counter_list[0] = thread_counter_list[0] + 1

def execute_thread():
	# I use a list [0] because it is easy to share between threads
	thread_counter= [0]
	thread_lock = threading.Lock()
	threads = []

	start_time = time.time()

	for i in range(5): # Create 5 threads
		# I use 'kwargs' to match the variable names easily. It makes my code clean.
		t = threading.Thread(target=thread_task, kwargs={"thread_lock": thread_lock, "thread_counter_list": thread_counter})
		threads.append(t)
		t.start()

	for t in threads: # Wait for all threads to finish their jobs
		t.join()

	end_time = time.time()
	total_time = end_time - start_time

	print("Thread Execution -> Counter: ", thread_counter[0], "/  Time:", total_time, "seconds")

def process_task(process_lock, process_counter):
	for i in range(10):
		time.sleep(0.1) # Wait for a short time
		# Again, I use with to lock safely.
		with process_lock:
			process_counter.value = process_counter.value + 1

def execute_process():
	# I use multiprocessing.Value to share a number between different processes safely
	process_counter_val = multiprocessing.Value('i', 0)
	process_lock = multiprocessing.Lock()
	processes = []

	start_time = time.time()
	# Create 5 processes
	for i in range(5):
		# Using kwargs stops me from making order mistakes
		p = multiprocessing.Process(target=process_task, kwargs = {'process_lock': process_lock, 'process_counter': process_counter_val}
)
		processes.append(p)
		p.start()
	# Wait for all processes to finish
	for p in processes:
		p.join()

	end_time = time.time()
	total_time = end_time - start_time


	print("Process Execution -> Counter: ", process_counter_val.value, "/  Time:", total_time, "seconds")


# This is the main part. I test and compare all three methods here.
def main():
	print("\nStarting I/O Simulation -> 50 TASKS")

	execute_sequential()
	execute_thread()
	execute_process()

	print("DONE")


# This line checks if we run the file directly.
# If yes, it starts the main function.
if __name__ == '__main__':
	main()





