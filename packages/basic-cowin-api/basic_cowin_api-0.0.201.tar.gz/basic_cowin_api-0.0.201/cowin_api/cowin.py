from datetime import date

from utils.RESTAPI import RestAPI as API
from utils.logit import get_logger


class CoWin(API):
    def __init__(self):
        self.logger = get_logger(__name__)
        cowin_base_url = "https://cdn-api.co-vin.in/api/v2/"
        self.urls = {
            "states":  ("get", f"{cowin_base_url}admin/location/states"),
            "districts":  ("get", f"{cowin_base_url}admin/location/districts/" +
                           "{criteria}"),
            "pincode": ("get", f"{cowin_base_url}" +
                        "appointment/sessions/public/calendarByPin?pincode=" +
                        "{criteria}&date={today}"),
            "district": ("get", f"{cowin_base_url}" +
                         "appointment/sessions/public/calendarByDistrict?district_id=" +
                         "{criteria}&date={today}")
        }

    def call_cowin(self, criteria_type, criteria, filters=None):
        self.logger.debug(f"{criteria_type = }, {criteria = }, {filters = }")
        today = date.today().strftime("%d-%m-%Y")
        flg, result = self.call(self.urls[criteria_type][0],
                                self.urls[criteria_type][1].format(criteria=criteria,
                                                                   today=today))
        self.logger.debug(f"API call result: {flg = }, {result = }")
        if criteria_type in ("pincode", "district"):
            ret_val = result['centers'] if flg else result
        else:
            ret_val = result[criteria_type] if flg else result
        self.logger.debug(f"returning {ret_val = }")
        return ret_val

    # Lets apply filter
    def apply_filter(self, centers, age, payment="any"):
        selected_centers = []
        self.logger.debug(f"Searching for age: {age} - {payment}")
        for center in centers:
            _sessions = []
            self.logger.debug(f"Searching for age: {age} in center: {center['name']}")
            if payment != "any" and payment != center['fee_type'].lower():
                continue

            for session in (center.get('sessions', False)):
                if session['available_capacity'] > 0:
                    if int(session['min_age_limit']) == int(age):
                        self.logger.debug(
                            f"Adding in center {center['name']} session: {session}")
                        _sessions.append(session)
            if _sessions:
                center['sessions'] = _sessions
                selected_centers.append(center)
        return {'centers': selected_centers}

    def check_by_pincode(self, pincode: int, age: int = 45, payment="any"):
        centers = self.call_cowin("pincode", pincode)
        result = self.apply_filter(centers, age, payment)
        return result

    def check_by_district_id(self, district: int, age: int = 45, payment="any"):
        centers = self.call_cowin("district", district)
        result = self.apply_filter(centers, age, payment)
        return result

    def get_state_list(self):
        return self.call_cowin("states", None)

    def get_districts_list(self, state_id):
        return self.call_cowin("districts", state_id)


# # Demo Usage
if __name__ == "__main__":
    cw = CoWin()

    result = cw.check_by_pincode(462003)
    print(result)
    print("*"*20)
    result = cw.check_by_district_id(district=651, age=45, payment="free")
    print(result)
    result = cw.get_state_list()
    print(result)
    result = cw.get_districts_list(2)
    print(result)
