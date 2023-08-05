from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from abc import ABC, abstractmethod
from enum import Enum
from jinja2 import Markup

__all__ = ['Element']


@dataclass
class ElementBase(ABC):
    """
    ElementBase Class require 'name' and 'content'
    """

    class Element(str, Enum):
        H1 = "h1"
        H2 = "h2"
        H3 = "h3"
        H4 = "h4"
        H5 = "h5"
        H6 = "h6"
        SPAN = "span"
        UL = "ul"
        OL = "ol"
        LI = "li"
        DIV = "div"
        FORM = "form"
        P = "p"
        TABLE = "table"
        TR = "tr"
        TD = "td"
        TH = "th"
        BODY = "body"
        HEADER = "header"
        FOOTER = "footer"
        INPUT = "input"
        IMG = "img"
        A = 'a'
        SELECT = 'select'
        OPTION = 'option'
        HR = 'hr'

    element: Union[ Element, str ]
    content: Union[ ElementBase, str]
    _id: Optional[ str ] = None
    _type: Optional[ str ] = None
    klass: Optional[ str ] = None
    style: Optional[ str ] = None
    action: Optional[ str ] = None
    method: Optional[ str ] = None
    src: Optional[ str ] = None
    href: Optional[ str ] = None
    value: Optional[ str ] = None
    name: Optional[ str ] = None

    def __html__(self):
        _id = f' id="{self._id}"' if self._id else ""
        _klass = f' class="{self.klass}"' if self.klass else ""
        _style = f' style="{self.style}"' if self.style else ""
        if self.element == self.Element.FORM:
            _action = f' action="{self.action}"' if self.action else ' action="/"'
            _method = f' method="{self.method}"' if self.method else ' method="GET"'
            return f"<{self.element}{_id}{_action}{_method}{_klass}{_style}>{self.content}</{self.element}>"
        elif self.element == self.Element.IMG:
            if self.src:
                _src = f' src="{self.src}"'
                return f"<{self.element}{_id}{_klass}{_style}{_src}/>"
            else:
                raise ValueError("scr is needed")
        elif self.element == self.Element.A:
            if self.href:
                href = f' href="{self.href}"'
                if self.content:
                    content = f'{self.content}'
                    return f"<{self.element}{_id}{_klass}{_style}{href}>{content}</{self.element}>"
                else:
                    raise ValueError('content is needed')
            else:
                raise ValueError("href is needed")
        elif self.element == self.Element.INPUT:
            if self._type:
                _type = f' type="{self._type}"'
                if self.name:
                    name = f' name="{self.name}"'
                    return f"<{self.element}{_id}{_klass}{_style}{_type}{name}/>"
                return f"<{self.element}{_id}{_klass}{_style}{_type}/>"
            else:
                _type = f' type="submit"'
                if self.name:
                    name = f' name="{self.name}"'
                    return f"<{self.element}{_id}{_klass}{_style}{_type}{name}/>"
                return f"<{self.element}{_id}{_klass}{_style}{_type}/>"
        elif self.element == self.Element.HR:
            return '<hr>\n'
        return f"<{self.element}{_id}{_klass}{_style}>{self.content}</{self.element}>"

    def __str__(self):
        return Markup(self)

    def __add__(self, other):
        if issubclass(type(other), (ElementBase, str)):
            return str(self) + str(other)
        raise ValueError(f'cannot perform {type(self)} + {type(other)}')


class Element(ElementBase):
    pass

