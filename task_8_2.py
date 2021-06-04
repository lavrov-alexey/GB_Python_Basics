import re

PATH_LOG_FILE = "nginx_logs.txt"
PATH_PARS_LOG = "pars_nginx_logs.txt"
RE_PATTERN = r"(?P<remote_addr>^.+)(?: - - )(?:\[" \
              r"(?P<req_datetime>.+)\]+)(?: \"" \
              r"(?P<req_type>[A-Z]+) )" \
              r"(?P<req_resource>[/\w\d]+)( [\w\d/.]+\" )" \
              r"(?P<resp_code>\d+) " \
              r"(?P<resp_size>\d+)"


def log_parser(log_lines: list, cmp_pattern):
    """Парсит переданный массив строк лога (вида nginx_logs) в соответствии с
    компилированным (re) шаблоном cmp_pattern, отдает список tupple вида:
    (remote_addr, request_datetime, request_type, requested_resource,
    response_code, response_size)"""
    res_pars = []
    for line in log_lines:
        result = cmp_pattern.search(line)
        res_pars.append(tuple(result.groupdict().values()))

    return res_pars


if __name__ == "__main__":
    re_pattern = re.compile(RE_PATTERN)

    # считаем, что лог сильно меньше ОЗУ - читаем целиком
    with open(PATH_LOG_FILE, 'r', encoding='utf-8') as f:
        content = f.readlines()

    pars_data = log_parser(content, re_pattern)

    with open(PATH_PARS_LOG, 'w', encoding='utf-8') as f:
        for pars_line in pars_data:
            f.write(f"{pars_line}\n")

    print(f'Распарсено {len(pars_data)} строк файла {PATH_LOG_FILE}.\n'
          f'Результат парсинга сохранен в файл {PATH_PARS_LOG}, '
          f'последние 5 строк:')
    print(*pars_data[-5:], sep='\n')
