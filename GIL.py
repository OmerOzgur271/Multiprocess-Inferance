from multiprocessing import Process
from time_decorator import report_time

def count(n):
	while n > 0:
		n-=1


@report_time
def run_multiprocessing():
	t1 = Process(target=count, args=(10000000,))
	t2 = Process(target=count, args=(10000000,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

@report_time
def run_sequential():
	count(10000000)
	count(10000000)

_, multiprocess_time = run_multiprocessing()
_, seq_time = run_sequential()

print(f'{multiprocess_time}, {seq_time}')