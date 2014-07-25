#!/usr/bin/env python3

def get_coord_offsets(longitude, latitude, distance, units):
	#FIXME: handle units correctly
	return (longitude + 10, longitude - 10, latitude + 10, latitude - 10)
