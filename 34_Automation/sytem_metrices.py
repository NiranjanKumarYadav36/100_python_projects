import os.path

import psutil
from datetime import datetime
import pandas

cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage('/')

system_metrics = {
    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'cpu_usage': cpu_usage,
    'memory_total_mb': memory_info.total / (1024 * 1024),
    'meory_used_mb': memory_info.used / (1024 * 1024),
    'disk_usage': disk_info.total / (1024 * 1024),
    'disk_usage': disk_info.used / (1024 * 1024),
}

df = pandas.DataFrame(system_metrics, index=[0])

if os.path.exists('system_metrices.csv'):
    df_existing = pandas.read_csv('system_metrices.csv')
    df_existing = pandas.concat(df_existing, df)
else:
    print(df)
    df.to_csv('system_metrices.csv', header=True, index=False)
