from unittest import TestCase
from VehicleDispatch_Methods import methods

orderJSON = {
    "orderID":3,
    "ptype":"clothes",
    "dloc":"12709 La Paz Austin, TX",
    "ploc":"9500 S IH 35 Frontage Rd Ste H, Austin",
    "username":"blob2234"
}

badOrderJSON = {
    "orderID":"asdf",
    "ptype":"bubbles",
    "dloc":"akldfjlkajsdflkjas",
    "ploc":"akjsdlkfjhaksdjhfkjahsdfkja",
    "username":"blob2234"
}

dispatchJSON = {
    "origin": "30.229647,-97.755056",
    "dloc": "12709 La Paz, Austin",
    "ploc": "3414 Lyons Rd, Austin"
}

dispatch_conf = {
            'vin': 'BDJF3583GHD',
            'routeBool': 'True'
}

current_ETA = {
    'vin': 'BDJF3583GHD',
    'currETA': '45'
}

total_eta = {
    'vin': 'BDJF3583GHD',
    'compETA': '50'
}

total_distance = {
    'distance': '450'
}

veh_location = {
    'vin': 'BDJF3583GHD',
    'lat': '45.1214',
    'long': '45.2158'
}

class TestMethods(TestCase):

    def test_happy_path_parsePostPath(self):
        self.assertEqual(methods.parsePostPath(
            'https://team12.supply.softwareengineeringii.com/supply/updateV_Complete_Route_Distance'),
            '/supply/updateV_Complete_Route_Distance')

    def test_parsePostPath(self):
        with self.assertRaises(Exception):
            methods.parsePostPath('https://team12.supply.softwareengineeringii.com/supply/request?ptype=veg')

    def test_parsePostPath(self):
        with self.assertRaises(Exception):
            methods.parsePostPath('https://team12.supply.softwareengineeringii.com/supply/dogs?ptype=veg')

    def test_happy_path_parseGetPath(self):
        self.assertEqual(methods.parseGetPath(
            'https://team12.supply.softwareengineeringii.com/supply/testDispatch'),
            '/supply/testDispatch')

    def test_parseGetPath(self):
        with self.assertRaises(Exception):
            methods.parsePostPath('https://team12.supply.softwareengineeringii.com/supply/338fjfvbhfdssf4')

    def test_parseGetPath(self):
        with self.assertRaises(Exception):
            methods.parsePostPath('https://team12.supply.softwareengineeringii.com/supply/testD')

    def test_getOrigin(self):
        self.assertEqual(methods.getOrigin(dispatchJSON), "30.229647,-97.755056")

    def test_happy_path_getOrderID(self):
        self.assertEqual(methods.getOrderID(orderJSON), 3)

    def test_getOrderID(self):
        with self.assertRaises(Exception):
            methods.getOrderID(badOrderJSON)

    def test_happy_path_getPayload(self):
        self.assertEqual(methods.getPayload(orderJSON), "clothes")

    def test_getPayload(self):
        with self.assertRaises(Exception):
            methods.getOrderID(badOrderJSON)

    def test_getDeliveryLocation(self):
        self.assertEqual(methods.getDeliveryLocation(orderJSON), "12709 La Paz Austin, TX")

    def test_getPayloadLocation(self):
        self.assertEqual(methods.getPayloadLocation(orderJSON), "9500 S IH 35 Frontage Rd Ste H, Austin")

    def test_getUsername(self):
        self.assertEqual(methods.getUsername(orderJSON), "blob2234")

    def test_createRoute(self):
        with self.assertRaises(Exception):
            methods.createRoute(badOrderJSON)
