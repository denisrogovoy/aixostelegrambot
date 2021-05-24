import requests
import json
import xml.etree.ElementTree
import token
token = token.tokenMoodle

#core_enrol_get_enrolled_users
#core_enrol_get_enrolled_users
url = 'http://54.237.179.112/moodle/webservice/rest/server.php?wstoken={0}'.format(token) #&moodlewsformat=json
#http://54.237.179.112/moodle/webservice/rest/server.php?wstoken=2286427f5478b825c9a858a25b5baed7&wsfunction=core_enrol_get_enrolled_users&moodlewsrestformat=json&courseid=2
def verification_to_moodle(emailTelegram, userrole):
    function = 'core_enrol_get_enrolled_users'
    verify_url = url+"&wsfunction={0}{1}".format(function, "&moodlewsrestformat=json")
    cources = "courseid=2"
    response = json.loads(requests.post(verify_url, params=cources).content)
    print(response)
    for user in response:
        if user["email"]==emailTelegram:
            for role in user["roles"]:
                if role["roleid"]==3 or role["roleid"]==4:
                    userrole[0]=2
                elif role["roleid"]==5:
                    userrole[0] = 1
                else:
                    userrole[0] = 0
    #print(response)
    #print(response[0]["email"])
    #print(response[0]["roles"])
    #print(userrole)

def get_course_info():
    function = 'core_course_get_courses_by_field'
    verify_url = url + "&wsfunction={0}{1}".format(function, "&moodlewsrestformat=json")
    #id = "courseid=2"
    field = "field=id&value=2"
    #value = "2"
    answer=requests.post(verify_url, params=field).content
    #print(answer)
    response = json.loads(answer)
    return response["courses"][0]["fullname"], response["courses"][0]["summary"]
    #print(response["courses"][0]["summary"])

def get_tasks():
    function = "mod_assign_get_assignments"
    field = "courseids[0]=2"
    labs = dict()
    verify_url = url + "&wsfunction={0}{1}".format(function, "&moodlewsrestformat=json")
    answer = requests.post(verify_url, params=field).content
    # print(answer)
    response = json.loads(answer)
    # print(response)
    for course in response["courses"]:
        if course["id"] == 2:
            for lab in course["assignments"]:
                labs.update({lab["id"]: lab["name"]})
    return labs

def get_grades(id):
    labs=get_tasks()
    function="mod_assign_get_grades"
    field = ""
    i=0
    for key,value in labs.items():
        field+="&assignmentids["+str(i)+"]="+str(key)
        i+=1
    #assignmentids[0]= int
    verify_url = url + "&wsfunction={0}{1}".format(function, "&moodlewsrestformat=json")
    answer = requests.post(verify_url, params=field).content
    print(answer)
    response = json.loads(answer)
    gradesText=""
    for assignment in response["assignments"]:
        gradesText+=labs[assignment["assignmentid"]] + ": "
        check=True
        for grade in assignment["grades"]:
            if grade["userid"]==id:
                check=False
                gradesText+=("*%.2f*" % float(grade["grade"]))+ " балів\n"
        if check:
                gradesText +="*0* балів\n"
        #print(assignment)
    for assignment in response["warnings"]:
            gradesText += labs[assignment["itemid"]]+": *0* балів\n"
    print(gradesText)
    #print(response)
    return gradesText





    #tree = xml.etree.ElementTree.fromstring(str(response.content).replace("b'", ""))
   # root = tree.getroot()
    #list=re.findall(r"<VALUE>.*@.*</VALUE>", str(response.content))
    #print(list)

    #for elem in root.findall('email'):
        #title = elem.find('KEY')
       # if 'email' in title.attrib:
