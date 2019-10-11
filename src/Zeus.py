import json

from lxml import html
import requests
from sys import exit

# The list of available webSite where to take solution
LIST_JSON_PATH = "../list.json"


# MAX_RESULT = 2
# MAX_RESPONSES_PER_LINK = 3

class bcolors:
    HEADER = '\033[95m' # rose
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # jaune
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Zeus:

    def __init__(self, _type = "Python"): # search_level = 0
        """
        Keyword Arguments:
            [REMOVED] search_level {int} -- [The level of searching results going from 0 to 5] (default: {0})
        """
        self.error = ""
        self.presentation_shows = False
        self._type = _type
        # self.search_level = search_level
        self.checking_message = "\r[+] Checking available solution(s) online"

    def presentation(self):
        """[A simple function for the header of Zeus]
        """
        print(bcolors.OKGREEN + "[+] ---------------------------------------------------------------------"+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+] |__  /___ _   _ ___  "+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+]   / // _ \ | | / __| ["+self._type+"] version."+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+]  / /|  __/ |_| \__ \\ This tool find your exception online for you."+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+] /____\___|\__,_|___/ Made by S@n1x-d4rk3r (github.com/sanix-darker)"+ bcolors.ENDC)
        print(bcolors.OKGREEN + "[+] ---------------------------------------------------------------------"+ bcolors.ENDC)


    def choose_from_answer(self, solutions, ch):
        """[summary]

        Arguments:
            solutions {[type]} -- [description]
            ch {[type]} -- [description]
        """
        selected = solutions[ch-1]
        print("\n\n[+] -----------------")
        print(bcolors.HEADER + "[+] On "+selected["title"]+"\n" + bcolors.ENDC)
        for (count_selected, select) in enumerate(selected["result_list"]):
            print(bcolors.BOLD + "[+] "+str(count_selected+1)+"-) "+str(select["title"])+" ("+str(select["answers"])+" answers, "+str(select["votes"])+" votes)" + bcolors.ENDC)
        print(bcolors.FAIL + "[+] 0-) To Back" + bcolors.ENDC)
        print(bcolors.FAIL + "[+] 99-) To Exit" + bcolors.ENDC)
        print("[+] ------------------------")
        choice2 = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))

        try:
            if(choice2 == 99): exit()
            if(choice2 == 0): self.printResult(solutions)

            print("\n\n[+] -----------------")
            print(bcolors.HEADER + "[+] > Forum : "+selected["title"] + bcolors.ENDC)
            print("[+] > Title : '"+selected["result_list"][choice2-1]["title"]+"'")
            print("[+] > Link : '"+selected["result_list"][choice2-1]["link"]+"'")

            if len(selected["result_list"][choice2-1]["solve_response"]) > 4:
                print(bcolors.OKGREEN + "[+] > Solution : ")
                print("[+] ---------------------------------------------------------------------------------------------------")
                print(selected["result_list"][choice2-1]["solve_response"].replace("\n", "\n[+] \t"))
                print("[+] ---------------------------------------------------------------------------------------------------" + bcolors.ENDC)
            else:
                print(bcolors.FAIL + "[+] { Any Solution was approve for this question }" + bcolors.ENDC)

            self.responses_entireQuestion(selected, solutions, choice2, ch)

            print(bcolors.FAIL + "[+] 0-) To Back" + bcolors.ENDC)
            print(bcolors.FAIL + "[+] 99-) To Exit" + bcolors.ENDC)
            print("[+] ------------------------")
            choice2 = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))
            if choice2 == 99: exit()
            if choice2 == 0: self.choose_from_answer(solutions, ch)
        except Exception as es: print(es)


    def responses_entireQuestion(self, selected, solutions, choice2, ch):
        """[summary]

        Arguments:
            selected {[type]} -- [description]
            solutions {[type]} -- [description]
            choice2 {[type]} -- [description]
            ch {[type]} -- [description]
        """
        # We check first if the numper of all others responses
        if len(selected["result_list"][choice2-1]["responses"]) > 0:
            getall = str(input(bcolors.WARNING + "[+] Get all other responses ? [ Y / N / 0(To go back) ] :" + bcolors.ENDC)).lower()

            try:
                if("y" in getall):
                    print("[+] > Others responses :")
                    print("\n[+] -")
                    for (respp_count, respp) in enumerate(selected["result_list"][choice2-1]["responses"]):
                        print("[+] ```````````````````````````````````````````````````````````````````````````````````````")
                        print(bcolors.BOLD + "[+] "+str(respp_count+1)+"-) "+str(respp["votes"])+"Votes" + bcolors.ENDC)
                        print("[+] ```````````````````````````````````````````````````````````````````````````````````````")
                        print("[+] "+respp["content"].replace("\n", "\n[+] \t"))
                    print("[+] -\n")
                elif ("0" in getall):
                    self.choose_from_answer(solutions, ch)
            except Exception as es:
                print(es)
                self.responses_entireQuestion(selected, solutions, choice2, ch)
        else:
            print(bcolors.FAIL + "[+] Any other responses for this question." + bcolors.ENDC)

        entire_content = str(input(bcolors.WARNING + "[+] Get the entire question ?  [ Y / N / 0(To go back) ] :" + bcolors.ENDC)).lower()
        try:
            if("y" in entire_content):
                print("[+] > Content :")
                print("[+] --------------------------|||||||||||||||||||||||||--------------------------|||||||||||||||||||||||||--------------------------|||||||||||||||||||||||||--------------------------")
                print((selected["result_list"][choice2-1]["content"]).replace("\n", "\n[+] \t"))
                print("[+] --------------------------|||||||||||||||||||||||||--------------------------|||||||||||||||||||||||||--------------------------|||||||||||||||||||||||||--------------------------")
            elif("0" in entire_content):
                self.choose_from_answer(solutions, ch)
        except Exception as es:
            print(es)
            self.responses_entireQuestion(selected, solutions, choice2, ch)


    def printResult(self, solutions):
        """[A function that return the result of solutions around the web]

        Arguments:
            solutions {[list]} -- [The list of solutions fetched]
        """
        choice = 0
        # We check if it's only one solution no need this step on listing just one solution
        if (len(solutions) > 1):
            print("\n\n[+] -----------------")
            for (count_sol, sol) in enumerate(solutions):
                print(bcolors.BOLD + "[+] "+str(count_sol+1)+"-) "+sol["title"]+" ("+str(sol["all_count"])+")" + bcolors.ENDC)
            # print(bcolors.BOLD + "[+] 88-) ["+str(self.search_level)+"] Change the search level(0-10)" + bcolors.ENDC)
            print(bcolors.FAIL + "[+] 0-) To stop" + bcolors.ENDC)
            print("[+] ------------------------")
            choice = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))
        else:
            choice = 1

        if choice == 0: exit()
        # if choice == 88:
        #     self.search_level = int(input(bcolors.WARNING + "[+] Choose the search level: " + bcolors.ENDC))
        #     self.go(self.error)

        try:
            # if the choice is 0 then the checkpoint 2 will loop
            self.choose_from_answer(solutions, choice)
        except Exception as es: print(es)


    # This method will generate a map of responses per links
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

        if("://" not in link and "www." not in link):
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
        for (responses_count, rep) in enumerate(tree2.xpath(JSONObj['responses'])):
            # On recuperes uniquement des elements qui ne sont pas de la reponse
            if ''.join(rep.xpath('.//text()')) != to_append["solve_response"] :
                votes_per_response = 0
                try: votes_per_response = int(tree2.xpath(JSONObj['responses_vote'])[responses_count])
                except Exception as es: pass
                responses_content.append( { "votes": votes_per_response, "content":''.join(rep.xpath('.//text()'))})
            # if responses_count == MAX_RESPONSES_PER_LINK: break
        # Adding in the to_append
        to_append["responses"] = responses_content
        return to_append


    # This method will only print the waiting message
    def checking_message_method(self):
        self.checking_message += "."
        return self.checking_message


    # This method have the only role on printing point to wait
    def wainting(self):
        print(self.checking_message_method(), end="")


    # Remove spcial character form the error text search
    def replaceSPECIALCARACTER(self, __string):
        return __string.replace("'", "").replace('"', '').replace('@', '')


    def fetch_results_per_link(self, search_link, JSONObj):
        r = requests.get(search_link)
        if r.status_code == 200:
            self.wainting()
            tree = html.fromstring(r.content)
            titles = tree.xpath(JSONObj['each']['title'])
            result_list = []
            for (i, elt) in enumerate(titles):
                self.wainting()
                link = tree.xpath(JSONObj['each']['link'])[i]

                if "http" not in link:
                    if JSONObj["link"] not in link and "www" not in link:
                        link = JSONObj["link"] + link
                    else:
                        link = "http://"+link.split("//")[1]

                try:
                    result_list.append(self.buildResultList(elt, link, tree, JSONObj, i))
                except Exception as es:
                    print(es)
                    self.go(self.error)
                # if i == MAX_RESULT: break

            return True, result_list, titles, len(titles)-1
        else:
            return False, [], [], 0


    # ? go method
    # ! The Main method that take the eror and proceed
    def go(self, error):
        """
        A function that return the result of solutions around the web

        Keyword Arguments:
            error {str} -- [The error message] (default: {""})
        """
        try:
            # global MAX_RESULT
            # global MAX_RESPONSES_PER_LINK

            if self.presentation_shows == False:
                self.presentation()
                self.presentation_shows = True

            # MAX_RESULT += self.search_level
            # MAX_RESPONSES_PER_LINK += self.search_level

            self.error = str(error).split("\n")[-1]
            print("[+] The Error is "+bcolors.FAIL+":::"+self.error+":::"+bcolors.ENDC)
            with open(LIST_JSON_PATH, "r") as file_:
                JSONArray = json.loads(file_.read())
                solutions = []
                self.checking_message = "\r[+] Checking available solution(s) online"
                print("[+] Where do you want to find solutions: ")
                for (solution_count, JSONObj) in enumerate(JSONArray):
                    print(bcolors.BOLD + "[+] "+str(solution_count+1)+"-) "+str(JSONObj["title"])+ bcolors.ENDC)

                thechoice = "1"
                try:
                    thechoice = input(bcolors.WARNING + "[+] (Ex: 1 or Ex: 1,2,3 or press ENTER (Default is stackOverFlow))\n[+] Your Choice: " + bcolors.ENDC)
                    if thechoice == "": thechoice = "1"
                except Exception as es: pass

                selected_choice = thechoice.split(",")

                self.wainting()
                for o in range(0, len(selected_choice)):
                    JSONObj = JSONArray[int(selected_choice[o])-1]

                    self.wainting()
                    # Removing special characters
                    search_link = self.replaceSPECIALCARACTER(JSONObj['search_link'].replace("[z]", self.error.replace(" ", JSONObj['space_replacement'])))

                    resultlist_fetched = self.fetch_results_per_link(search_link, JSONObj)
                    titles = resultlist_fetched[2]
                    self.wainting()
                    result_count = len(titles)
                    all_count = resultlist_fetched[3]
                    solutions.append( {
                        "title": JSONObj['title'],
                        "result_count": result_count,
                        "all_count": all_count,
                        "result_list": resultlist_fetched[1]
                    })
                self.printResult( solutions )
        except Exception as es:
            print("\n[+] ERROR on ZEUS, something bad happens with the selected option, check the error below:")
            print(es)