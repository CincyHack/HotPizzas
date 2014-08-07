#!/usr/bin/env python3

def get_coord_offsets(longitude, latitude, distance, units):
	#FIXME: handle units correctly
	return (longitude + 0.1, longitude - 0.1, latitude + 0.1, latitude - 0.1)
