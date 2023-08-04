import pytest

from sulguk import transform_html

SPACES_SPAN_HTML = """
1    <span>2</span> <span>   3<span>    </span>    </span>
"""
SPACES_SPAN_PLAIN = "1 2 3 "

# 1 empty line, ignore empty paragraphs
PARAGRAPH_HTML = """
    <p>1</p>
    <p></p>
    <p></p>
    <p></p>
    <p>2</p>
"""
PARAGRAPH_PLAIN = "\n1\n\n2\n\n"

# empty line between each block
HEADERS_HTML = """
    <h1>1</h1>
    <h1>2</h1>
    <p>3</p>
"""
HEADERS_PLAIN = "\n1\n\n2\n\n3\n\n"

# br adds new line after/before empty
BR_HTML = """
<p>1</p><br/>2<br/><br/><br/>3<br/><br/><p>4</p>
"""
BR_PLAIN = "\n1\n\n\n2\n\n\n3\n\n\n4\n\n"

SPACES_HTML_1 = "1  1"
SPACES_PLAIN_1 = "1 1"
SPACES_HTML_2 = "2&nbsp;&nbsp;2"
SPACES_PLAIN_2 = "2\xa0\xa02"
SPACES_HTML_3 = "3 &nbsp; 3"
SPACES_PLAIN_3 = "3 \xa0 3"
SPACES_HTML_4 = "4 \n 4"
SPACES_PLAIN_4 = "4 4"


@pytest.mark.parametrize("html, plain", [
    (SPACES_SPAN_HTML, SPACES_SPAN_PLAIN),
    (PARAGRAPH_HTML, PARAGRAPH_PLAIN),
    (HEADERS_HTML, HEADERS_PLAIN),
    (BR_HTML, BR_PLAIN),
    (SPACES_HTML_1, SPACES_PLAIN_1),
    (SPACES_HTML_2, SPACES_PLAIN_2),
    (SPACES_HTML_3, SPACES_PLAIN_3),
    (SPACES_HTML_4, SPACES_PLAIN_4),
])
def test_spaces(html, plain):
    result = transform_html(html)
    print(repr(plain))
    print(repr(html))
    assert result.text == plain
