from owlready2 import *

onto_path.append("/home/suhas/DDP/vonda/examples/chatcat/src/main/resources/ontology/")
onto = get_ontology("UnivFAQ.owl").load()

with onto:
    sync_reasoner()

 
######### Global variables

pronouns = ["he", "him", "his", "she", "her", "hers", "they","them", "theirs"]
ObjectPronouns = ["that", "this", "it", "the","it's", "its"]
profs = ["prof", "profs","teacher", "instructor", "lecturer","professor"]



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


def get_prof_research_examples():
    
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: prof_research_info \n  examples: | \n"
    r = list(default_world.sparql(""" prefix univ: <http://www.semanticweb.org/suhaspai/ontologies/2021/4/UnivFAQ#> 
                                SELECT ?y WHERE { ?x rdfs:label ?y . 
                            ?z rdfs:subClassOf* univ:Professors.
                ?x rdf:type ?z}	"""))  
    
    for ele in r:
        prof_name = ele[0].lower()

        res_str += "    - what are [{}'s](Professors) research interests ?\n".format(prof_name)
        res_str += "    - what are [{}'s](Professors) research areas ?\n".format(prof_name)
        res_str += "    - what are [{}'s](Professors) research specialities ?\n".format(prof_name)
        res_str += "    - what are [{}'s](Professors) areas of interests ?\n".format(prof_name)
        res_str += "    - what field is [{}](Professors) interested in ?\n".format(prof_name)
        res_str += "    - what research field is [{}](Professors) working in ?\n".format(prof_name)
        res_str += "    - what research field does [{}](Professors) specialize in ?\n".format(prof_name)
    
    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()


def get_course_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- lookup: Courses \n  examples: |\n"
    r = list(default_world.sparql(""" prefix univ: <http://www.semanticweb.org/suhaspai/ontologies/2021/4/UnivFAQ#> 
                                SELECT ?x ?y WHERE { ?x rdfs:label ?y . 
                            ?z rdfs:subClassOf* univ:Courses.
                ?x rdf:type ?z}	"""))

    for ele in r:
        res_str += "  - {}\n".format((ele[0].iri)[-6:])
        res_str += "  - {}\n".format(ele[1])
    
    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()   

def get_course_details_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: course_info \n  examples: | \n"
    r = list(default_world.sparql(""" prefix univ: <http://www.semanticweb.org/suhaspai/ontologies/2021/4/UnivFAQ#> 
                                SELECT ?x ?y WHERE { ?x rdfs:label ?y . 
                            ?z rdfs:subClassOf* univ:Courses.
                ?x rdf:type ?z}	"""))

    for ele in r:
        
        course_code = (ele[0].iri)[-6:]
        course_name = ele[1]

        res_str += "    - tell me about the course [{}](Courses)\n".format(course_code)
        res_str += "    - tell me about the course [{}](Courses)\n".format(course_name)

        res_str += "    - tell me about the [{}](Courses) course \n".format(course_code)
        res_str += "    - tell me about the [{}](Courses) course \n".format(course_name)

        res_str += "    - information about the [{}](Courses) course \n".format(course_code)
        res_str += "    - information about the [{}](Courses) course \n".format(course_name)

        res_str += "    - details of the [{}](Courses) course \n".format(course_code)
        res_str += "    - details of the [{}](Courses) course \n".format(course_name)

        res_str += "    - what is the [{}](Courses) course about \n".format(course_code)
        res_str += "    - what is the [{}](Courses) course about \n".format(course_name)

        res_str += "    - describe the [{}](Courses) course \n".format(course_code)
        res_str += "    - describe the [{}](Courses) course \n".format(course_name)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close() 

def get_course_prof_info_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: course_prof_info \n  examples: | \n"
    r = list(default_world.sparql(""" prefix univ: <http://www.semanticweb.org/suhaspai/ontologies/2021/4/UnivFAQ#> 
                                SELECT ?x ?y WHERE { ?x rdfs:label ?y . 
                            ?z rdfs:subClassOf* univ:Courses.
                ?x rdf:type ?z}	"""))

    for ele in r:
        
        course_code = (ele[0].iri)[-6:]
        course_name = ele[1]
        for syns in profs:

            res_str += "    - which {} teaches the course [{}](Courses) ?\n".format(syns, course_name)
            res_str += "    - which {} teaches the course [{}](Courses) ?\n".format(syns, course_code)

            res_str += "    - which {} teaches the [{}](Courses) course ?\n".format(syns, course_name)
            res_str += "    - which {} teaches the [{}](Courses) course ?\n".format(syns, course_code)

        res_str += "    - who teaches the [{}](Courses) course ?\n".format(course_name)
        res_str += "    - who teaches the [{}](Courses) course ?\n".format(course_code)

        res_str += "    - who teaches the course [{}](Courses) ?\n".format(course_name)
        res_str += "    - who teaches the course [{}](Courses) ?\n".format(course_code)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close() 

def get_course_prereqs_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: course_prereq_info \n  examples: | \n"

    r = list(default_world.sparql(""" prefix univ: <http://www.semanticweb.org/suhaspai/ontologies/2021/4/UnivFAQ#> 
                                SELECT ?x ?y WHERE { ?x rdfs:label ?y . 
                            ?z rdfs:subClassOf* univ:Courses.
                ?x rdf:type ?z}	"""))
    all_req_syns = ["prerequisites", "prereqs", "requirements", "prerequisite"]

    for ele in r:
        
        course_code = (ele[0].iri)[-6:]
        course_name = ele[1]
        
        for req_syns in all_req_syns:

            res_str += "    - what courses are the {} for the course [{}](Courses) \n".format(req_syns, course_code)
            res_str += "    - what courses are the {} for the course [{}](Courses) \n".format(req_syns, course_name)

            res_str += "    - what courses are the {} for the [{}](Courses) course \n".format(req_syns, course_code)
            res_str += "    - what courses are the {} for the [{}](Courses) course \n".format(req_syns, course_name)

        res_str += "    - what courses have to be completed before the [{}](Courses) course \n".format(course_name) 
        res_str += "    - what courses have to be completed before the [{}](Courses) course \n".format(course_code)

        res_str += "    - what prerequisite courses does the [{}](Courses) course have \n".format(course_name)  
        res_str += "    - what prerequisite courses does the [{}](Courses) course have \n".format(course_code) 

    for objPro in ObjectPronouns:
        res_str += "    - what prerequisite courses does [{}](ObjectPronoun) have \n".format(objPro)
        res_str += "    - what are [{}](ObjectPronoun) prerequisite courses \n".format(objPro)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()   

def get_main_name(name):
    s = sorted(name.split(" "), key=len)
    return s[-1]


def main():
    get_prof_research_examples()
    pass

if __name__ == "__main__":
    main()





  
