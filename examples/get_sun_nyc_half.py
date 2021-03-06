import matplotlib.pyplot as plt
import datetime
from pytz import timezone
from datetime import timedelta
from shadegpx import shadegpx

filename = 'NYC-Half-2019.gpx'
tz = timezone('US/Eastern')
start_time = datetime.datetime(2018, 3, 17, 7, 30, tzinfo=tz)  # 7:30 AM EST
end_time = start_time + timedelta(hours=2, minutes=30)  # 2.5 hrs of cheering

x, y, avg_color = shadegpx.shade_calc(filename, start_time, end_time)

dx = [0] + (x[1:] - x[:-1]).tolist()
dy = [0] + (y[1:] - y[:-1]).tolist()

sc = plt.scatter(x, y, c=avg_color, s=3, cmap='RdYlBu')
plt.title('Average Shade Factor')
cbar = plt.colorbar(sc)
cbar.ax.set_ylabel('Shade Factor', rotation=270, fontsize=11, labelpad=20)
plt.show()