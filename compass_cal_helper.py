import pymongo


def process_compass_cal(compass_cals: pymongo.cursor.Cursor):
    """
    Round the values in the compass calibration results.  Then check
    if the compass calibration passed or failed for each direction.
    :param compass_cals: Compass Cal cursor to the results
    :return: List of all the results from the query.
    """
    # Convert the cursor to a list
    # I can then modify the information
    compass_cal_list = list(compass_cals)

    for compass in compass_cal_list:
        # Beam 0
        compass['post_rnd_b0'] = round(compass['Point1_Post_Hdg'], 1)
        if compass['Point1_Post_Hdg'] > 300:
            compass['result_rnd_b0'] = round(360 - compass['Point1_Post_Hdg'], 2)
        else:
            compass['result_rnd_b0'] = round(0 - compass['Point1_Post_Hdg'], 2)

        # Check if Beam 0 Passed
        if(abs(compass['result_rnd_b0']) < 2.0):
            compass['result_b0'] = "PASS"
        else:
            compass['result_b0'] = "FAIL"

        # Beam 1
        compass['post_rnd_b1'] = round(compass['Point2_Post_Hdg'], 1)
        compass['result_rnd_b1'] = round(90 - compass['Point2_Post_Hdg'], 2)

        # Check if Beam 1 Passed
        if (abs(compass['result_rnd_b1']) < 2.0):
            compass['result_b1'] = "PASS"
        else:
            compass['result_b1'] = "FAIL"

        # Beam 2
        compass['post_rnd_b2'] = round(compass['Point3_Post_Hdg'], 1)
        compass['result_rnd_b2'] = round(180 - compass['Point3_Post_Hdg'], 2)

        # Check if Beam 2 Passed
        if (abs(compass['result_rnd_b2']) < 2.0):
            compass['result_b2'] = "PASS"
        else:
            compass['result_b2'] = "FAIL"

        # Beam 3
        compass['post_rnd_b3'] = round(compass['Point4_Post_Hdg'], 1)
        compass['result_rnd_b3'] = round(270 - compass['Point4_Post_Hdg'], 2)

        # Check if Beam 3 Passed
        if (abs(compass['result_rnd_b3']) < 2.0):
            compass['result_b3'] = "PASS"
        else:
            compass['result_b3'] = "FAIL"

    return compass_cal_list