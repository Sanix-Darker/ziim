import json

from lxml import html, etree
import requests
from sys import exit

LIST_JSON_PATH = "../list.json"
MAX_RESULT = 2
MAX_RESPONSES_PER_LINK = 3

class bcolors:
    HEADER = '\033[95m' # rose
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # jaune
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# print bcolors.WARNING + "Warning: No active frommets remain. Continue?" 
#       + bcolors.ENDC

class Zeus:

    def __init__(self, lang = "Python", search_level = 0):
        """
        Keyword Arguments:
            search_level {int} -- [The level of searching results going from 0 to 5] (default: {0})
        """
        self.lang = lang
        self.search_level = search_level

    def presentation(self):
        """
        A simple function for the header of Zeus
        """
        print(bcolors.OKGREEN + "[+] ---------------------------------------------------------------------"+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+] |__  /___ _   _ ___  "+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+]   / // _ \ | | / __|"+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+]  / /|  __/ |_| \__ \\ This tool find your exception online for you."+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+] /____\___|\__,_|___/ Made by S@n1x-d4rk3r (github.com/sanix-darker)"+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+] ---------------------------------------------------------------------"+ bcolors.ENDC)

    def printResult(self, solutions):
        """
        A function that return the result of solutions around the web

        Keyword Arguments:
            solutions {list} -- [The list of solutions fetched] (default: {""})
        """
        choice = 0
        print("\n\n[+] -----------------")
        count_sol = 1
        for sol in solutions:
            print(bcolors.BOLD + "[+] "+str(count_sol)+"-) "+sol["title"]+" ("+str(sol["all_count"])+" / "+str(sol["result_count"])+")" + bcolors.ENDC)
            count_sol += 1
        print(bcolors.FAIL + "[+] 0-) To stop" + bcolors.ENDC)
        print("[+] ------------------------")
        choice = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))
        if choice == 0:
            exit()

        try:
            choice2 = 0
            while(choice2 == 0):
                selected = solutions[choice-1]
                print("\n\n[+] -----------------")
                print(bcolors.HEADER + "[+] On "+selected["title"]+"\n" + bcolors.ENDC)
                count_selected = 1
                for select in selected["result_list"]:
                    print(bcolors.BOLD + "[+] "+str(count_selected)+"-) "+str(select["title"])+" ("+str(select["answers"])+" answers, "+str(select["votes"])+" votes)" + bcolors.ENDC)
                    count_selected += 1
                print(bcolors.FAIL + "[+] 0-) To Back" + bcolors.ENDC)
                print("[+] ------------------------")
                choice2 = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))

                try:
                    if(choice2 == 0):
                        self.printResult(solutions)

                    print("\n\n[+] -----------------")
                    print(bcolors.HEADER + "[+] On "+selected["title"] + bcolors.ENDC)
                    print("[+] > Title : '"+selected["result_list"][choice2-1]["title"]+"'")
                    print("[+] > Link : '"+selected["result_list"][choice2-1]["link"]+"'")

                    if len(selected["result_list"][choice2-1]["solve_response"]) > 4:
                        print(bcolors.OKGREEN + "[+] > Solution : ")
                        print("[+] ===================================================================================================")
                        print("[+] ---------------------------------------------------------------------------------------------------")
                        print(selected["result_list"][choice2-1]["solve_response"].replace("\n", "\n[+] "))
                        print("[+] ---------------------------------------------------------------------------------------------------")
                        print("[+] ===================================================================================================" + bcolors.ENDC)
                    else:
                        print(bcolors.FAIL + "{ Any Solution was approve for this question }" + bcolors.ENDC)

                    # We check first if the numper of all others responses
                    if len(selected["result_list"][choice2-1]["responses"]) > 0:
                        getall = str(input(bcolors.WARNING + "[+] Do you want to get all responses ? (Y/N) :" + bcolors.ENDC)).lower()
                        try:
                            if getall == "y":
                                print("[+] > Others responses :")
                                print("\n[+] -")
                                respp_count = 1
                                for respp in selected["result_list"][choice2-1]["responses"]:
                                    print("[+] ```````````````````````````````````````````````````````````````````````````````````````")
                                    print(bcolors.BOLD + "[+] "+str(respp_count)+"-) "+str(respp["votes"])+"Votes" + bcolors.ENDC)
                                    print("[+] ```````````````````````````````````````````````````````````````````````````````````````")
                                    print("[+] "+respp["content"].replace("\n", "\n[+] \t"))
                                    respp_count += 1
                                print("[+] -\n")
                        except Exception as es:
                            pass

                    entire_content = str(input(bcolors.WARNING + "[+] Do you want to see the entire question ? (Y/N) :" + bcolors.ENDC)).lower()
                    try:
                        if entire_content == "y":
                            print("[+] > Content :\n--------------------------\n '"+selected["result_list"][choice2-1]["content"]+"'\n--------------------------\n")
                    except Exception as es:
                        pass

                    print(bcolors.FAIL + "[+] 0-) To Back" + bcolors.ENDC)
                    print(bcolors.FAIL + "[+] 99-) To Exit" + bcolors.ENDC)
                    print("[+] ------------------------")
                    choice2 = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))
                    if choice2 == 99:
                        exit()
                except Exception as es:
                    print(es)

        except Exception as es:
            print(es)


    def buildResultList(self, elt, link, tree, JSONObj, i):
        """[This method have the role on building the result_list]

        Arguments:
            elt {[type]} -- [element from the array of titles]
            link {[str]} -- [The link]
            content {[str]} -- [The content of the question]
            tree {[xpath]} -- [description]
            tree2 {[xpath]} -- [description]
            JSONObj {[json]} -- [description]
        """
        content = ""
        try: content = ''.join(tree.xpath(JSONObj['each']['content']))
        except Exception as es: pass

        if("://" not in link):
            link = JSONObj['link'] + link
        source = requests.get(link)
        # The tree2 for sub-requests
        tree2 = html.fromstring(source.content)

        to_append =  {
            "title": elt,
            "link": link,
            "content":content
        }
        # Getting the solution
        to_append["solve_response"] = ""
        try: to_append["solve_response"] = ''.join(tree2.xpath(JSONObj['solve_response'])[0].xpath('.//text()'))
        except Exception as es: pass

        # Getting the number of answers
        to_append["answers"] = 0
        try: to_append["answers"] = int(tree.xpath(JSONObj['each']['answers'])[i])
        except Exception as es: pass

        # Getting the number of votes
        to_append["votes"] = 0
        try: to_append["votes"] = int(tree.xpath(JSONObj['each']['votes'])[i])
        except Exception as es: pass

        # Getting the list of all response
        responses_content = []
        responses_count = 0
        for rep in tree2.xpath(JSONObj['responses']):
            # On recuperes uniquement des elements qui ne sont pas de la reponse
            if ''.join(rep.xpath('.//text()')) != to_append["solve_response"] :
                votes_per_response = 0
                try: votes_per_response = int(tree2.xpath(JSONObj['responses_vote'])[responses_count])
                except Exception as es: pass
                responses_content.append( { "votes": votes_per_response, "content":''.join(rep.xpath('.//text()'))})
            responses_count += 1
            if responses_count == MAX_RESPONSES_PER_LINK:
                break
        # Adding in the to_append
        to_append["responses"] = responses_content
        return to_append


    # ? go method
    # ! The Main method that take the eror and proceed
    def go(self, error):
        global MAX_RESULT
        global MAX_RESPONSES_PER_LINK
        """
        A function that return the result of solutions around the web

        Keyword Arguments:
            error {str} -- [The error message] (default: {""})
        """
        self.presentation()

        MAX_RESULT += self.search_level
        MAX_RESPONSES_PER_LINK += self.search_level

        error = self.lang+" "+str(error).split("\n")[-1]
        with open(LIST_JSON_PATH, "r") as file_:
            JSONArray = json.loads(file_.read())
            solutions = []
            print("[+] Where do you want to find solutions: ")
            solution_count = 1
            for JSONObj in JSONArray:
                print(bcolors.BOLD + "[+] "+str(solution_count)+"-) "+str(JSONObj["title"])+ bcolors.ENDC)

            thechoice = "1"
            try:
                thechoice = input(bcolors.WARNING + "[+] Choose ( Ex: 1 or Ex: 1,2,3 or press ENTER (Default is stackOverFlow)): " + bcolors.ENDC)
                if thechoice == "":
                    thechoice = "1"
            except Exception as es:
                pass

            selected_choice = thechoice.split(",")

            checking_message = "\r[+] Checking available solution(s) online, search_level("+str(self.search_level)+")."
            print(checking_message, end="")

            for o in range(0, len(selected_choice)):
                JSONObj = JSONArray[int(selected_choice[o])-1]

                checking_message += "."
                print(checking_message, end="")

                search_link = JSONObj['search_link'].replace("[z]", error.replace(" ", JSONObj['space_replacement']))
                r = requests.get(search_link)
                if r.status_code == 200:

                    checking_message += "."
                    print(checking_message, end="")
                    tree = html.fromstring(r.content)
                    titles = tree.xpath(JSONObj['each']['title'])
                    result_list = []
                    i = 0
                    for elt in titles:
                        checking_message += "."
                        print(checking_message, end="")
                        link = tree.xpath(JSONObj['each']['link'])[i]

                        to_append = self.buildResultList(elt, link, tree, JSONObj, i)
                        result_list.append(to_append)
                        i += 1
                        if i == MAX_RESULT:
                            break

                    checking_message += "."
                    print(checking_message, end="")

                    result_count = len(titles)
                    all_count = i
                    solutions.append( {
                        "title": JSONObj['title'],
                        "result_count": result_count,
                        "all_count": all_count,
                        "result_list": result_list
                    })
            self.printResult( solutions )