from owlready2 import *

onto_path.append("/home/suhas/DDP/vonda/examples/chatcat/src/main/resources/ontology/")
onto = get_ontology("UnivFAQ.owl").load()

with onto:
    sync_reasoner()

 
######### Global variables

pronouns = ["he", "him", "his", "she", "her", "hers", "they","them", "theirs"]
ObjectPronouns = ["that", "this", "it", "the","it's", "its"]
profs = ["prof", "profs","teacher", "instructor", "lecturer","professor"]

CS_syns = ["Computer Science", "CS","CSE", "Comp Sci", "Comp Science", "Computer Science Engineering"]
Elec_syns = ["Electrical Engineering", "EEE", "Elec Engg", "Elec", "Electrical", "Electronics", "ECE", "EE"]
Mech_syns = ["Mechanical Engineering", "Mechanical", "Mech", "Mechatronics", "ME", "Mech Engg", "Mechanical Engg"]
Chem_syns = ["Chemical Engineering","Chemical", "Chem Engineering", "Chem Engg", "Chem", "ChemE"]

dept_names = {}
dept_names["Computer Science"] = CS_syns
dept_names["Electrical Engg."] = Elec_syns
dept_names["Mechanical Engg."] = Mech_syns
dept_names["Chemical Engg."] = Chem_syns

btech_syns = ["btech", "beng", "beng", "bachelors", "bachelor of technology", "bachelors of technology"]
dd_syns = ["DD", "dual degree", "dual", "dual deg", "double deg", "integrated deg" , "integrated" , "integrated degree"]
mtech_syns = ["mtech", "masters", "masters of technology", "master of technology"]
phd_syns = [ "phd" , "postdoc" , "postdoc" , "doctor of philosophy" , "doctorate"]

programs_syns = [btech_syns,dd_syns,mtech_syns, phd_syns]


def program_lookup_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- lookup: Program \n  examples: |\n"
    for program in programs_syns:
        for program_syn in program:
            res_str += "    - {} \n".format(program_syn)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()

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

        res_str += "    - description of the [{}](Courses) course \n".format(course_code)
        res_str += "    - description of [{}](Courses) course \n".format(course_name)

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

def get_dept_facilities_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: dept_facilities_info \n  examples: | \n"

    for dept in dept_names.keys():
        dept_syns = dept_names[dept]
        for syn in dept_syns:
            res_str += "    - what labs are offered by the [{}](Department) department \n".format(syn)
            res_str += "    - what labs are in the [{}](Department) department \n".format(syn)
            res_str += "    - what labs are in the department of [{}](Department)  \n".format(syn)
            res_str += "    - what are the facilities in the department of [{}](Department)  \n".format(syn)
            res_str += "    - what facilities are offered by the [{}](Department) department \n".format(syn)
            res_str += "    - [{}](Department) department facilities \n".format(syn)
    
    for objPro in ObjectPronouns:
        res_str += "    - what are the facilities offered by [{}](ObjectPronoun) department \n".format(objPro)
        res_str += "    - what are the facilities in [{}](ObjectPronoun) department \n".format(objPro)
        res_str += "    - what are the labs in [{}](ObjectPronoun) department \n".format(objPro)
    
    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()   

def get_dept_courses_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: dept_courses_info \n  examples: | \n"

    for dept in dept_names.keys():
        dept_syns = dept_names[dept]
        for syn in dept_syns:
            res_str += "    - what courses are offered by the [{}](Department) department this year \n".format(syn)
            res_str += "    - what courses are offered by the department  [{}](Department) this year \n".format(syn)
            res_str += "    - courses offered by the [{}](Department) department \n".format(syn)
            res_str += "    - [{}](Department) department courses \n".format(syn)
            res_str += "    - [{}](Department) courses \n".format(syn)
            res_str += "    - courses in [{}](Department) \n".format(syn)
    
    for objPro in ObjectPronouns:
        res_str += "    - [{}](ObjectPronoun) department courses \n".format(objPro)
        res_str += "    - courses in [{}](ObjectPronoun) department  \n".format(objPro)
        res_str += "    - courses offered by [{}](ObjectPronoun) department  \n".format(objPro)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()   

