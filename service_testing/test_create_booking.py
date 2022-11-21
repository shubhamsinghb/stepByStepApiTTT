import json
import parametrize_from_file
import logging

from client.heroku_client.create_booking_client import CreateBookingClient
from util.response_utils import ResponseUtils

createBookingClient = CreateBookingClient()


@parametrize_from_file(path='test_data/create_booking.yaml')
def test_create_booking(payload,response):
    logging.info("Testing create booking")
    response_expected, status_code, response_text = createBookingClient.create_booking(json.dumps(payload))
    assert ResponseUtils.assert_response_jsons(response, response_expected, fields_ignored=
                                               "root['bookingid']")
