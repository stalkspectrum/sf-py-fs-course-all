class Tag:
    def __init__(self, tag, toplevel=False, is_single=False):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.toplevel = toplevel
        self.is_single = is_single
        self.children = []
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        if self.toplevel:
            print("<%s>" % self.tag)
            for child in self.children:
                print(child)
            print("</%s>" % self.tag)
    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)
        if self.children:
            opening = "<{tag} {attrs}>".format(tag=self.tag, attrs=attrs)
            internal = "%s" % self.text
            for child in self.children:
                internal += str(child)
            ending = "</%s>" % self.tag
            return opening + internal + ending
        else:
            if self.is_single:
                return "<{tag} {attrs}/>".format(tag=self.tag, attrs=attrs)
            else:
                return "<{tag} {attrs}>{text}</{tag}>".format(
                    tag=self.tag, attrs=attrs, text=self.text
                )
