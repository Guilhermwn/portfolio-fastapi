import htpy as h # HTPY: Biblioteca base da criação do site
import bs4 # BeautifulSoup4: Biblioteca para identação e formatação do código html gerado


def render(element:h.Node) -> str:
    """
    Recebe: Um elemento qualquer Node HTPY\n
    Retorna: Uma string HTML formatada e identada do elemento HTPY
    """
    s = h.render_node(element)
    formatter = bs4.formatter.HTMLFormatter(indent=2)
    string = bs4.BeautifulSoup(s, features="html.parser")
    return string.prettify(formatter=formatter)