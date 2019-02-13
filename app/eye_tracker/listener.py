import tobii_research as tr

a = tr.find_all_eyetrackers()[0]
calib = ScreenBasedCalibrationValidation(eyetracker, sample_count, timeout_ms)
calib.enter_validation_mode()
points_to_collect = [
    Point2(0.1, 0.1),
    Point2(0.1, 0.9),
    Point2(0.5, 0.5),
    Point2(0.9, 0.1),
    Point2(0.9, 0.9)]

for point in points_to_collect:
    # Visualize point on screen
    # ...
    calib.start_collecting_data(point)
    while calib.is_collecting_data:
        time.sleep(0.5)

calibration_result = calib.compute()
calib.leave_validation_mode()


def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))


my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
