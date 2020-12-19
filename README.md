*This repository houses a small portion of a team-based project for my
Software Engineering I course at St. Edward's University.*

*The project's goal was to implement a cloud-based web application that
would allow someone to purchase produce from their home and have it delivered
to them via an autonomous/self-driving vehicle. This repository is for the Supply-Side
Backend Services API, which was in charge of cataloging the locations/destinations of 
vehicles, assigning specific orders to delivery vehicles, dispatching vehicles, 
confirming successful delivery, and storing all related information in the database.
It was the first time I had ever built an API.*

# Supply Backend Services

Everything you need to know to understand the vehicle dispatch process, as is.

## VehicleDispatch_Methods.py

This file contains all methods called by the run.py during the dispatch process, which include:

* parsePostPath(path)
* parseGetPath(path)
* getJSON(post_body)
* getMapJSON(post_body)
* getDistanceJSON(post_body)
* getLocationJSON(post_body)
* getCompETAJSON(post_body)
* getCurrETAJSON(post_body)
* getRouteBoolJSON(post_body)
* getOrderIDJSON(post_body)
* getOrigin(map_json)
* getDistance(distance_json)
* getVIN(location_json)
* getVLat(location_json)
* getVLong(location_json)
* getCompETA(compETA_json)
* getCurrETA(currETA_json)
* getRouteBool(routeBool_json)
* getOrderID(json)
* getPayload(json)
* getDeliveryLocation(json)
* getPayloadLocation(json)
* getUsername(json)
* getRealTimeETA(orderID)
* createRoute(origin, ploc, dloc)
* updateDispatchETA(VIN, compETA)
* updateRealTimeDispatchETA(VIN, currETA)
* updateDispatchStatusComplete(VIN)
* updateDispatchStatusInProgress(VIN)
* updateVehicleStatus(VIN)
* updateVehicleLatLong(VIN, lat, long)
* getRoute()
* executeDispatch(orderID, ptype, dloc, ploc, username)

## parsePostPath(path)
This method simply fetches the path from the URL of the HTTP request and checks if it's an acceptable one that we have hardcoded for potential POST requests.

*Here's a less cluttered version for you.*

```python
path_parse = parse.urlparse(path)
path = path_parse[2]
if path != "/supply/requestv" and path != "/supply/dispatchv":
    raise Exception("Not a valid request path.")
return path
```

## parseGetPath(path)
This method simply fetches the path from the URL of the HTTP request and checks if it's an acceptable one that we have hardcoded for potential GET requests.

*Here's a less cluttered version for you.*

```python
path_parse = parse.urlparse(path)
path = path_parse[2]
if path != "/supply/testDispatch":
    raise Exception("Not a valid request path.")
return path
```

## getOrderJSON(post_body)
This method gets the JSON-formatted info out of the request body, which is passed to the method within **run.py**.

```python
post_dict = json.loads(post_body)
return post_dict
```
To access the data inside the newly-formed object, use this format:

```python
order_id = post_dict.get("orderID")

key_in_object = post_dict.get("keyName")
```

## getMapJSON(post_body)
This method gets the JSON-formatted info related to route creation out of the request body, which is passed to the method within **run.py**.

```python
post_dict = json.loads(post_body)
return post_dict
```
To access the data inside the newly-formed object, use this format:

```python
origin = post_dict.get("origin")

key_in_object = post_dict.get("keyName")
```

## getDistanceJSON(post_body)
This method gets the JSON-formatted info related to vehicle distance reports out of the request body, which is passed to the method within **run.py**.
````python
post_dict = json.loads(post_body)
return post_dict
````

## getLocationJSON(post_body)
This method gets the JSON-formatted info related to vehicle location reports out of the request body, which is passed to the method within **run.py**.
````python
post_dict = json.loads(post_body)
return post_dict
````

## getCompETAJSON(post_body)
This method gets the JSON-formatted info related to vehicle ETA reports out of the request body, which is passed to the method within **run.py**.
````python
post_dict = json.loads(post_body)
return post_dict
````

## getCurrETAJSON(post_body)
This method gets the JSON-formatted info related to vehicle ETA reports out of the request body, which is passed to the method within **run.py**.
````python
post_dict = json.loads(post_body)
return post_dict
````

## getRouteBoolJSON(post_body)
This method gets the JSON-formatted info related to vehicle route completion reports out of the request body, which is passed to the method within **run.py**.
````python
post_dict = json.loads(post_body)
return post_dict
````

## getOrderIDJSON(post_body)
This method gets the JSON-formatted info related to passing back real-time ETA out of the request body, which is passed to the method within **run.py**.
````python
post_dict = json.loads(post_body)
return post_dict
````

## getOrigin(map_json)
This method is one of several that simply exists to retrieve a value from one of the keys in the object created back in **getMapJSON**. In this case, the origin.

```python
origin = map_json.get("origin")
return origin
```

