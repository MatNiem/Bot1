from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def jp2_quote(nr):
    source = urlopen('https://pl.wikiquote.org/w/index.php?title=Jan_Pawe%C5%82_II&action=edit')

    soup = BeautifulSoup(source, features='html.parser')

    jp2_regex = re.compile(r"\* (?!Autor)(?!Opis)(?!Źródło)(?!Zobacz też)(?!\[\[)(.*)")

    lista = jp2_regex.findall(str(soup))
    return lista[nr]
