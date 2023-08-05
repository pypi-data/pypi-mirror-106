import os


class HF:
    def __init__(self):
        self.header: str = None
        self.footer: str = None


class Common(HF):
    def __init__(self):
        self.list_header: str = None
        self.list_footer: str = None
        self.list_entry: str = None
        self.list_separator: str = None


class Template(HF):
    def __init__(self):
        self.article: HF = HF()
        self.articles: Common = Common()
        self.tags: Common = Common()


    def write_templates(self, src: str):
        # get initial working directory
        iwd = os.getcwd()
        os.chdir(src)

        print('creating dir structure...')
        # create templates dir
        os.mkdir('templates')
        os.chdir('templates')

        # common
        os.mkdir('common')
        os.chdir('common')
        self.__write_template('header.html',
                              ['<!DOCTYPE html>\n',
                               '<html lang="$$LANG">\n',
                               '<head>\n',
                               '<meta charset="utf-8">\n',
                               '<title>$$TITLE</title>\n',
                               '$$EXTRAHEAD\n',
                               '</head>\n',
                               '<body>\n'])
        self.__write_template('footer.html',
                              ['</body>\n',
                               '</html>\n'])

        # go back to templates
        os.chdir('..')

        # article entry
        os.mkdir('article')
        os.chdir('article')
        self.__write_template('header.html',
                              ['<h1>$$TITLE</h1>'])
        self.__write_template('footer.html',
                              [''])

        # article index
        os.mkdir('index')
        os.chdir('index')
        self.__write_template('header.html',
                              [''])
        self.__write_template('list_header.html',
                              ['<h2>Articles</h2>\n',
                               '<ul>\n'])
        self.__write_template('list_entry.html',
                              ['<li><a href="$$URL">$$DATE - $$TITLE</a></li>\n'])
        self.__write_template('list_separator.html',
                              [''])
        self.__write_template('list_footer.html',
                              ['</ul>\n'])
        self.__write_template('footer.html',
                              [''])

        # go back to templates
        os.chdir('../..')

        # tag
        os.mkdir('tag')
        os.chdir('tag')
        self.__write_template('header.html',
                              [''])
        self.__write_template('list_header.html',
                              ['<p>Tags: '])
        self.__write_template('list_entry.html',
                              ['<a href="$$URL">$$NAME</a>'])
        self.__write_template('list_separator.html',
                              [', '])
        self.__write_template('list_footer.html',
                              ['</p>\n'])
        self.__write_template('footer.html',
                              [''])

        # return to initial working directory
        os.chdir(iwd)
        print('done creating dir structure...')


    def read_templates(self, src: str):
        # get initial working directory
        iwd = os.getcwd()
        os.chdir(os.path.join(src, 'templates'))

        # common
        os.chdir('common')
        self.header = self.__read_template('header.html')
        self.footer = self.__read_template('footer.html')

        # go back to templates
        os.chdir('..')

        # article entry
        os.chdir('article')
        self.article.header = self.__read_template('header.html')
        self.article.footer = self.__read_template('footer.html')

        # article index
        os.chdir('index')
        self.articles.header = self.__read_template('header.html')
        self.articles.list_header = \
                self.__read_template('list_header.html')
        self.articles.list_entry = \
                self.__read_template('list_entry.html')
        self.articles.list_separator = \
                self.__read_template('list_separator.html')
        self.articles.list_footer = \
                self.__read_template('list_footer.html')
        self.articles.footer = self.__read_template('footer.html')

        # go back to templates
        os.chdir('../..')

        # tag
        os.chdir('tag')
        self.tags.header = self.__read_template('header.html')
        self.tags.list_header = self.__read_template('list_header.html')
        self.tags.list_entry = self.__read_template('list_entry.html')
        self.tags.list_separator = self.__read_template('list_separator.html')
        self.tags.list_footer = self.__read_template('list_footer.html')
        self.tags.footer = self.__read_template('footer.html')

        # return to initial working directory
        os.chdir(iwd)


    def __write_template(self, file_name: str, content: list[str]):
        with open(file_name, 'w+') as f:
            for c in content:
                f.write(c)

    def __read_template(self, file_name: str) -> str:
        out: str = None
        with open(file_name, 'r') as f:
            out = f.read()

        return out