## getDistance(distance_json)
This method is one of several that simply exists to retrieve a value from one of the keys in the object created back in **getDistanceJSON**. In this case, the distance.

```python
distance = distance_json.get("distance")
return distance
```

## getVIN(location_json)
This method is one of several that simply exists to retrieve a value from one of the keys in the object created back in **getLocationJSON**. In this case, the VIN.

```python
VIN = str(location_json.get("vin"))
return VIN
```
## getVLat(location_json)
This method is one of several that simply exists to retrieve a value from one of the keys in the object created back in **getLocationJSON**. In this case, the lat.

```python
lat = location_json.get("lat")
return lat
```

## getVLong(location_json)
This method is one of several that simply exists to retrieve a value from one of the keys in the object created back in **getLocationJSON**. In this case, the long.

```python
long = location_json.get("long")
return long
```

## getCompETA(compETA_json)
This method is one of several that simply exists to retrieve a value from one of the keys in the object created back in **getCompETAJSON**. In this case, the compETA.

```python
compETA = compETA_json.get("compETA")
return compETA
```

## getCurrETA(currETA_json)
This method is one of several that simply exists to retrieve a value from one of the keys in the object created back in **getCurrETAJSON**. In this case, the currETA.

```python
currETA = currETA_json.get("currETA")
return currETA
```

## getRouteBool(routeBool_json)
This method is one of several that simply exists to retrieve a value from one of the keys in the object created back in **getRouteBoolJSON**. In this case, the routeBool.

```python
routeBool = routeBool_json.get("routeBool")
return routeBool
```

## getOrderID(json)
This method is one of five that simply exists to retrieve a value from one of the keys in the object created back in **getJSON**. In this case, the orderID.

```python
orderID = json.get("orderID")
return orderID
```

## getPayload(json)
This method follows the same format as **getOrderID**, but uses "ptype" as the key.
Also does light error checking to make sure the payload type is valid.

```python
ptype = json.get("ptype")
if ptype != "veg" and ptype != "clothes":
    raise Exception("Not a valid parameter for vehicle request.")
return ptype
```

## getDeliveryLocation(json)
This method follows the same format as **getOrderID**, but uses "dloc" as the key.

```python
dloc = json.get("dloc")
return dloc
```

## getPayloadLocation(json)
This method follows the same format as **getOrderID**, but uses "ploc" as the key.

```python
ploc = json.get("ploc")
return ploc
```

## getUsername(json)
This method follows the same format as **getOrderID**, but uses "username" as the key.

```python
username = json.get("username")
return username
```

## getRealTimeETA(orderID)
Method designed to pull a real time ETA from the Dispatch Records database that is attached to an orderID.
````python
# Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='team12',
                                     password='pandapanda',
                                     db='team12_wego',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record for test purposes
                sql = "SELECT `real_time_ETA` FROM `Dispatch_Records` WHERE `orderID`=%s AND `status`=%s"
                cursor.execute(sql, (orderID, 'IN PROGRESS'))
                result = cursor.fetchone()

        finally:
            cursor.close()
            connection.close()
        realTimeETA = result["real_time_ETA"]
        print('Real time ETA: ' + realTimeETA + '\n\n')
        return realTimeETA
````

## createRoute(origin, ploc, dloc)
This method is designed to interact with the Google Maps API to generate a route for the vehicle by sending the origin, ploc, and dloc.

```python
http = 'https://maps.googleapis.com/maps/api/directions/json?'

params = dict(
    origin=origin,
    destination=dloc,
    waypoints=ploc,
    key='AIzaSyAyfjcxAXy8Iq-GlT1ltwGnIomOVc255-I'
)

data = requests.get(url=http, params=params)

if data.status_code == 200:
    binary = data.content
    route = json.loads(binary)
    print(route)
else:
    print('Not a valid request path.\n')
return route
```

