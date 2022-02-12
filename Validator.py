import re
from tqdm import tqdm
from ReadingFile import ReadingFile


class Validator_elem:
    """Валидатор для элемента списка (словаря)"""
    dict: dict()
    telephone: str
    weight: int
    inn: str
    passport_series: str
    occupation: str
    work_experience: int
    political_views: str
    worldview: str
    address: str

    def __init__(self, dict) -> None:
        """Конструктор класса"""
        self.telephone = dict["telephone"]
        self.weight = dict["weight"]
        self.inn = dict["inn"]
        self.passport_series = dict["passport_series"]
        self.occupation = dict["occupation"]
        self.work_experience = dict["work_experience"]
        self.political_views = dict["political_views"]
        self.worldview = dict["worldview"]
        self.address = dict["address"]

    def check_telephone(self) -> bool:
        """Проверка номера телефона"""
        pattern = r"(\+{1})[7|8](\-{1})(\(){1}[0-9]{3}(\))(\-{1})[0-9]{3}(\-{1})[0-9]{2}(\-{1})[0-9]{2}"
        if re.match(pattern, self.telephone):
            return True
        return False

    def check_weight(self) -> bool:
        """Проверка веса"""
        if isinstance(self.weight, int):
            if 30 <= self.weight < 200:
                return True
        return False

    def check_inn(self) -> bool:
        """Проверка инн"""
        if re.match('[0-9]*$', self.inn):
            return True
        return False

    def check_passport_series(self) -> bool:
        """Проверка паспорта"""
        if re.match('^([0-9]{2}\s{1}[0-9]{2})?$', self.passport_series):
            return True
        return False

    def check_occupation(self) -> bool:
        """Проверка профессии"""
        pattern = "^([а-яА-Я]|-| ){3,}$"
        #pattern = "^[А-Я]{1}[а-я]+$"
        if re.match(pattern, self.occupation):
            return True
        else:
            return False
    def check_work_experience(self) -> bool:
        """Проверка опыта работы"""
        if isinstance(self.work_experience, int):
            if 0 < self.work_experience < 50:
                return True
        return False

    def check_political_views(self) -> bool:
        """Проверка политических взглядов"""
        pattern = "Либеральные|Коммунистические|Социалистические|Анархистские|Умеренные" \
                  "|Либертарианские|Консервативные|Индифферентные|"
        if re.match(pattern, self.political_views):
            return True
        return False

    def check_worldview(self) -> bool:
        """Проверка вероисповедания"""
        pattern = "^.+(?:изм|анство)$"
        if re.match(pattern, self.worldview):
            return True
        return False

    def check_address(self) -> bool:
        """Проверка адреса"""
        pattern = "(?:ул\\.|Аллея) (?:им[\\.\\s]|)[^\\s]+ [^\\s]*(?:\\s|)\\d+"
        if re.match(pattern, self.address):
            return True
        return False


class Validator_collection:
    """Валидатор с коллекцией экземпляров класса записей"""
    data: list

    def __init__(self, collection_ins) -> None:
        """Инициализация списком с экземпляров класса записей"""
        self.data = collection_ins

    def check_dictionary(self, index) -> dict():
        check = False
        if Validator_elem(self.data[index]).check_telephone() and Validator_elem(self.data[index]).check_weight() \
                and Validator_elem(self.data[index]).check_inn() and Validator_elem(self.data[index]).check_passport_series()\
                and Validator_elem(self.data[index]).check_occupation() and Validator_elem(self.data[index]).check_work_experience()\
                and Validator_elem(self.data[index]).check_political_views() and Validator_elem(self.data[index]).check_worldview()\
                and Validator_elem(self.data[index]).check_address():
            check = True
        return check

    def count_valid(self) -> int:
        """Число валидных записей"""
        count_correct = 0
        for i in tqdm(range(len(self.data)),
                      desc="Подсчёт количества валидных записей",
                      ncols=150, colour='green'):
            if self.check_dictionary(i):
                count_correct += 1
        return count_correct

    def count_invalid(self) -> int:
        """Число невалидных записей"""
        count_incorrect = 0
        for i in tqdm(range(len(self.data)),
                      desc="Подсчёт количества невалидных записей",
                      ncols=150, colour='green'):
            if not self.check_dictionary(i):
                count_incorrect += 1
        return count_incorrect

    def count_invalid_general(self) -> dict:
        """Количество некорректных записей отдельно"""
        count_telephone = 0
        count_weight = 0
        count_inn = 0
        count_passport_series = 0
        count_occupation = 0
        count_work_experience = 0
        count_political_views = 0
        count_worldview = 0
        count_address = 0
        for index in tqdm(range(len(self.data)),
                          desc="Подсчёт некорректных записей  данных",
                          ncols=150, colour='green'):
            if not Validator_elem(self.data[index]).check_telephone():
                count_telephone += 1
            if not Validator_elem(self.data[index]).check_weight():
                count_weight += 1
            if not Validator_elem(self.data[index]).check_inn():
                count_inn += 1
            if not Validator_elem(self.data[index]).check_passport_series():
                count_passport_series += 1
            if not Validator_elem(self.data[index]).check_occupation():
                count_occupation += 1
            if not Validator_elem(self.data[index]).check_work_experience():
                count_work_experience += 1
            if not Validator_elem(self.data[index]).check_political_views():
                count_political_views += 1
            if not Validator_elem(self.data[index]).check_worldview():
                count_worldview += 1
            if not Validator_elem(self.data[index]).check_address():
                count_address += 1

        rezult = {"invalid_telephone": count_telephone,
                  "invalid_weight": count_weight,
                  "invalid_inn": count_inn,
                  "invalid_passport_series": count_passport_series,
                  "invalid_occupation": count_occupation,
                  "invalid_work_experience": count_work_experience,
                  "invalid_political_views": count_political_views,
                  "invalid_worldview": count_worldview,
                  "invalid_address": count_address}
        return rezult


"""
read_path = ReadingFile()
data = read_path.get_data()
lst_valid = Validator_collection(data)
print(lst_valid.count_invalid())

#print(Validator_elem(lst_valid.data[0]).check_snils())
#print (lst_valid.check_dictionary(6))
print (lst_valid.count_valid())
print (lst_valid.count_invalid_general())
"""
