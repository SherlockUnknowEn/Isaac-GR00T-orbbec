# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from pathlib import Path

from ..configs import CameraConfig, ColorMode, Cv2Rotation

@CameraConfig.register_subclass("orbbec")
@dataclass
class OrbbecCameraConfig(CameraConfig):
    fps: int | None = None
    width: int | None = None
    height: int | None = None
    color_mode: str = "rgb"
    use_depth: bool = True
    mock: bool = False
    index: int = 0
    channels: int = 3
    TemporalFilter_alpha: float = 0.5
    Hi_resolution_mode: bool = False

    def __post_init__(self):
        # bool is stronger than is None, since it works with empty strings

        if self.color_mode not in ["rgb", "bgr"]:
            raise ValueError(
                f"`color_mode` is expected to be 'rgb' or 'bgr', but {self.color_mode} is provided."
            )
        if self.width is None:
            raise ValueError("`height` is expected to be 'None' .")
        if self.use_depth:
            match self.width:
                case 640:
                    self.height = 480 + 400
                case 1280:
                    self.height = 720 + 800
        if not self.use_depth:
            match self.width:
                case 640:
                    self.height = 480
                case 1280:
                    self.height = 720

        at_least_one_is_not_none = self.fps is not None or self.width is not None or self.height is not None
        at_least_one_is_none = self.fps is None or self.width is None or self.height is None
        if at_least_one_is_not_none and at_least_one_is_none:
            raise ValueError(
                "For `fps`, `width` and `height`, either all of them need to be set, or none of them, "
                f"but {self.fps=}, {self.width=}, {self.height=} were provided."
            )
