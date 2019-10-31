'''----------------------------------------------------------------------------
- Основной файл для генерации HTML-кода. Необходимые классы импортируются из
  ./class_art.py. Класс Tag - частично наследует из класса TopLevelTag
  (переписаны только методы __init__ и __str__).

          -----===== Улучшайзинг и фиченаворотинг =====-----
- Для корректности вывода учитывается кодировка UTF-8.
- Для вывода на консоль можно указывать как None, так и 'stdout'.
- Рекомендуется использовать более изящный 'css_class' вместо
  корявого 'klass' (хотя его тоже можно).
- Устранено возникновение лишнего пробела перед '>' или '/>' в тэгах
  вроде <title >, <br />.
- Во избежание путаницы в контекстных менеджерах для вложенных одноимённых
  тэгов (например, div) надо использовать уникальные идентификаторы -
  ...as div_1, ...as div_2, etc.
- Для красоты строки генерируются с отступами в зависимости от уровня вложенности
  тэгов. К сожалению, уровень вложенности задаётся вручную значением tag_level
  для объекта класса Tag. Единица отступа - 4 пробела.
  Таким образом tag_level="3" задаёт отступ в 12 пробелов.
- В итоге, для проверки работы всего этого в код главной функции добавлено
  побольше тэгов, так что выхлоп заметно отличается от эталонного, хотя
  и содержит его.
'''

from class_art import HtmlArt as HTML
from class_art import TopLevelTagArt as TopLevelTag
from class_art import TagArt as Tag

def generate_code(F_OUTPUT=None):
    with HTML(output=F_OUTPUT, lang="en-us") as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "Page title"
                head += title
            with Tag("meta", is_single=True, http_equiv="Content-Type", content="text/html; charset=UTF-8") as meta:
                head += meta
            doc += head
        with TopLevelTag("body") as body:
            with Tag("h1", klass=("main-text",)) as h1:
                h1.text = "Page head"
                body += h1
            with Tag("div", klass=("container", "container-fluid"), id="lead", test_und="test_und") as div_1:
                with Tag("p", tag_level="2") as paragraph:
                    paragraph.text = "Another test"
                    div_1 += paragraph
                with Tag("img", is_single=True, src="/icon.png", data_image="responsive", tag_level="2") as img:
                    div_1 += img
                body += div_1
            with Tag("hr", is_single=True) as hr:
                body += hr
            with Tag("div", css_class=("div2test",)) as div_2:
                with Tag("div", css_class=("div2-test",), id_t="id_test", tag_level="2") as div_3:
                    with Tag("p", css_class=("par_test",), tag_level="3") as paragraph:
                        paragraph.text = "YET ANOTHER MOVIE"
                        div_3 += paragraph
                    with Tag("div", id="div4_id", tag_level="3") as div_4:
                        with Tag("img", is_single=True, src="/strange.png", tag_level="4") as img:
                            div_4 += img
                        div_3 += div_4
                    div_2 += div_3
                body += div_2
            doc += body

if __name__ == '__main__':
    generate_code('result.html')    ##### ('/path/to/file.html') задаёт результирующий файл.
    #generate_code('stdout')         ##### (None) или ('stdout') записывает на стандартный вывод (консоль).
