import abc


class OpenglShapeDrawerService(abc.ABC):
    @abc.abstractmethod
    def create_rectangle(self, color, vertices):
        pass

    @abc.abstractmethod
    def get_shape_drawer_scene(self):
        pass

    # @abc.abstractmethod
    # def process_border(self, is_drawer_border):
    #     pass


