from googleapiclient.discovery import build


class GoogleImageApiRepo(object):
    CUSTOM_SEARCH = 'customsearch'
    CUSTOM_SEARCH_VERSION = 'v1'
    IMAGE_SEARCH_TYPE = 'image'

    class ImagesObjectKeys(object):
        ITEMS = 'items'
        LINK = 'link'

    def __init__(self, credentials_descriptor):
        self._cx = credentials_descriptor.cx
        self.service = self.build_service(credentials_descriptor)
        self.__list_dictionaries = dict()

    def build_service(self, credentials_descriptor):
        return build(
            self.CUSTOM_SEARCH,
            self.CUSTOM_SEARCH_VERSION,
            developerKey=credentials_descriptor.developer_key
        )

    def search_images(self, query):
        resp = self.__get_list(query).execute()
        result = []
        for item in resp[self.ImagesObjectKeys.ITEMS]:
            link = item[self.ImagesObjectKeys.LINK]
            if link is not None:
                result.append(link)
        return result

    def __get_list(self, query):
        if query in self.__list_dictionaries:
            return self.__list_dictionaries[query]
        else:
            generated = self.__generate_list_for_query(query)
            self.__list_dictionaries[query] = generated
            return generated

    def __generate_list_for_query(self, query):
        return self.service.cse().list(
            q=query,
            searchType=self.IMAGE_SEARCH_TYPE,
            cx=self._cx
        )
