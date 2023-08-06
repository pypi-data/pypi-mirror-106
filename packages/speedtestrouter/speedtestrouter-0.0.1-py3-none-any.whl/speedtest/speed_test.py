import os

try:
    import speedtest
except ImportError:
    os.system('python -m pip install speedtest-cli')
try:
    import schedule
except ImportError:
    os.system('python -m pip install schedule')
try:
    import argparse
except ImportError:
    os.system('python -m pip install argparse')
try:
    from tqdm import tqdm
except ImportError:
    os.system('python -m pip install tqdm')

import schedule
import argparse
import speedtest
#from getch import pause_exit
from tqdm import tqdm
import time
import logging
from datetime import datetime
from csv import DictWriter

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
root_path = 'C:\Data mining Project\RDOFResults\speedtest'
result_csv = root_path + '\speedtest.csv'

if not os.path.exists(root_path):
    os.makedirs(root_path)
if os.path.exists(result_csv):
    os.remove(result_csv)

field_names = ['SpeedTestTime', 'DownloadSpeed(MB)', 'UploadSpeed(MB)', 'ISP', 'BestHostedServer',
               'HostedServerDistance(KM)',
               'Latency']


def GetArgs():
    parser = argparse.ArgumentParser(description='SpeedTest Runner')
    parser.add_argument('-i', '--interval', type=int, metavar='', required=True,
                        help='Interval in Minutes.')
    parser.add_argument('-t', '--timeout', type=int, metavar='', required=False,
                        help='Timeout in minutes')
    args = parser.parse_args()
    return args


# args = GetArgs()
#timeout = int(input('Enter Speed Test Duration In Seconds:'))
#interval = int(input('Enter Speed Test Frequency In Seconds:'))

timeout = 180
interval = 10

logging.info('Speed Test duration Set : {} Seconds'.format(timeout))
logging.info('Speed Test frequency Set : {} Seconds'.format(interval))


def CreateResultCsv():
    with open(result_csv, 'w', newline='') as csv_obj:
        writer_obj = DictWriter(csv_obj, fieldnames=field_names)
        writer_obj.writeheader()
        csv_obj.close()


def SpeedTestRunner():
    speed_dict = {}
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    res = speedtest.Speedtest()
    logging.info('Running Speed Test...')
    down_speed = res.download()
    res_download_speed = round(down_speed / 1000000, 2)
    up_speed = res.upload()
    res_upload_speed = round(up_speed / 1000000, 2)
    config = res.get_config()
    closest_servers = res.get_best_server()
    speed_dict.update({'SpeedTestTime': str(dt_string), 'DownloadSpeed(MB)': str(res_download_speed),
                       'UploadSpeed(MB)': str(res_upload_speed),
                       'ISP': config['client']['isp'], 'BestHostedServer': closest_servers['name'],
                       'HostedServerDistance(KM)': str(round(closest_servers['d'], 2)),
                       'Latency': str(closest_servers['latency'])})
    logging.info('Speed Run at {} --- {} '.format(str(dt_string), '|'.join(list(speed_dict.values()))))

"""
    with open(result_csv, 'a', newline='') as csv_rows:
        write_rows = DictWriter(csv_rows, fieldnames=field_names)
        write_rows.writerow(speed_dict)
        csv_rows.close()"""


def main():
    CreateResultCsv()
    SpeedTestRunner()
    schedule.every(interval).seconds.do(SpeedTestRunner)
    start = time.time()
    while time.time() - start < timeout:
        schedule.run_pending()
        for i in tqdm(range(0, interval), desc='Waiting For {} Seconds To Start Next Test'.format(interval)):
            time.sleep(1)
    logging.info('Timeout Completed : {} Seconds'.format(timeout))
    logging.info('Results Available At Path: {}'.format(root_path))
    #pause_exit(0, 'Press Any Key To Exit...')


if __name__ == '__main__':
    main()