def get_dept_profs_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: dept_profs_info \n  examples: | \n"

    for dept in dept_names.keys():
        dept_syns = dept_names[dept]
        for syn in dept_syns:
            res_str += "    - professors in the [{}](Department) department \n".format(syn)
            res_str += "    - list all the profs in the [{}](Department) department \n".format(syn)
            res_str += "    - list all the teachers in the [{}](Department) dept\n".format(syn)
            res_str += "    - [{}](Department) department professors\n".format(syn)
            res_str += "    - [{}](Department) department profs\n".format(syn)
            res_str += "    - lecturers teaching in [{}](Department) department \n".format(syn)
            res_str += "    - teachers teaching in [{}](Department) department \n".format(syn)
    
    for objPro in ObjectPronouns:
        res_str += "    - teachers teaching in [{}](ObjectPronoun) department \n".format(objPro)
        res_str += "    - professors in [{}](ObjectPronoun) department \n".format(objPro)
        res_str += "    - [{}](ObjectPronoun) department profs\n".format(objPro)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close()  

def get_dept_ug_progs_examples():

    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: dept_ug_programs_info \n  examples: | \n"
    for dept in dept_names.keys():
        dept_syns = dept_names[dept]
        for syn in dept_syns:
            res_str += "    - undergrad programs in [{}](Department) department \n".format(syn)
            res_str += "    - undergraduate programs in [{}](Department) department \n".format(syn)
            res_str += "    - undergraduate programs in [{}](Department) department \n".format(syn)
            res_str += "    - [{}](Department) department undergraduate programs \n".format(syn)
            res_str += "    - [{}](Department) department ug programs \n".format(syn)
            res_str += "    - undergrad programs offered by [{}](Department) department \n".format(syn)
            res_str += "    - what programs does [{}](Department) department offer for undergraduates \n".format(syn)

    for objPro in ObjectPronouns:
            res_str += "    - undergrad programs in [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - ug programs in [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - undergraduate programs in [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - [{}](ObjectPronoun) department undergraduate programs \n".format(objPro)
            res_str += "    - [{}](ObjectPronoun) department ug programs \n".format(objPro)
            res_str += "    - undergrad programs offered by [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - what programs does [{}](ObjectPronoun) department offer for undergraduates \n".format(objPro)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close() 

def get_dept_pg_progs_examples():

    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: dept_pg_programs_info \n  examples: | \n"
    for dept in dept_names.keys():
        dept_syns = dept_names[dept]
        for syn in dept_syns:
            res_str += "    - postgrad programs in [{}](Department) department \n".format(syn)
            res_str += "    - postgraduate programs in [{}](Department) department \n".format(syn)
            res_str += "    - postgraduate programs in [{}](Department) department \n".format(syn)
            res_str += "    - [{}](Department) department postgraduate programs \n".format(syn)
            res_str += "    - [{}](Department) department pg programs \n".format(syn)
            res_str += "    - postgrad programs offered by [{}](Department) department \n".format(syn)
            res_str += "    - what programs does [{}](Department) department offer for postgraduates \n".format(syn)

    for objPro in ObjectPronouns:
            res_str += "    - postgrad programs in [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - pg programs in [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - postgraduate programs in [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - [{}](ObjectPronoun) department postgraduate programs \n".format(objPro)
            res_str += "    - [{}](ObjectPronoun) department pg programs \n".format(objPro)
            res_str += "    - postgrad programs offered by [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - what programs does [{}](ObjectPronoun) department offer for postgraduates \n".format(objPro)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close() 

