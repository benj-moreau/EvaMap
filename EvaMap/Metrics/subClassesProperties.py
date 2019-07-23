import rdflib
import requests

from Metrics.metric import metric

def subClassesProperties(g_onto, liste_map, g_map, raw_data, g_link) :
    result = metric()
    result['name'] = "Correct use of subclasses and properties"
    set_SO = set()
    set_P = set()
    points = 0
    nbPossible = 0
    for s, p, o in g_map.triples((None, None, None)) :
        set_SO.add(s)
        set_SO.add(o)
        set_P.add(p)
    for subobj in set_SO :
        for _, _, o2 in g_onto.triples((None, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf'), subobj)) :
            if not isinstance(o2, rdflib.term.BNode) :
                nbPossible = nbPossible + 1
            if (None, None, o2) in g_map and not isinstance(o2, rdflib.term.BNode):
                points = points + 1
            elif (o2, None, None) in g_map and not isinstance(o2, rdflib.term.BNode):
                points = points + 1
            else :
                result['feedbacks'].append(str(o2) + "is missing.")
    for pred in set_P :
        for _, _, o3 in g_onto.triples((None, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#subPropertyOf'), pred)) :
            if not isinstance(o3, rdflib.term.BNode) :
                nbPossible = nbPossible + 1
            if (None, o3, None) in g_map and not isinstance(o3, rdflib.term.BNode) :
                points = points + 1
            else :
                result['feedbacks'].append(str(o3) + "is missing.")
    if nbPossible == 0 :
        result['score'] = 1
    else :
        result['score'] = points/nbPossible
    return result
