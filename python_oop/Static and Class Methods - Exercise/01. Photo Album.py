from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.__create_matrix()

    def __create_matrix(self):
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.MAX_PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for row_idx in range(len(self.photos)):
            row = self.photos[row_idx]
            if len(row) < PhotoAlbum.MAX_PHOTOS_PER_PAGE:
                self.photos[row_idx].append(label)
                return f"{label} photo added successfully on page {row_idx + 1} slot {len(self.photos[row_idx])}"
        return 'No more free slots'

    def display(self):

        result = "-" * 11
        result += "\n"
        for row in self.photos:
            result += " ".join(["[]" for _ in row]) + "\n"
            result += "-" * 11
            result += "\n"
        return result.strip()
