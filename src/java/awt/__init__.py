# Copyright (C) 2018-2020
# Author: Cesar Roman
# Contact: cesar@thecesrom.dev
"""Contains all of the classes for creating user interfaces and for
painting graphics and images.
"""

__all__ = ["Color", "Component", "Container", "Frame", "Image", "Window"]

from java.lang import Object


class Color(Object):
    """The Color class is used to encapsulate colors in the default sRGB
    color space or colors in arbitrary color spaces identified by a
    ColorSpace. Every color has an implicit alpha value of 1.0 or an
    explicit one provided in the constructor. The alpha value defines
    the transparency of a color and can be represented by a float value
    in the range 0.0 - 1.0 or 0 - 255. An alpha value of 1.0 or 255
    means that the color is completely opaque and an alpha value of 0 or
    0.0 means that the color is completely transparent. When
    constructing a Color with an explicit alpha or getting the
    color/alpha components of a Color, the color components are never
    premultiplied by the alpha component.

    The default color space for the Java 2D(tm) API is sRGB, a proposed
    standard RGB color space. For further information on sRGB, see
    http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html.
    """

    def __init__(self, *args):
        """Creates a color.

        Args:
            *args: Variable length argument list.
        """
        print args


class Component(Object):
    """A component is an object having a graphical representation that
    can be displayed on the screen and that can interact with the user.
    """

    pass


class Container(Component):
    """A generic Abstract Window Toolkit(AWT) container object is a
    component that can contain other AWT components.
    """

    def add(self, *args):
        """Adds the specified component.

        Args:
            *args: Variable length argument list.
        """
        print (self, args)


class Window(Container):
    """A Window object is a top-level window with no borders and no
    menubar.
    """

    pass


class Frame(Window):
    """A Frame is a top-level window with a title and a border."""

    pass


class Image(Object):
    """The abstract class Image is the superclass of all classes that
    represent graphical images. The image must be obtained in a
    platform-specific manner.
    """

    pass
