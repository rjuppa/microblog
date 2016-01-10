from jinja2 import Markup


class momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, format):
        return Markup("<script>\ndocument.write(moment(\"%s\").%s);\n</script>" % (self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), format))

    def format(self, fmt):
        return self.render("format(\"%s\")" % fmt)

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")


def render_marks(some_func):
     def inner(obj, text):
         if not text:
             text = ''
         text = text.replace('{b}', '<b>')
         text = text.replace('{/b}', '</b>')
         text = text.replace('{br}', '<br>')
         text = text.replace('\r\n', '<br>')
         text = text.replace('{pre}', '<pre>')
         text = text.replace('{/pre}', '</pre>')
         text = text.replace('{code}', '<div class="highlight"><pre><code>')
         text = text.replace('{/code}', '</code></pre></div>')
         text = text.replace('{ahref}', '<a href="')
         text = text.replace('{/ahref}', '" target="_blank">')
         text = text.replace('{a}', '')
         text = text.replace('{/a}', '</a>')
         return some_func(obj, text)
     return inner

def clear_marks(some_func):
     def inner(obj, text):
         if not text:
             text = ''
         text = text.replace('{b}', '')
         text = text.replace('{/b}', '')
         text = text.replace('{br}', '')
         text = text.replace('\r\n', '')
         text = text.replace('{pre}', '')
         text = text.replace('{/pre}', '')
         text = text.replace('{code}', '')
         text = text.replace('{/code}', '')
         text = text.replace('{ahref}', '')
         text = text.replace('{/ahref}', '')
         text = text.replace('{a}', '')
         text = text.replace('{/a}', '')
         return some_func(obj, text)
     return inner


class use_html(object):

    @render_marks
    def replace_html(self, text):
        if text:
            return text
        else:
            return ''

    def render(self, text):
        return Markup(self.replace_html(text))

    @clear_marks
    def shorter(self, text):
        text = self.replace_html(text)
        if '<br>' in text:
            n = text.index('<br>')
            text = text[0:n]
        else:
            text = text[0:160]

        return Markup(text)
