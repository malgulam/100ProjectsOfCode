#this project is modified by an original project authored by:https://github.com/N3ROO
#and modified by: malimba

import psutil
import time
from threading import Thread

#index: number of bytes sent
__BYTES_SENT__ = 0

#index: number of bytes received
__BYTES_RECV__ = 1

#index: number of packets sent
__PACKETS_SENT__ = 2

#index: total numbrt of errors while receiving
__ERR_IN__ = 4

#index: total number of errors while sendig
__ERR_OUT__ = 5

#index: total number of incoming packets which were dropped
__DROP_IN__ = 5

#index: total number of outgoing packets which were dropped
__DROP_OUT__ = 7

class Tracker:

    def __init__(self):
        self.__reset_bytes_recv_vars__()
        self.__reset_bytes_sent_vars__()
        self.init_total_sent = self.__get_bytes_sent_total__()
        self.init_total_recv = self.__get_bytes_recv_total__()


    def get_total_data_used(self):
        """ Returns the data used since the start 4G/3G ...
        """
        return ((self.__get_bytes_sent_total__() - self.init_total_sent) +
                (self.__get_bytes_recv_total__() - self.init_total_recv))


    def get_current_upload_speed(self):
        """ Returns the current upload speed in bytes per seconds.
        """
        dtime = time.time() - self.last_bytes_sent_time
        dsent = self.__get_bytes_sent_total__() - self.last_bytes_sent_total
        self.__reset_bytes_sent_vars__()
        return dsent / dtime if dtime != 0 else 0


    def get_current_download_speed(self):
        """ Returns the current downlaod speed in bytes per seconds.
        """
        dtime = time.time() - self.last_bytes_recv_time
        dsent = self.__get_bytes_recv_total__() - self.last_bytes_recv_total
        self.__reset_bytes_recv_vars__()
        return dsent / dtime if dtime != 0 else 0


    def __reset_bytes_sent_vars__(self):
        self.last_bytes_sent_total = self.__get_bytes_sent_total__()
        self.last_bytes_sent_time = time.time()


    def __reset_bytes_recv_vars__(self):
        self.last_bytes_recv_total = self.__get_bytes_recv_total__()
        self.last_bytes_recv_time = time.time()


    def __get_bytes_sent_total__(self):
        return psutil.net_io_counters(pernic=False)[__BYTES_SENT__]


    def __get_bytes_recv_total__(self):
        return psutil.net_io_counters(pernic=False)[__BYTES_RECV__]
