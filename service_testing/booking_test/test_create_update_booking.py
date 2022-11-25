import json
import parametrize_from_file
import logging

from client.heroku_client.create_booking_client import CreateBookingClient
from utils.response_utils import ResponseUtils

createBookingClient = CreateBookingClient()


@parametrize_from_file(path='../test_data/create_update_booking.yaml')
def test_create_booking(payload, response):
    response_expected, status_code, response_text = createBookingClient.create_booking(json.dumps(payload))
    assert ResponseUtils.assert_response_jsons(response, response_expected, fields_ignored=
    "root['bookingid']")


@parametrize_from_file(path='../test_data/create_update_booking.yaml')
def test_create_update_booking(payload, response,payload_update,response_expected_update, get_token):
    response_create, status_code, _ = createBookingClient.create_booking(json.dumps(payload))
    logging.info(response_create)
    assert ResponseUtils.assert_response_jsons(response, response_create, fields_ignored="root['bookingid']")
    booking_id = response_create['bookingid']
    token = get_token
    response_update, status_code_update, _ = createBookingClient.update_booking(json.dumps(payload_update),
                                                                                booking_id,token)
    assert ResponseUtils.assert_response_jsons(response_expected_update, response_update,
                                               fields_ignored="root['bookingid']")
