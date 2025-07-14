python getting_started/examples/eval_lerobot.py \
    --robot.type=so101_follower \
    --robot.port=/dev/ttyUSB_follower \
    --robot.id=fjie666_robot \
    --robot.cameras="{ webcam: {type: orbbec, use_depth: True, width: 640, Hi_resolution_mode: False, fps: 30}}" \
    --lang_instruction="Grasp a lego block and put it in the bin."
