BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    signs = ['!', '?', '.', ',', ':', ';']
    last = min(len(text) - 1, start + size - 1)
    for i in range(last, start - 1, -1):
        if text[i] in signs and (i == (len(text) -1) or text[i + 1] not in signs):
            return text[start: i + 1], i - start + 1


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, "r", encoding='UTF-8') as f:
        text = f.read()
    start = 0
    last = len(text) - 1
    n_page = 1
    count = 0
    while start < last and count < 20:
        count += 1
        page, n_signs = _get_part_text(text=text, start=start, size=PAGE_SIZE)
        start += n_signs
        book[n_page] = page.lstrip()
        n_page += 1

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)