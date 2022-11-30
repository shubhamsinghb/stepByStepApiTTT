import time
from datetime import datetime, timedelta
import pytz


class DateTimeUtils:

    # Get current date in format yyyy-mm-dd
    @staticmethod
    def get_current_date():
        return datetime.today().strftime('%Y-%m-%d')

    @staticmethod
    def get_current_date_with_time_zone(timezone='GMT'):
        tz_zone = pytz.timezone(timezone)
        datetime_zone = datetime.now(tz_zone) + timedelta(minutes=29)
        print(datetime_zone.strftime('%Y-%m-%d %H:%M:%S:%fZ'))
        return datetime_zone.strftime("%Y-%m-%dT%H:%M:%S%z")

    @staticmethod
    def get_current_date_with_time_zone_with_microsecs(timezone='GMT'):
        tz_zone = pytz.timezone(timezone)
        datetime_zone = datetime.now(tz_zone) + timedelta(minutes=29)
        return datetime_zone.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+'Z'

    @staticmethod
    def get_current_date_with_time_zone_for_recur(timezone='GMT'):
        tz_zone = pytz.timezone(timezone)
        datetime_zone = datetime.now(tz_zone) + timedelta(minutes=29)
        return datetime_zone.strftime('%Y-%m-%d %H:%M:%S')+'.000Z'


    @staticmethod
    def get_current_epoch_time():
        return int(time.time())

    # Get current date in format yyyy-mm-dd
    @staticmethod
    def get_current_date_only_time_zone(timezone='GMT'):
        tz_zone = pytz.timezone(timezone)
        datetime_zone = datetime.now(tz_zone)
        return datetime_zone.strftime('%Y-%m-%d')

    @staticmethod
    def get_current_time_only_timezone(timezone='GMT'):
        tz_zone = pytz.timezone(timezone)
        datetime_zone = datetime.now(tz_zone)
        return datetime_zone.strftime('%H:%M:%S')


# if __name__ == "__main__":
#
#     print(DateTimeUtils.get_current_date_with_time_zone('GMT'))
#     print(DateTimeUtils.get_current_date_with_time_zone('Asia/Colombo'))