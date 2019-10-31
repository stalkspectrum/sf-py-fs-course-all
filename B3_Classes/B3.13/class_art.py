class HtmlArt:
    ''' Объект класса представляет собой стандартную обёртку из
    <!doctype>+<html>+</html>. Может содержать внутри другие тэги.
    Для <HTML> можно задать атрибут 'lang'. По умолчанию lang='ru'.
    '''
    def __init__(self, output=None, lang='ru'):
        self.output = output
        self.LANG = lang
        self.HTML_INSIDE_CONTENT = []
        self.HTML_INSIDE_STRINGS = []
    def __enter__(self):
        return self
    def __exit__(self, *ARG_LIST, **ARG_DICT):
        if self.output is not None and self.output != 'stdout':
            with open(self.output, mode='w', encoding='UTF-8', newline=None) as OUTPUT_FILE:
                OUTPUT_FILE.write(str(self))
                OUTPUT_FILE.close()
        else:
            print(self)
    def __iadd__(self, HTML_INSIDE_STRINGS):
        self.HTML_INSIDE_CONTENT.append(HTML_INSIDE_STRINGS)
        return self
    def __str__(self):
        HTML_CODE = '<!DOCTYPE html>\n<html lang=\"{DOC_LANG}\">\n'.format(DOC_LANG=self.LANG)
        for HTML_INSIDE_STRINGS in self.HTML_INSIDE_CONTENT:
            HTML_CODE += str(HTML_INSIDE_STRINGS)
        HTML_CODE += '</html>\n'
        return HTML_CODE

class TopLevelTagArt:
    ''' Класс для создания top-level тэгов <head> или <body> без атрибутов
    и без отступов. Могут содержать внутри себя другие тэги.
    '''
    def __init__(self, H_TLTAG, **ARG_DICT):
        self.H_TLTAG = H_TLTAG
        self.TLTAG_INSIDE_CONTENT = []
    def __enter__(self, *ARG_LIST, **ARG_DICT):
        return self
    def __exit__(self, *ARG_LIST, **ARG_DICT):
        pass
    def __iadd__(self, TLTAG_INSIDE_STRINGS):
        self.TLTAG_INSIDE_CONTENT.append(TLTAG_INSIDE_STRINGS)
        return self
    def __str__(self):
        HTML_CODE = '<{TAG_NAME}>\n'.format(TAG_NAME=self.H_TLTAG)
        for TLTAG_INSIDE_STRINGS in self.TLTAG_INSIDE_CONTENT:
            HTML_CODE += str(TLTAG_INSIDE_STRINGS)
        HTML_CODE += '</{TAG_NAME}>\n'.format(TAG_NAME=self.H_TLTAG)
        return HTML_CODE

class TagArt(TopLevelTagArt):
    ''' Основной класс для создания любых тэгов. Парных, одиночных, пустых,
    с текстом или другими тэгами внутри, с атрибутами или без них,
    с регулируемыми отступами для написания наглядной структуры.
    '''
    def __init__(self, H_TAG, is_single=False, tag_level='1', klass=None, css_class=None, **ATTRIBS_DICT):
        self.H_TAG = H_TAG
        self.SINGLE_TAG = is_single
        self.TAG_ATTRIBS_DICT = {}
        self.text = ''
        self.TAG_INSIDE_CONTENT = []
        #####=====----- Единичный отступ - 4 пробела -----=====#####
        self.TAG_INDENT = ' ' * 4
        #####=====----- Уровень вложенности по умолчанию - 1 -----=====#####
        self.TAG_LEVEL = int(tag_level)
        #####=====----- 'klass' (коряво) равносильно 'css_class' (рекомендуется к использованию) -----=====#####
        if klass is not None:
            self.TAG_ATTRIBS_DICT['class'] = ' '.join(klass)
        elif css_class is not None:
            self.TAG_ATTRIBS_DICT['class'] = ' '.join(css_class)
        #####=====----- Наполнение словаря атрибутами и замена '_' на '-' в именах атрибутов -----=====#####
        for I_ATTRIB, I_VALUE in ATTRIBS_DICT.items():
            if '_' in I_ATTRIB:
                I_ATTRIB = I_ATTRIB.replace('_', '-')
            self.TAG_ATTRIBS_DICT[I_ATTRIB] = I_VALUE
    def __iadd__(self, TAG_INSIDE_STRINGS):
        self.TAG_INSIDE_CONTENT.append(TAG_INSIDE_STRINGS)
        return self
    def __str__(self):
        S_ATTRIBS = []
        for S_ATTRIB, S_VALUE in self.TAG_ATTRIBS_DICT.items():
            S_ATTRIBS.append('{ATTR_NAME}="{ATTR_VAL}"'.format(ATTR_NAME=S_ATTRIB, ATTR_VAL=S_VALUE))
        TAG_ATTRIBS_STR = " ".join(S_ATTRIBS)
        if len(self.TAG_INSIDE_CONTENT) == 0:
            if self.SINGLE_TAG:
                if len(TAG_ATTRIBS_STR) == 0:
                    return '{TAG_SPACES}<{TAG_NAME}/>\n'.format(TAG_NAME=self.H_TAG, TAG_SPACES=(self.TAG_INDENT * self.TAG_LEVEL))
                else:
                    return '{TAG_SPACES}<{TAG_NAME} {TAG_ATTRIBS}/>\n'.format(TAG_NAME=self.H_TAG, TAG_ATTRIBS=TAG_ATTRIBS_STR, TAG_SPACES=(self.TAG_INDENT * self.TAG_LEVEL))
            else:
                if len(TAG_ATTRIBS_STR) == 0:
                    return '{TAG_SPACES}<{TAG_NAME}>{TAG_TEXT}</{TAG_NAME}>\n'.format(TAG_NAME=self.H_TAG, TAG_TEXT=self.text, TAG_SPACES=(self.TAG_INDENT * self.TAG_LEVEL))
                else:
                    return '{TAG_SPACES}<{TAG_NAME} {TAG_ATTRIBS}>{TAG_TEXT}</{TAG_NAME}>\n'.format(TAG_NAME=self.H_TAG, TAG_ATTRIBS=TAG_ATTRIBS_STR, TAG_TEXT=self.text, TAG_SPACES=(self.TAG_INDENT * self.TAG_LEVEL))
        else:
            if len(TAG_ATTRIBS_STR) == 0:
                TAG_OPEN = '{TAG_SPACES}<{TAG_NAME}>\n'.format(TAG_NAME=self.H_TAG, TAG_SPACES=(self.TAG_INDENT * self.TAG_LEVEL))
            else:
                TAG_OPEN = '{TAG_SPACES}<{TAG_NAME} {TAG_ATTRIBS}>\n'.format(TAG_NAME=self.H_TAG, TAG_ATTRIBS=TAG_ATTRIBS_STR, TAG_SPACES=(self.TAG_INDENT * self.TAG_LEVEL))
            if self.text:
                TAG_INSIDE = '{TAG_TEXT}'.format(TAG_TEXT=self.text)
            else:
                TAG_INSIDE = ''
            for TAG_INSIDE_STR in self.TAG_INSIDE_CONTENT:
                TAG_INSIDE += str(TAG_INSIDE_STR)
            TAG_CLOSE = '{TAG_SPACES}</{TAG_NAME}>\n'.format(TAG_NAME=self.H_TAG, TAG_SPACES=(self.TAG_INDENT * self.TAG_LEVEL))
            return TAG_OPEN + TAG_INSIDE + TAG_CLOSE
