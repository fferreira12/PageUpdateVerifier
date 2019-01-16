from file_persistence import FilePersistence


class Config():

    def __init__(self, config_file: str):
        self.config_file = config_file
        # self.persistence = FilePersistence()
        self.config = FilePersistence.ReadJSON(self.config_file)

    def get_config(self, config: str):
        return self.config[config]

    def __getitem__(self, item):
        return self.config[item]
