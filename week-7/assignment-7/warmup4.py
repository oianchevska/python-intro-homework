# Use the datetime Module
from datetime import datetime

now = datetime.now()
print (f'Today is {now.strftime("%B %d, %Y")}')