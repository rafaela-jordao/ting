def exists_word(word, instance):
    content = list()
    for i in range(len(instance)):
        row = instance.search(i)

        list_data = [
            {"linha": (index + 1)}
            for index, line in enumerate(row["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]

        file = {
            "palavra": word,
            "arquivo": row["nome_do_arquivo"],
            "ocorrencias": list_data,
        }

        if not len(file["ocorrencias"]):
            return []

        if file:
            content.append(file)
        return content


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
