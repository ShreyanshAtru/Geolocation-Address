from statistics import median
from django.http import HttpResponse
import requests, json, os
import xml.etree.ElementTree as ET
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv

load_dotenv()


class LocationService:
    def get_lat_long(line1: str, output_type: str):
        """
        It takes a string as input, splits it into a list of words, joins the list with a "+" sign, and
        then makes a request to the Google Maps API
        :param line1: The address you want to get the latitude and longitude for
        :type line1: str
        :param output_type: str
        :type output_type: str
        :return: a response object.
        """
        address = line1.split(" ")
        
        # add your key here 
        API_KEY = ''   
        url_address = "+".join(address)
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(
            url_address, API_KEY)

        response = requests.get(url)
        location = json.loads(response.text)
        lat_lng = location["results"][0].get("geometry").get("location")
        if output_type is "json":
            return Response({"coordinates": lat_lng, "address": line1})
        else:
            return LocationService.xml_response(
                line1=line1, lat=lat_lng["lat"], long=lat_lng["lng"]
            )

    def xml_response(line1: str, lat: int, long: int):
        """
        It creates an XML response.
        :param line1: The first line of the address
        :type line1: str
        :param lat: latitude
        :type lat: int
        :param long: longitude
        :type long: int
        :return: an HttpResponse object.
        """
        root = ET.Element("root")
        address = ET.SubElement(root, "address")
        address.text = line1
        coordinates = ET.SubElement(root, "coordinates")
        latitude = ET.SubElement(coordinates, "lat")
        latitude.text = str(lat)
        longitude = ET.SubElement(coordinates, "lng")
        longitude.text = str(long)
        response = HttpResponse(ET.tostring(root))
        response["content_type"] = "application/xml; charset=utf-8"
        return response
