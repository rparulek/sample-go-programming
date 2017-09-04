import threading
import time
import Queue

group_member_counter = 0
group_counter = 0
job_queue = Queue.Queue()
job_lock = threading.Lock()
global_group_list = []

class MyWorkerClass(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        process_job_queue(self.name)

def process_job_queue(thread_name):
    global group_member_counter
    global global_group_list
    while not job_queue.empty():
        job_lock.acquire()

        job = job_queue.get()
        print(thread_name, "acquired job lock and started processing job: ", job, "from job queue")
        global_group_list.append(job)
        group_member_counter += 1
        if group_member_counter == 5:
            print("Created new group of 5 members from queue", global_group_list)
            group_member_counter = 0
            global_group_list = []

        job_lock.release()

        time.sleep(0.5)
        job_queue.task_done()

def main():

    job_process_start_time = time.time()
    for i in range(1,101):
        job_queue.put(i)

    for t in range(1,6):
        thread_name = "thread-" + str(t)
        new_thread = MyWorkerClass(thread_name)
        new_thread.start()

    job_queue.join()

    print("All jobs from job queue have been processed")
    job_process_end_time = time.time()
    processing_time = job_process_end_time - job_process_start_time
    print("Entire job processing completed in", processing_time, "seconds")

if __name__ == "__main__":
    main()
