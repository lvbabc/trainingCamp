import os, time, random
from multiprocessing import Pool

# print(f'Process ({os.getpid()}) start ...')
# pid = os.fork()
# if pid == 0:
#     print(f'I am child process {os.getpid()} and my parent is {os.getppid()}.')
# else:
#     print(f'I {os.getpid()} just created a child process {pid}.')


def long_time_task(name):
    print('Run task {0} {1}'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task {0} runs {1:0.2f} seconds'.format(name, (end - start)))


if __name__ == '__main__':
    print('Parent process {0}'.format(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
