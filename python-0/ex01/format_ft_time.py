import time
from datetime import datetime

current_time = time.time()

seconds_since_epoch = f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation"
formatted_date = datetime.now().strftime("%b %d %Y")

print(seconds_since_epoch)
print(formatted_date)