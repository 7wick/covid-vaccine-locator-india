from rest_framework import status
from rest_framework.response import Response
import requests
import os
import json


def get_centres(date, age, state_name, district_name):
    state_id = get_state_id(state_name)
    district_id = get_district_id(state_id, district_name)
    try:
        response = requests.get(
            "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict",
            params={
                'district_id': district_id,
                'date': date
            },
            headers={"User-Agent": "Chrome"}
        )
        total_available_centres = 0
        centre_list = list()
        for centre in response.json()["centers"]:
            for details in centre["sessions"]:
                result = dict()
                if details['available_capacity'] > 0 and details["min_age_limit"] <= age:
                    total_available_centres += 1
                    result["name"] = centre["name"]
                    result["block_name"] = centre["block_name"]
                    result["pincode"] = centre["pincode"]
                    result["min_age_limit"] = details["min_age_limit"]
                    result["date"] = details["date"]
                    result["available_capacity"] = details["available_capacity"]
                    centre_list.append(result)

        if total_available_centres > 0:
            final_response = dict()
            final_response['Total available centres'] = total_available_centres
            final_response['Centres'] = centre_list
        else:
            final_response = {'message': 'No vaccines available in this district, for the given age, for the next 7 days.'}
        return final_response
    except Exception:
        return Response(data={'message': 'Unexpected Error. Kindly retry a couple of times!'},
                        status=status.HTTP_400_BAD_REQUEST)


def get_state_id(state_name):
    try:
        unchanged_states = ["Andaman and Nicobar Islands", "Dadra and Nagar Haveli", "Daman and Diu",
                            "Jammu and Kashmir"]
        if state_name not in unchanged_states:
            state_name = state_name.title()
        response = requests.get(
            "https://cdn-api.co-vin.in/api/v2/admin/location/states",
            headers={"User-Agent": "Chrome"}
        )
        states = response.json()['states']
        state_id = next(item for item in states if item["state_name"] == state_name)['state_id']
        return state_id
    except Exception:
        return Response(data={'message': 'Invalid state_name. Enter it correctly!'},
                        status=status.HTTP_400_BAD_REQUEST)


def get_district_id(state_id, district_name):
    try:
        district_url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{0}".format(str(state_id))
        response = requests.get(district_url, headers={"User-Agent": "Chrome"})
        districts = response.json()['districts']
        district_id = next(item for item in districts if item["district_name"] == district_name.capitalize())[
            'district_id']
        return district_id
    except Exception:
        return Response(data={'message': 'Invalid district_name. Enter it correctly!'},
                        status=status.HTTP_400_BAD_REQUEST)
