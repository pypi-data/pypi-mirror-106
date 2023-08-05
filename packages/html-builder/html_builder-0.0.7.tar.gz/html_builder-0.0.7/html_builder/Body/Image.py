from html_builder import Element, EmptyElement, ExistElement


class Image(Element):
    """src is a image source,alt是图片替换文本,is_lazy是表示是否延迟加载"""

    def __init__(self,
                 src: str,
                 alt: str = 'can not load image',
                 is_lazy: bool = True):
        self.__src = src
        self.__alt = alt
        self.__is_lazy = is_lazy
        self.__resps = {}

    

    # TODO: check the resps and return str to _str_
    def respImage(self, media_min_width:int, src:str):
        self.__resps[media_min_width] = src


    

class UnitImage(EmptyElement):
    def __init__(self,
                 src: str,
                 alt: str = 'fail to load image',
                 is_lazy: bool = True):
        self.__src = src
        self.__alt = alt
        self.__is_lazy = is_lazy

        self.__width = None
        self.__height = None

    def _getEleKey(self):
        return 'img'

    def setSize(self, width: int, height: int):
        self.__width = width
        self.__height = height
        return self

    def _getAttrs(self) -> dict:
        rt = {
            'src': self.__src,
            'alt': self.__alt,
        }
        if self.__width is not None and self.__height is not None:
            rt['width'] = self.__width
            rt['height'] = self.__height
        if self.__is_lazy:
            rt['loading'] = 'lazy'
        return rt

class UnitPicture(ExistElement):
    def __init__(self, img:UnitImage):
        self.img = img
        self.__resps = {}

    def respImage(self, media_min_width:int, src:str):
        self.__resps[media_min_width] = src

    def _getEleKey(self):
        return 'picture'

class PictureSource(EmptyElement):
    def __init__(self, media_min_width:int, src:str):
        ...

    def _getEleKey(self):
        return 'source'