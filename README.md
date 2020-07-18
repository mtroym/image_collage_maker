![Upload Python Package](https://github.com/mtroym/image_collage_maker/workflows/Upload%20Python%20Package/badge.svg?branch=release)![PyPI](https://img.shields.io/pypi/v/collage-maker)

image collage maker
==============================

Installation
------------------------------
```pip install collage-maker```


Descriptions
-------------------------------

Collage is a image combiner to combine lists of arrays.

This is Collage Maker, it makes the collage with borders.

You may want to set the ``border_px``, ``border_bg``, ``direction`` to let it work.

By default, ``border_px=3, border_color=[255, 255, 255, 255]``

Usage:
```python
from collage_maker import make_collage
collage = make_collage(images=[
        [image_a, image_b],
        [image_c, image_d, [image_f, image_g]]
    ],
    direction=0, border_px=1, border_color=[0, 0, 0, 255])
```

.. note:: The border_color is of length 4 because images are length 4.
