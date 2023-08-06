"""
Module defining the VGG external format.
"""
from typing import Tuple

from wai.annotations.domain.image import Image
from ..configuration import Image as JSONImage

# Image data, VGG Image JSON format
VGGExternalFormat = Tuple[Image, JSONImage]
