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


def process_tanktest_noise(tank_noise: pymongo.cursor.Cursor):
    """
    Round the values in the Tank Test Noise results.  Then check
    if the Tank Test Noise passed or failed for each beam.
    :param tank_noise: Tank Test cursor to the results
    :return: List of all the results from the query.
    """
    # Convert the cursor to a list
    # I can then modify the information
    tanktest_noise_list = list(tank_noise)

    for tank in tanktest_noise_list:

        # Find the minimum amplitude based on the frequency
        min_amp = 119.0
        if "300" in tank['SubsystemDescStr']:
            min_amp = 119.0
        elif "600" in tank['SubsystemDescStr']:
            min_amp = 119.0
        else:
            min_amp = 98.0

        # Beam 0
        # Noise
        tank['noise_b_0'] = round(tank['Beam0NoiseFloor'], 2)
        if tank['Beam0NoiseFloor'] < 40:
            tank['noise_result_b_0'] = "PASS"
        else:
            tank['noise_result_b_0'] = "FAIL"

        # Amplitude
        tank['amp_b_0'] = round(tank['Beam0Signal1mTank'], 2)
        if tank['Beam0Signal1mTank'] > min_amp:
            tank['amp_result_b_0'] = "PASS"
        else:
            tank['amp_result_b_0'] = "FAIL"

        # Beam 1
        # Noise
        tank['noise_b_1'] = round(tank['Beam1NoiseFloor'], 2)
        if tank['Beam1NoiseFloor'] < 40:
            tank['noise_result_b_1'] = "PASS"
        else:
            tank['noise_result_b_1'] = "FAIL"

        # Amplitude
        tank['amp_b_1'] = round(tank['Beam1Signal1mTank'], 2)
        if tank['Beam1Signal1mTank'] > min_amp:
            tank['amp_result_b_1'] = "PASS"
        else:
            tank['amp_result_b_1'] = "FAIL"

        # Beam 2
        # Noise
        tank['noise_b_2'] = round(tank['Beam2NoiseFloor'], 2)
        if tank['Beam2NoiseFloor'] < 40:
            tank['noise_result_b_2'] = "PASS"
        else:
            tank['noise_result_b_2'] = "FAIL"

        # Amplitude
        tank['amp_b_2'] = round(tank['Beam2Signal1mTank'], 2)
        if tank['Beam2Signal1mTank'] > min_amp:
            tank['amp_result_b_2'] = "PASS"
        else:
            tank['amp_result_b_2'] = "FAIL"

        # Beam 3
        # Noise
        tank['noise_b_3'] = round(tank['Beam3NoiseFloor'], 2)
        if tank['Beam3NoiseFloor'] < 40:
            tank['noise_result_b_3'] = "PASS"
        else:
            tank['noise_result_b_3'] = "FAIL"

        # Amplitude
        tank['amp_b_3'] = round(tank['Beam3Signal1mTank'], 2)
        if tank['Beam3Signal1mTank'] > min_amp:
            tank['amp_result_b_3'] = "PASS"
        else:
            tank['amp_result_b_3'] = "FAIL"

    return tanktest_noise_list
