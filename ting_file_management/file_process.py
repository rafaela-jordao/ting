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


# Essa função deverá ser capaz de remover o primeiro arquivo processado
def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    file_removed = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file_removed} removido com sucesso\n")


# Essa função deverá ser capaz de apresentar as informações
# superficiais de um arquivo processado.
def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
