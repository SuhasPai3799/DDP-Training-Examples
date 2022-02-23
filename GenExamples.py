from owlready2 import *

onto_path.append("/home/suhas/DDP/vonda/examples/chatcat/src/main/resources/ontology/")
onto = get_ontology("UnivFAQ.owl").load()

with onto:
    sync_reasoner()





def prof_lookup_examples():

    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- lookup: Professors \n  examples: |\n"
    
    r = list(default_world.sparql(""" prefix univ: <http://www.semanticweb.org/suhaspai/ontologies/2021/4/UnivFAQ#> 
                                    SELECT ?y WHERE { ?x rdfs:label ?y . 
                                ?z rdfs:subClassOf* univ:Professors.
                    ?x rdf:type ?z}	"""))

    for ele in r:
        print(ele[0])
        prof_name = ele[0].lower()
        res_str +=  "  - " + "prof." + prof_name + "\n"
        res_str +=  "  - " + "dr." + prof_name + "\n"
        res_str += "  - " + prof_name + "\n"
        res_str += "  - " + get_main_name(prof_name) + "\n"
    
    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()

def course_prof_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: course_info \n  examples: | \n"
    r = list(default_world.sparql(""" prefix univ: <http://www.semanticweb.org/suhaspai/ontologies/2021/4/UnivFAQ#> 
                                SELECT ?y WHERE { ?x rdfs:label ?y . 
                            ?z rdfs:subClassOf* univ:Professors.
                ?x rdf:type ?z}	"""))

    for ele in r:
        prof_name = ele[0].lower()
        
        res_str += "  - what course does [{}](Professors) teach?\n".format(prof_name)
        res_str += "  - what course does [{}](Professors) teach?\n".format("prof. " + prof_name)
        res_str += "  - what course does [{}](Professors) teach?\n".format("prof " + prof_name)
        res_str += "  - what course does [{}](Professors) teach?\n".format("prof " + prof_name)
        res_str += "  - what course does [{}](Professors) teach?\n".format("professor " + prof_name)
        res_str += "  - what course does [{}](Professors) teach?\n".format("dr. " + prof_name)

        res_str += "  - courses taught by [{}](Professors)?\n".format(prof_name)
        res_str += "  - courses taught by [{}](Professors)?\n".format("prof. " + prof_name)
        res_str += "  - courses taught by [{}](Professors)?\n".format("prof " + prof_name)
        res_str += "  - courses taught by [{}](Professors)?\n".format("professor " + prof_name)
        res_str += "  - courses taught by [{}](Professors)?\n".format("prof " + prof_name)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()   

def get_main_name(name):
    s = sorted(name.split(" "), key=len)
    return s[-1]


def main():
    course_prof_examples()

if __name__ == "__main__":
    main()





  
