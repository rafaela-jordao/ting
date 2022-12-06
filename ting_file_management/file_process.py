from ting_file_management.file_management import txt_importer
import sys


# Essa função deverá ser capaz de transformar o conteúdo da lista
# gerada pela função txt_importer em um dicionário que será armazenado
# dentro da Queue.
def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    content = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": (content),
    }
    instance.enqueue(data)
    sys.stdout.write(str(data))
    return data


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
