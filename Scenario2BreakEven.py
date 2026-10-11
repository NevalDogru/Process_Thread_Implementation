import time
import threading
import multiprocessing

def check_even_odd(start_index, end_index, results, worker_num):
	# This is a heavy math task for the CPU
	# It calculates even numbers and squares of odd numbers.
	total = 0
	for i in range(start_index, end_index):
		if i % 2 == 0:
			total = total + 1
		else:
			total = total + (i * i)
	# Save the final result in the results list or array
	results[worker_num] = total

def execute_threads(workload):
	# My computer has a 10 core CPU, so I use 10 workers for best performance.
	num_workers = 10
	size = workload // num_workers
	# Create a list of 10 zeros to store results from each thread.
	results = [0] * num_workers
	thread_list = []

	start = time.time()

	for i in range(num_workers):
		start_index = i * size
		end_index = start_index + size

		t = threading.Thread(target=check_even_odd, kwargs={'start_index': start_index, 'end_index': end_index, 'results': results,
				'worker_num': i })
		thread_list.append(t)
		t.start()
	# Wait for all 10 threads to finish their work
	for t in thread_list:
		t.join()

	end_time = time.time()
	total_time = end_time - start
	return total_time

def execute_process(workload):
	# Again, I use 10 workers to match my CPU core count.
	num_workers = 10
	size = workload // num_workers
	# I use multiprocessing.Array to share data between separate processes safely.
	process_results = multiprocessing.Array('d', num_workers)
	process_list = []

	start = time.time()

	for i in range(num_workers):
		start_index = i * size
		end_index = start_index + size

		p = multiprocessing.Process(target=check_even_odd, kwargs={'start_index': start_index, 'end_index': end_index, 'results': process_results,
               'worker_num': i})
		process_list.append(p)
		p.start()
	# Wait for all 10 processes to finish
	for p in process_list:
		p.join()

	end_time = time.time()
	total_time = end_time - start
	return total_time

def main():
	# This is the main part of the experiment to find the break-even point.
	print("\nScenario 2: Finding Break Even Point")
	# I start from 10 million to see the performance change step by step.
	workload = 40000000
	step_size = 10000000
	# This loop runs until Multiprocessing is faster than Threading.
	while True:
		print("\nTesting with Workload Size:", workload)

		t_time = execute_threads(workload)
		p_time = execute_process(workload)

		print("Thread Time:", t_time, "seconds")
		print("Process Time:", p_time, "seconds")
		# If Processes are faster, we found the point and stop the loop.
		if p_time < t_time:

			print("\nFINALLY BREAK EVEN POINT FOUND!")
			print("At workload:", workload, "Multiprocessing became faster.")

			break
		# If Threads are still faster, increase the workload and try again.
		workload = workload + step_size

if __name__ == "__main__":
	main()



