from urllib.parse import urlparse
import re

import rdflib

from EvaMap.Metrics.metric import metric

def humanReadableURIs(g_onto, liste_map, g_map, raw_data, g_link) :
    nbPossible = 0
    points = 0
    result = metric()
    result['name'] = "Human readable URIs"
    set_URIs = set()
    for s, p, o in g_map.triples((None, None, None)):
        if isinstance(s, rdflib.term.URIRef) :
            set_URIs.add(s)
    for s in set_URIs:
        if isinstance(s, rdflib.term.URIRef):
            nbPossible = nbPossible + 1
            str = urlparse(s)
            if str.fragment != '':
                str = str.fragment
                if test_HumanReadable(str) :
                    points = points + 1
                else :
                    result['feedbacks'].append(f"It seems that {str} is not a Human Readable URI")
            else :
                str = str.path
                str = str.split("/")[-1]
                if test_HumanReadable(str) :
                    points = points + 1
                else :
                    result['feedbacks'].append(f"It seems that {str} is not a Human Readable URI")
            if str.startswith('$') :
                nbPossible = nbPossible - 1
                points = points - 1
    if nbPossible == 0:
        result['score'] = 1
    else:
        result['score'] = 1-((nbPossible) - points)/(nbPossible)
    return result


def test_HumanReadable(str) :
    if not str.startswith('$') :
        regexp = re.compile(r'[A-Z][A-Z][A-Z]') #Si on a une suite de 3 majuscules
        if regexp.search(str):
            return False
        regexp = re.compile(r'[0-9]+[A-Za-z-_.]+[0-9]*$') #Si on a un string contenant un chiffre au milieu d'autre caractères
        if regexp.search(str):
            return False
        regexp = re.compile(r'[$+!*\'()]') #Si on a un caractère particulier qui ne devrait pas exister
        if regexp.search(str):
            return False
        if len(str) < 3 : #si la taille est inférieure à 3
            return False
        if re.subn('[0-9]', '', str)[1] > 8 : #Si on a plus de 8 chiffres (date)*
            return False
    return True