import psutil
import time
import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

app = r'C:\Users\Sandramohan\AppData\Local\Programs\Python\Python38\python.exe'

nManager = notifications.ToastNotificationManager
notifier = nManager.create_toast_notifier(app)
heading1 = ' Battery full disconnect the charger'
heading2 = 'Baterry low please connect the charger'

tString = """
<toast duration ="short">
    <visual>
        <binding template='ToastGeneric'>
            <text>{heading}</text>
            <text>{text}</text>
            <image placement="appLogoOverride" HintCrop="circle" src="C:/Users/Sandramohan/OneDrive/Desktop/Code/battery/{img}.ico"/>
        </binding>
    </visual>
    <action activationType="system" arguments="snooze" hint-inputId="snoozeTime" content="" />
 
    <action activationType="system" arguments="dismiss" content=""/>
</toast>
"""

xDoc = dom.XmlDocument()

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    psutil.sensors_battery().power_plugged
    text = f'battery percentage is now {percent}'
    if percent <50 and not psutil.sensors_battery().power_plugged:
        
        xDoc.load_xml(tString.format(heading=heading2,text=text,img='low'))

        notification = notifications.ToastNotification(xDoc)

        #display notification
        notifier.show(notification)
        
        time.sleep(60*2)


    elif percent> 98 and psutil.sensors_battery().power_plugged:
        
        xDoc.load_xml(tString.format(heading=heading1,text=text,img='full'))

        notification = notifications.ToastNotification(xDoc)

        #display notification
        notifier.show(notification)
        time.sleep(60*2)
        

    else:
        time.sleep(60*2)



from gi.repository import Notify,GdkPixbuf
from time import sleep, time

import psutil
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
print(plugged)
percent = float(percent)
print(percent)
while True:
    battery= psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    percent = float(percent)

    if percent<50 and not plugged:
        Notify.init("Battery")
        notification = Notify.Notification.new("Battery low")

        # Use GdkPixbuf to create the proper image type
        image = GdkPixbuf.Pixbuf.new_from_file("low.ico")

        # Use the GdkPixbuf image
        notification.set_icon_from_pixbuf(image)
        notification.set_image_from_pixbuf(image)

        notification.show()
        sleep(60*2)

    elif percent>98 and plugged:
        print()
        Notify.init('Battery')
        notification =Notify.Notification.new('Battery is almost full')

        # Use GdkPixbuf to create the proper image type
        image = GdkPixbuf.Pixbuf.new_from_file("full.ico")

        # Use the GdkPixbuf image
        notification.set_icon_from_pixbuf(image)
        notification.set_image_from_pixbuf(image)

        # notification.show()
        sleep(60*5)
    
    else:
        sleep(60*5)
