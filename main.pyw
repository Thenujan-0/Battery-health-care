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

def main():
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
        main()
        

    elif percent> 98 and psutil.sensors_battery().power_plugged:
        
        xDoc.load_xml(tString.format(heading=heading1,text=text,img='full'))

        notification = notifications.ToastNotification(xDoc)

        #display notification
        notifier.show(notification)
        time.sleep(60*2)
        main()

    else:
        time.sleep(60*2)
        main()

main()
