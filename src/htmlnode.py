class HTMLNODE:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        htmlString = ""
        if self.props == None:
            return htmlString
        for prop in self.props:
            key, value = prop
            htmlString += f' {key}="{value}"'
        return htmlString
    
    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNODE):
    def __init__(self, value, tag = None, props= None ):
        super().__init__(tag=tag, value=value, children = None,  props = props)

    def to_html(self):
        if not self.value:
            raise ValueError("error")
        if self.tag == None:
            return self.value
        self.new_props = self.props_to_html()
        return f"<{self.tag}{self.new_props}>{self.value}</{self.tag}>"

class ParentNode(HTMLNODE):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag=tag, value=None, children= children, props=props )
    
    def to_html(self):
        if self.tag == None:
            raise ValueError('incorrect value')
        if self.children == None:
            raise ValueError('Children required')
        result = ""
        for child in self.children:
                child_result = child.to_html()
                result += child_result
        return f"<{self.tag}>{result}</{self.tag}>"