## updateDispatchETA(VIN, compETA)
Method designed to update an existing, in-progress dispatch record with the total expected route ETA reported from the Vehicle that matches the VIN passed through by the Vehicle during its route.
````python
print('Inside updateDispatchETA:' + '\n')
        compETA = int(compETA, 10)
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='team12',
                                     password='pandapanda',
                                     db='team12_wego',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record for test purposes
                sql = "UPDATE `Dispatch_Records` SET `ETA`=%s WHERE `VIN`=%s AND `status`=%s"
                cursor.execute(sql, (compETA, VIN, 'IN PROGRESS'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        finally:
            cursor.close()
            connection.close()
````

## updateRealTimeDispatchETA(VIN, currETA)
Method designed to update an existing, in-progress dispatch record with the current real-time route ETA reported from the Vehicle that matches the VIN passed through by the Vehicle during its route.
````python
print('Inside updateRealTimeDispatchETA:' + '\n')
        currETA = int(currETA, 10)
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='team12',
                                     password='pandapanda',
                                     db='team12_wego',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record for test purposes
                sql = "UPDATE `Dispatch_Records` SET `real_time_ETA`=%s WHERE `VIN`=%s AND `status`=%s"
                cursor.execute(sql, (currETA, VIN, 'IN PROGRESS'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        finally:
            cursor.close()
            connection.close()
````

## updateDispatchStatusComplete(VIN)
Method designed to update an existing, in-progress dispatch record with the status "COMPLETE" given the routeBool reported from the Vehicle is "True" and that the record's VIN matches the VIN passed through by the Vehicle during its route.
````python
print('Inside updateDispatchStatusComplete:' + '\n')
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='team12',
                                     password='pandapanda',
                                     db='team12_wego',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record for test purposes
                sql = "UPDATE `Dispatch_Records` SET `status`=%s WHERE `VIN`=%s AND `status`=%s AND `real_time_ETA`=%s"
                cursor.execute(sql, ('COMPLETE', VIN, 'IN PROGRESS', 0))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        finally:
            cursor.close()
            connection.close()
````

## updateDispatchStatusInProgress(VIN)
Method designed to update an existing, in-progress dispatch record with the status "IN PROGRESS" given the record's VIN matches the VIN passed through by the Vehicle during its route.
````python
print('Inside updateDispatchStatusInProgress:' + '\n')
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='team12',
                                     password='pandapanda',
                                     db='team12_wego',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record for test purposes
                sql = "UPDATE `Dispatch_Records` SET `status`=%s WHERE `VIN`=%s AND `status`=%s"
                cursor.execute(sql, ('IN PROGRESS', VIN, 'OPEN'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        finally:
            cursor.close()
            connection.close()
````

## updateVehicleStatus(VIN)
Method designed to update a Vehicle's status to "AVAILABLE" given the record's VIN matches the VIN passed through by the Vehicle during its route.
````python
print('Inside updateVehicleStatus:' + '\n')
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='team12',
                                     password='pandapanda',
                                     db='team12_wego',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record for test purposes
                sql = "UPDATE `Vehicles` SET `status`=%s WHERE `VIN`=%s"
                cursor.execute(sql, ('AVAILABLE', VIN))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            cursor.close()
            connection.close()
````

## updateVehicleLatLong(VIN, lat, long)
Method designed to update a Vehicle's lat,lng columns in the Vehicles table given the vehicle's VIN matches the VIN passed through by the Vehicle during its route.
````python
print('Inside updateVehicleLatLong:' + '\n')
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='team12',
                                     password='pandapanda',
                                     db='team12_wego',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record for test purposes
                sql = "UPDATE `Vehicles` SET `lat`=%s, `lng`=%s WHERE `VIN`=%s"
                cursor.execute(sql, (lat, long, VIN))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

        finally:
            cursor.close()
            connection.close()
````

## getRoute()
This method simply fetches a route that has already been created and placed into an existing and open Dispatch Record, along with it's corresponding VIN.

```python
connection = pymysql.connect(host='localhost',user='team12',password='pandapanda',db='team12_wego',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record for test purposes
        sql = "SELECT * FROM `Dispatch_Records` WHERE `status`=%s"
        cursor.execute(sql, ('OPEN'))
        result = cursor.fetchone()
        VIN = result['VIN']

        #Should convert the dumped JSON to an actual JSON

        route = result['route']
        route = json.loads(route)
        print(result)

finally:
    cursor.close()
    connection.close()
return VIN, route
```


## executeDispatch(orderID, ptype, dloc, ploc, username)
The real star of the show, this method is where all the above elements come into play. Here we select a car from the existing database that is marked AVAILABLE.

```python
try:
            with connection.cursor() as cursor:
                # Find an available vehicle
                sql = "SELECT * FROM `Vehicles` WHERE `status`=%s"
                cursor.execute(sql, ('AVAILABLE'))
                result = cursor.fetchone()
```

Then we get all the attributes of the vehicle (just in case we need them in the future), but we'll only really need the VIN at this stage.

```python
car_VIN = result['VIN']
car_license = result['plateNumber']
car_make = result['make']
car_model = result['model']
car_year = result['year']
car_color = result['color']
car_lat = result['lat']
car_long = result['lng']
car_status = result['status']
```

And then we update the same car as BUSY before closing our connection to the database.

```python
sql = "UPDATE `Vehicles` SET `status`=%s WHERE `vin`=%s"
cursor.execute(sql, ('BUSY', car_VIN))
```

The last big operation is creating the dispatch record, which is really just an INSERT statement.

```python
sql = "INSERT INTO `Dispatch_Records` (`orderID`, `deliveryAddress`, `payloadType`, `payloadAddress`, `userID`, `VIN`, `route`, `status`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
cursor.execute(sql, (orderID, delivery_location, ptype, payload_location, username, car_VIN, route, 'OPEN'))
```