def get_dept_progs_examples():

    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: dept_programs_info \n  examples: | \n"
    for dept in dept_names.keys():
        dept_syns = dept_names[dept]
        for syn in dept_syns:
            res_str += "    - programs in [{}](Department) department \n".format(syn)
            res_str += "    - programs offered by [{}](Department) department \n".format(syn)
            res_str += "    - what program does [{}](Department) department offer \n".format(syn)
            res_str += "    - what program does [{}](Department) offer \n".format(syn)
            res_str += "    - [{}](Department) programs \n".format(syn)
            res_str += "    - [{}](Department) degrees \n".format(syn)



    for objPro in ObjectPronouns:
            res_str += "    - programs in [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - programs offered by [{}](ObjectPronoun) department \n".format(objPro)
            res_str += "    - what program does [{}](ObjectPronoun) department offer \n".format(objPro)
            res_str += "    - what program does [{}](ObjectPronoun) offer \n".format(objPro)
            res_str += "    - [{}](ObjectPronoun) department programs \n".format(objPro)
            res_str += "    - [{}](ObjectPronoun) department degrees \n".format(objPro)

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close() 

def get_dept_info_examples():
    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: dept_info \n  examples: | \n"
    for dept in dept_names.keys():
        dept_syns = dept_names[dept]
        for syn in dept_syns:
            res_str += "    - tell me about the [{}](Department) department \n".format(syn)
            res_str += "    - information about [{}](Department) department \n".format(syn)
            res_str += "    -  [{}](Department) department description \n".format(syn)
            res_str += "    -  [{}](Department) dept description \n".format(syn)
            res_str += "    -  details on the [{}](Department) department in IIT madras \n".format(syn)

    for objPro in ObjectPronouns:
        res_str += "    - tell me about the [{}](ObjectPronoun) department \n".format(objPro)
        res_str += "    - information about [{}](ObjectPronoun) department \n".format(objPro)
        res_str += "    -  [{}](ObjectPronoun) department description \n".format(objPro)
        res_str += "    -  [{}](ObjectPronoun) dept description \n".format(objPro)
        res_str += "    -  details on the [{}](ObjectPronoun) department in IIT madras \n".format(objPro)
    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close() 

def get_program_info_examples():

    f1 = open("cur_examples.txt","w+")
    f2 = open("all_examples.txt","a+")
    res_str = "- intent: program_info \n  examples: | \n"
    for dept in dept_names.keys():
        dept_syns = dept_names[dept]
        for syn in dept_syns:
            for program in programs_syns:
                for program_syn in program:
                    res_str += "    - tell me about the [{}](Program) in [{}](Department) department \n".format(program_syn,syn)
                    res_str += "    - information about [{}](Program) in [{}](Department)  \n".format(program_syn,syn)
                    res_str += "    - details of the [{}](Department) [{}](Program) program  \n".format(syn, program_syn)
    
    for objPro in ObjectPronouns:
        for program in programs_syns:
                for program_syn in program:
                    res_str += "    - tell me about the [{}](Program) in [{}](ObjectPronoun) department  \n".format(program_syn,objPro)
                    res_str += "    - information about [{}](Program) in [{}](ObjectProunoun)  \n".format(program_syn,objPro)
                    res_str += "    - details of the [{}](ObjectPronoun) [{}](Program) program  \n".format(objPro, program_syn)

    for objPro in ObjectPronouns:
        res_str += "    - tell me about [{}](ObjectPronoun) program  \n".format(objPro)
        res_str += "    - information about [{}](ObjectPronoun) program  \n".format(objPro)       
        res_str += "    - [{}](ObjectPronoun) program details  \n".format(objPro)  

    f1.write(res_str)
    f2.write(res_str)
    f1.close()
    f2.close() 


def get_main_name(name):
    s = sorted(name.split(" "), key=len)
    return s[-1]


def main():
    get_program_info_examples()
    pass

if __name__ == "__main__":
    main()





  
