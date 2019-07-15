# Test functions in city.py
from tubes.tourguide.city import main

def test_main():
	"""
	Let's input a city
	and test we receive a string
	back.
	"""
	assert main(city="Cleveland")
	assert main(city="yz%^") is None
