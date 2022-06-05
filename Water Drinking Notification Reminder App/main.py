import plyer
import time

if __name__ == '__main__':
    while True:
        plyer.notification.notify(
            title="Time to Drink water!!",
            message="You should drink about 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon='WaterGlass.ico',
            timeout=12
        )
        time.sleep(60*60)
