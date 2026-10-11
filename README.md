# Process vs. Thread Implementation: Evaluating Performance Bottlenecks

This repository contains a performance analysis of concurrent programming in Python, specifically comparing multi-threading and multi-processing approaches. The project evaluates how the Global Interpreter Lock (GIL) in CPython affects execution times across I/O-bound and CPU-bound scenarios.

## 📂 Repository Structure

* **`Scenario1IOSimulation.py`**: Implementation of I/O-bound tasks to observe the efficiency of multi-threading during frequent CPU waits.
* **`Scenario2BreakEven.py`**: Implementation of CPU-bound workloads to identify the "Efficiency Cross-over" point where the true parallelism of processes overcomes GIL limitations and process management overhead.
* **`Process_Thread_Implementation.pdf`**: The comprehensive academic report detailing the theoretical background, methodology, address space isolation concepts, and final performance benchmarks.

## 🚀 Technologies
* Python 3.x
* `threading` module
* `multiprocessing` module

## ⚙️ How to Run
You can run the simulation scripts directly from your terminal:

```bash
python Scenario1IOSimulation.py
python Scenario2BreakEven.py
