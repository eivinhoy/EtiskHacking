from multiprocessing import Process
import threading
import time
import urllib.request
import urllib

class Post:

    def __init__(self, website, mode):
        self.website = website

        #mode is either:
        #   "Simple"      (Simple POST)
        #   "Multiple"    (Multi-thread POST)
        #   "Process"     (Multiprocessing)
        self.mode = mode
        self.run_job()

    def post(self):

        #post data
        #req = urllib.request.Request(self.website)
        #response = urllib.request.urlopen(req)
        #if len(response.read()):
            #print("[{0}] =>  {1}".format(response.code, self.website))
        time.sleep(1.0)
        if self.mode == "Multiple":
            time.sleep(0.000001)

    def run_job(self):
        origin_time = time.time()
        if(self.mode == "Process"):

            #multiprocessing POST
            processes = list()
            for i in range(5):
               process = Process(target = self.post)
               process.start()
               processes.append(process)
            for process in processes:
               process.join()
            #calculate the time interval
            time_interval = time.time() - origin_time
            print("mode - {0}: {1}".format(method, time_interval))

        if(self.mode == "Multiple"):

            #multithreading POST
            threads = list()
            for i in range(5):
               thread = threading.Thread(target = self.post)
               thread.start()
               threads.append(thread)
            for thread in threads:
               thread.join()
            #calculate the time interval
            time_interval = time.time() - origin_time
            print("mode - {0}: {1}".format(method, time_interval))
        
        if(self.mode == "Simple"):

            #simple POST
            for i in range(5):
                self.post()
            #calculate the time interval
            time_interval = time.time() - origin_time
            print("mode - {0}: {1}".format(method, time_interval))
        return time_interval

if __name__ == "__main__":
    target_url = "http://testphp.vulnweb.com"
    for method in ["Process", "Multiple", "Simple"]:
        Post(target_url, 
            method
            )
