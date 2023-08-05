from html_builder import EmptyElement


class Meta(EmptyElement):
    def _getEleKey(self):
        return 'meta'


class MCharset(Meta):
    UTF8 = 'utf-8'

    def __init__(self, charset: str = 'utf-8'):
        self.__charset = charset

    def _getAttrs(self):
        return {
            'charset': self.__charset
        }


class MKeywords(Meta):
    def __init__(self, keywords: list):
        # 列表中放搜索引擎关键词
        self.__keywords = keywords


class MDescription(Meta):
    def __init__(self, description: str):
        # 放网站描述
        self.__description = description

    def _getAttrs(self):
        return {
            'name':'description',
            'content': self.__description
        }

class MAuthor(Meta):
    def __init__(self, name: str):
        self.__name = name


class MAutoRefresh(Meta):
    # <meta http-equiv="refresh" content="30">
    def __init__(self, seconds: int = 30):
        self.__seconds = seconds
