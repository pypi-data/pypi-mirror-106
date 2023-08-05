import datetime
import pandas as pd
from .setup_url import req_url

class FetchData:
    def get_states_dict(self):
        res = {}
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        state_name = req_url(url)
        for name in state_name['states']:
            res.update({name['state_id']:name['state_name']})
        return res

    def get_states_list(self):
        res = {}
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        state_name = req_url(url)
        for name in state_name['states']:
            res.update({name['state_id']:name['state_name']})
        ans = list(res.values())
        return ans

    def get_states_table(self):
        res = {}
        url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        state_name = req_url(url)
        for name in state_name['states']:
            res.update({name['state_id']:name['state_name']})
        df = pd.DataFrame(list(zip(list(res.keys()), list(res.values()))), columns = ['State Id', 'State Name'])
        return df

    def get_districts_dict(self):
        res = {}
        for state_code in range(1,40):
            url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code)
            district_name = req_url(url)
            for name in district_name["districts"]:
                res.update({name['district_id']:name['district_name']})
        return res

    def get_districts_list(self):
        res = {}
        for state_code in range(1,40):
            url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code)
            district_name = req_url(url)
            for name in district_name["districts"]:
                res.update({name['district_id']:name['district_name']})
        ans = list(res.values())
        return ans

    def get_districts_tables(self):
        pd.options.display.max_columns = None
        data = {}
        res = []
        for state_code in range(1,40):
            url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code)
            district_name = req_url(url)
            for name in district_name["districts"]:
                data.update({name['district_id']:name['district_name']})
                res.append(state_code)
        df = pd.DataFrame(list(zip(list(data.keys()), res,list(data.values()))), columns = ['District Id', 'State Code', 'District Name'])
        df.sort_values('District Id', ignore_index = True, inplace = True)
        return df

        
    def get_centers_by_districtId(self,district_id,numdays=7):
        df = pd.DataFrame(columns = ['date', 'center_id', 'name', 'address',
                                'state_name', 'district_name', 'block_name', 'pincode',
                                    'from1', 'to', 'fee_type', 'available_capacity', 'min_age_limit', 'vaccine', 'slots'])
        
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        for INP_DATE in date_str:
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id, INP_DATE)
            json_data = req_url(url)
            if type(json_data)==dict:
                if json_data["centers"]:
                    for center in json_data["centers"]:
                        date = center['sessions'][0]['date']
                        center_id = center['center_id']
                        name = center['name']
                        address = center['address']
                        state_name = center['state_name']
                        district_name = center['district_name']
                        block_name = center['block_name']
                        pincode = center['pincode']
                        from1 = center['from']
                        to = center['to']
                        fee_type = center['fee_type']
                        available_capacity = center['sessions'][0]['available_capacity']
                        min_age_limit = center['sessions'][0]['min_age_limit']
                        vaccine = center['sessions'][0]['vaccine']
                        slots = center['sessions'][0]['slots']
                        df.loc[len(df)] = [date, center_id, name, address,state_name, district_name, block_name, pincode,
                                        from1, to, fee_type, available_capacity, min_age_limit, vaccine, slots]
                else:
                    date = INP_DATE
                    center_id = 'NA'
                    name = 'NA'
                    address = 'NA'
                    state_name = 'NA'
                    district_name = 'NA'
                    block_name = 'NA'
                    pincode = 'NA'
                    from1 = 'NA'
                    to = 'NA'
                    fee_type = 'NA'
                    available_capacity = 'NA'
                    min_age_limit = 'NA'
                    vaccine = 'NA'
                    slots = 'NA'
                    df.loc[len(df)] = [date, center_id, name, address,
                                        state_name, district_name, block_name, pincode,
                                        from1, to, fee_type, available_capacity, min_age_limit, vaccine, slots]
        
        return df

    def get_centers_By_PinCode(self,POST_CODE, numdays=7):
        POST_CODE = str(POST_CODE)
        df = pd.DataFrame(columns = ['date', 'center_id', 'name', 'address',
                                'state_name', 'district_name', 'block_name', 'pincode',
                                    'from1', 'to', 'fee_type', 'available_capacity', 'min_age_limit', 'vaccine', 'slots'])
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        for INP_DATE in date_str:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
            json_data = req_url(URL)
            if type(json_data)==dict:
                if json_data["centers"]:
                    for center in json_data["centers"]:
                        date = center['sessions'][0]['date']
                        center_id = center['center_id']
                        name = center['name']
                        address = center['address']
                        state_name = center['state_name']
                        district_name = center['district_name']
                        block_name = center['block_name']
                        pincode = center['pincode']
                        from1 = center['from']
                        to = center['to']
                        fee_type = center['fee_type']
                        available_capacity = center['sessions'][0]['available_capacity']
                        min_age_limit = center['sessions'][0]['min_age_limit']
                        vaccine = center['sessions'][0]['vaccine']
                        slots = center['sessions'][0]['slots']
                        df.loc[len(df)] = [date, center_id, name, address,state_name, district_name, block_name, pincode,
                                        from1, to, fee_type, available_capacity, min_age_limit, vaccine, slots]
                else:
                    date = INP_DATE
                    center_id = 'NA'
                    name = 'NA'
                    address = 'NA'
                    state_name = 'NA'
                    district_name = 'NA'
                    block_name = 'NA'
                    pincode = 'NA'
                    from1 = 'NA'
                    to = 'NA'
                    fee_type = 'NA'
                    available_capacity = 'NA'
                    min_age_limit = 'NA'
                    vaccine = 'NA'
                    slots = 'NA'
                    df.loc[len(df)] = [date, center_id, name, address,
                                        state_name, district_name, block_name, pincode,
                                        from1, to, fee_type, available_capacity, min_age_limit, vaccine, slots]
        return df

    def get_availability_by_pincode(self,POST_CODE,numdays = 7):        
        POST_CODE = str(POST_CODE)
        df = pd.DataFrame(columns = ['date', 'name', 'address', 'fee_type','available_capacity', 'min_age_limit','vaccine'])
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        for INP_DATE in date_str:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
            json_data = req_url(URL)
            if type(json_data)==dict:
                if json_data["centers"]:
                    for center in json_data["centers"]:
                        date = center['sessions'][0]['date']
                        name = center['name']
                        address = center['address']
                        fee_type = center['fee_type']
                        available_capacity = center['sessions'][0]['available_capacity']
                        min_age_limit = center['sessions'][0]['min_age_limit']
                        vaccine = center['sessions'][0]['vaccine']
                        print(address)
                        df.loc[len(df)] = [date,name, address,fee_type, available_capacity, min_age_limit, vaccine]
                else:
                    date = INP_DATE
                    name = 'NA'
                    address = 'NA'
                    fee_type = 'NA'
                    available_capacity = 'NA'
                    min_age_limit = 'NA'
                    vaccine = 'NA'
                    df.loc[len(df)] = [date,name, address,fee_type, available_capacity, min_age_limit, vaccine]
        return df
