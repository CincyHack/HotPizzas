#!/usr/bin/env python3


def get_coord_offsets(longitude, latitude, distance, units):
	#FIXME: handle units correctly
	longitude = float(longitude)
	latitude = float(latitude)
	return (longitude + 0.1, longitude - 0.1, latitude + 0.1, latitude - 0.1)


def parse_filter(filter):
	#FIXME: Set max depth here... do this globally
	depth = 5
	#Check if filter is a string, fail if not
	configs = filter.split("-")
	return (configs[0], configs[1:1+depth])


def get_user_gps(request):
	#FIXME: handle situations where the data isn't here more gracefully
	return (request.DATA.get("long", None), request.DATA.get("lat", None))


def est_time(gps1, gps2, old=None, count=0):
	#FIXME: implement a real gps calculation method here
	if not old:
		return 20
	else:
		return 15

