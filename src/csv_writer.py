import json


def data_write_in_json(cdr: str, family: str, file_output: str) -> None:
    with open('freq_aa_in_canonical_form.json', 'r') as f:
        data = json.load(f)
    # Получаем данные для true_family из словаря data
    data_for_true_family = data.get(family, [])

    # Создаем словарь с данными для записи в файл
    data_to_write = {cdr: data_for_true_family}

    # Записываем данные в файл file_output
    with open(file_output, 'a') as f:
        json.dump(data_to_write, f, indent=4)
        f.write('\n')
        print(f"Data for {family} has been written to {file_output} file.")
        print()
