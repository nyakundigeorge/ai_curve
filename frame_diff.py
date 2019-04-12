import cv2
# compute frame diffrences


def frame_diff(prev_frame, cur_frame, next_frame):
    # diffrence between the current frame and the next frame
    diff_frame_1 = cv2.absdiff(next_frame, cur_frame)
    # diffrence between the current frame and the previous frame
    diff_frame_2 = cv2.absdiff(cur_frame, prev_frame)

    return cv2.bitwise_and(diff_frame_1, diff_frame_2)


# define function to get the current frame from the webcam
def get_frame(cap, scaling_factor):
    # read teh current frame from the video capture object
    _, frame = cap.read()
    # resize the image
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    return gray


if __name__ == "__main__":
    # define the video capture object
    cap = cv2.VideoCapture(0)

    # define the scaling factor for the images
    scaling_factor = 0.5

    # grab the current frame
    prev_frame = get_frame(cap, scaling_factor)
    # grab the next frame
    cur_frame = get_frame(cap, scaling_factor)
    # grab the frame after
    next_frame = get_frame(cap, scaling_factor)

    # keep reading the frame from the webcam
    # until the user presses the ESC key

    while True:
        # display the frame differences
        cv2.imshow('Object Movement', frame_diff(
            prev_frame, cur_frame, next_frame))
        # update the variables
        prev_frame = cur_frame
        cur_frame = next_frame

        # grab the next frame
        next_frame = get_frame(cap, scaling_factor)

        # check if the user hit the ESC Key
        key = cv2.waitKey(10)
        if key == 27:
            break
    # close all windows

    cv2.destroyAllWindows()
