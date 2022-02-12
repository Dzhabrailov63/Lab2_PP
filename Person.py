
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=str, help='Input path for file')
parser.add_argument("rezult_name", type=str, help='Input name for rezult file')
args = parser.parse_args()
"""
from ReadingFile import ReadingFile

"""
print(args.file_path)
print(args.rezult_name)
"""


class Person:
    telephone: str
    weight: int
    inn: int
    passport_series: int
    occupation: str
    work_experience: int
    political_views: str
    worldview: str
    address: str

    def __init__(self, em, we, sn, pa, un, ag, ac, wo, ad) -> None:
        self.telephone = em
        self.weight = we
        self.inn = sn
        self.passport_series = pa
        self.occupation = un
        self.work_experience = ag
        self.political_views = ac
        self.worldview = wo
        self.address = ad


def collection_instances(path) -> list:
    """Cозданиe коллекции экземпляров класса записи (только вопрос зачем)"""
    read_path = ReadingFile(path)
    data = read_path.get_data()
    # ***
    need_lst = list()
    for pd in data:
        need_lst.append(
            Person(
                pd["telephone"],
                pd["weight"],
                pd["inn"],
                pd["passport_series"],
                pd["occupation"],
                pd["work_experience"],
                pd["political_views"],
                pd["worldview"],
                pd["address"]))
    # ***
    return need_lst
