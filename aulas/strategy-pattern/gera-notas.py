# import pyyaml module
from abc import ABC, abstractmethod
import sys
import logging

logging.basicConfig(level=logging.INFO)


class Parser(ABC):
    def __init__(self, filetype):
        self.path = f"./notas.{filetype}"

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def load(self):
        pass


class CSVParser(Parser):
    def extract(self):
        import csv

        data = {"alunos": []}

        # Abrir o arquivo CSV para leitura
        try:
            with open(self.path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    nome = row["Nome"]
                    media = float(row["Media"])
                    notas = [float(nota) for nota in row["Notas"].split(", ")]

                    # Construir um dicionário com os dados do aluno
                    aluno = {"nome": nome, "notas": notas, "media": media}

                    # Adicionar o aluno à estrutura de dados
                    data["alunos"].append(aluno)
            return data
        except Exception as e:
            return f"Error parsing CSV file: {str(e)}"

    def load(self, data):
        import csv

        try:
            with open(self.path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Nome", "Media", "Notas"])
                for aluno in data["alunos"]:
                    nome = aluno["nome"]
                    media = aluno["media"]
                    notas = aluno["notas"]
                    writer.writerow([nome, media, ", ".join(map(str, notas))])
            return "Writen to file successfully"
        except Exception as e:
            return f"Error writing CSV file: {str(e)}"


class YMLParser(Parser):
    def extract(self):
        import yaml
        from yaml.loader import SafeLoader

        try:
            with open(self.path) as f:
                return yaml.load(f, Loader=SafeLoader)
        except Exception as e:
            return f"Error parsing YAML file: {str(e)}"

    def load(self, data):
        import yaml

        yaml_output = yaml.dump(data, sort_keys=False)

        try:
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                f.write(yaml_output)
            return "Writen to file successfully"
        except Exception as e:
            return f"Error writing yml file: {str(e)}"


parsers = {
    "yml": YMLParser,
    "csv": CSVParser,
}


class CalculateMean:
    def __init__(self, source_type: str, target_type: str = None) -> None:
        self.source_parser = parsers[source_type](source_type)
        self.target = target_type if target_type else source_type
        self.target_parser = parsers[self.target](self.target)

    def _calculate(self, data):
        for i, aluno in enumerate(data["alunos"]):
            media = 0
            for nota in aluno["notas"]:
                media += nota
            data["alunos"][i]["media"] = media
        return data

    def create_mean(self):
        data = self.source_parser.extract()
        print("Data: ", data)

        new_data = self._calculate(data)

        logging.info(self.target_parser.load(new_data))


if __name__ == "__main__":
    try:
        myClass = CalculateMean(sys.argv[1], sys.argv[2])
    except IndexError:
        myClass = CalculateMean(sys.argv[1])

    myClass.create_mean()
