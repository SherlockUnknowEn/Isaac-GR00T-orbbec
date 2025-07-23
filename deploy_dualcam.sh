python getting_started/examples/eval_lerobot.py \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbmodem5A7A0178061 \
    --robot.id=fjie666_follower_arm \
    --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}, wrist: {type: opencv, index_or_path: 1, width: 640, height: 480, fps: 30} }" \
    --lang_instruction="Grasp a lego block and put it in the bin." \
    --policy_host=192.168.1.175
