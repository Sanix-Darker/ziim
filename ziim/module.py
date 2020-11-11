import json
import requests
from lxml import html
from sys import exit, argv
from subprocess import Popen, PIPE, STDOUT


list_json = [
    {
        "title":"StackOverflow",
        "link":"https://stackoverflow.com",
        "search_link":"https://stackoverflow.com/search?q=[z]",
        "space_replacement": "+",
        "each":{
            "title": "//div[@class='result-link']//h3//a/@title",
            "link": "//div[@class='result-link']//h3//a/@href",
            "content": "//div[contains(@class, 'summary')]//div[contains(@class, 'excerpt')]//text()",
            "answers": "//div[@class='stats']//div[contains(@class, 'status')]//strong/text()",
            "votes": "//div[@class='stats']//div[contains(@class, 'vote')]//div[contains(@class, 'votes')]//span[contains(@class, 'vote-count-post')]//strong/text()"
        },
        "responses":"//div[@id='answers']//div[contains(@class, 'answer')]//div[contains(@class, 'post-text')]",
        "responses_vote":"//div[@id='answers']//div[contains(@class, 'votecell')]//div[contains(@class, 'vote-count')]/@data-value",
        "solve_response":"//div[@id='answers']//div[contains(@class, 'accepted-answer')]//div[contains(@class, 'post-text')]"
    },
    {
        "title":"StackExchange",
        "link":"https://stackexchange.com",
        "search_link":"https://stackexchange.com/search?q=[z]",
        "space_replacement": "+",
        "each":{
            "title": "//div[@class='result-link']//span//a/text()",
            "link": "//div[@class='result-link']//span//a/@href",
            "content": "//div[contains(@class, 'summary')]//div[contains(@class, 'excerpt')]//text()",
            "answers": "//div[@class='nothing-yet']/text()",
            "votes": "//div[@class='nothing-yet']/text()"
        },
        "responses":"//div[@id='answers']//div[contains(@class, 'answer')]//div[contains(@class, 'post-text')]",
        "responses_vote":"//div[@id='answers']//div[contains(@class, 'votecell')]//div[contains(@class, 'vote-count')]/@data-value",
        "solve_response":"//div[@id='answers']//div[contains(@class, 'accepted-answer')]//div[contains(@class, 'post-text')]"
    },
    {
        "title":"CodeProject",
        "link":"https://www.codeproject.com",
        "search_link":"https://www.codeproject.com/search.aspx?q=[z]&doctypeid=4",
        "space_replacement": "+",
        "each":{
            "title": "//div[contains(@class, 'content-list-item')]//div[@class='entry']//span[@class='title']//a/text()",
            "link": "//div[contains(@class, 'content-list-item')]//div[@class='entry']//span[@class='title']//a/@href",
            "content": "//div[contains(@class, 'summary')]//text()",
            "answers": "//div[@class='nothing-yet']/text()",
            "votes": "//div[@class='nothing-yet']/text()"
        },
        "responses":"//div[@class='text']",
        "responses_vote":"//div[@class='nothing-yet']/text()",
        "solve_response":"//div[@itemprop='acceptedAnswer']"
    },
    {
        "title":"CodeRanch",
        "link":"https://coderanch.com",
        "search_link":"https://coderanch.com/forums/search/search/-1?match_type=all&sort_by=time&groupByTopic=true&q=[z]",
        "space_replacement": "+",
        "each":{
            "title": "//div[@class='topicinfoheader']//div[@class='subjectsection']//a[@class='subject']/text()",
            "link": "//div[@class='topicinfoheader']//div[@class='subjectsection']//a[@class='subject']/@href",
            "content": "//div[contains(@class, 'posts')]//td[contains(@class, 'row1')]//text()",
            "answers": "//div[@class='nothing-yet']/text()",
            "votes": "//div[@class='nothing-yet']/text()"
        },
        "responses":"//div[contains(@class, 'postText')]",
        "responses_vote":"//div[@class='nothing-yet']/text()",
        "solve_response":"//div[@class='nothing-yet']"
    },
    {
        "title":"Reddit [language/topic]",
        "link":"https://www.reddit.com",
        "search_link":"https://www.reddit.com/r/[t]/search/?q=[z]&restrict_sr=1",
        "space_replacement": "%20",
        "each":{
            "title": "//div[@class='SubredditVars-r-javascript']//h3//text()",
            "link": "//div[@class='topicinfoheader']//div[@class='subjectsection']//a[@class='subject']/@href",
            "content": "//div[contains(@class, 'posts')]//td[contains(@class, 'row1')]//text()",
            "answers": "//div[@class='nothing-yet']/text()",
            "votes": "//div[@class='nothing-yet']/text()"
        },
        "responses":"//div[contains(@class, 'postText')]",
        "responses_vote":"//div[@class='nothing-yet']/text()",
        "solve_response":"//div[@class='nothing-yet']"
    }
]


# MAX_RESULT = 2
# MAX_RESPONSES_PER_LINK = 3

class Bcolors:
    """
    Just some color for the terminal
    """
    HEADER = '\033[95m'  # rose
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'  # jaune
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


bcs = Bcolors


class Ziim:

    def __init__(self, _type="Python"):  # search_level = 0
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
        """
        A simple function for the header of Ziim
        """
        print(bcs.OKGREEN + "[+] ---------------------------------------------------------------------" + bcs.ENDC)
        print(bcs.OKGREEN + "[+]  ______ _            " + bcs.ENDC)
        print(bcs.OKGREEN + "[+] |__  (_|_)_ __ ___   " + bcs.ENDC)
        print(bcs.OKGREEN + "[+]   / /| | | '_ ` _ \\  [" + self._type + "] version." + bcs.ENDC)
        print(bcs.OKGREEN + "[+]  / /_| | | | | | | | This tool find your exception online for you." + bcs.ENDC)
        print(bcs.OKGREEN + "[+] /____|_|_|_| |_| |_| Made by S@n1x-d4rk3r (github.com/sanix-darker/ziim)" + bcs.ENDC)
        print(bcs.OKGREEN + "[+] ---------------------------------------------------------------------" + bcs.ENDC)

    def zm(self, command):
        try:
            proc = Popen(command.split(" "), stdout=PIPE, stderr=STDOUT)
            output = proc.communicate()[0].decode('utf-8')
            print(output)
            error = Ziim().remove2points(output)
            if len(error) > 1:
                Ziim().go(error)
        except KeyboardInterrupt:
            print("Thank you using ziim-cli")
            exit()

    def remove2points(self, output):
        for lign in str(output).split("\n"):
            if "Err" in lign or "Exception" in lign:
                return lign.split(":")[1]
        return ""

    def choose_from_answer(self, solutions, ch):
        """
        This method takes solutions as JSON element and present their
            titles as option, when you choose, you have the solution
            per title and other responses

        Arguments:
            solutions
            ch
        """
        selected = solutions[ch - 1]
        print("\n\n[+] -----------------")
        print(bcs.HEADER + "[+] On " + selected["title"] + "\n" + bcs.ENDC)
        for (count_selected, select) in enumerate(selected["result_list"]):
            print(bcs.BOLD + "[+] " + str(count_selected + 1) + "-) " + str(select["title"]) + " (" + str(
                select["answers"]) + " answers, " + str(select["votes"]) + " votes)" + bcs.ENDC)
        print(bcs.FAIL + "[+] 0-) To Back" + bcs.ENDC)
        print(bcs.FAIL + "[+] 99-) To Exit" + bcs.ENDC)
        print("[+] ------------------------")
        choice2 = int(input(bcs.WARNING + "[+] Choose available options: " + bcs.ENDC))

        try:
            if choice2 == 99:
                exit()
            if choice2 == 0:
                self.printResult(solutions)

            print("\n\n[+] -----------------")
            print(bcs.HEADER + "[+] > Forum : " + selected["title"] + bcs.ENDC)
            print("[+] > Title : '" + selected["result_list"][choice2 - 1]["title"] + "'")
            print("[+] > Link : '" + selected["result_list"][choice2 - 1]["link"] + "'")

            if len(selected["result_list"][choice2 - 1]["solve_response"]) > 4:
                print(bcs.OKGREEN + "[+] > Solution : ")
                print("[+] "
                      "----------------------------------------------------------------\
                      -----------------------------------")
                print(selected["result_list"][choice2 - 1]["solve_response"].replace("\n", "\n[+] \t"))
                print("[+] \
                        --------------------------------------------------------------\
                        -------------------------------------" + bcs.ENDC)
            else:
                print(bcs.FAIL + "[+] { Any Solution was approve for this question }" + bcs.ENDC)

            self.responses_entireQuestion(selected, solutions, choice2, ch)

            print(bcs.FAIL + "[+] 0-) To Back" + bcs.ENDC)
            print(bcs.FAIL + "[+] 99-) To Exit" + bcs.ENDC)
            print("[+] ------------------------")
            choice2 = int(input(bcs.WARNING + "[+] Choose available options: " + bcs.ENDC))
            if choice2 == 99:
                exit()
            if choice2 == 0:
                self.choose_from_answer(solutions, ch)
        except Exception as es:
            print(es)

    def responses_entireQuestion(self, selected, solutions, choice2, ch):
        """
        This method proposes if the user want all responses then
            ask if he want to see the whole body of the question

        Arguments:
            selected
            solutions
            choice2
            ch
        """
        # We check first if the numper of all others responses
        if len(selected["result_list"][choice2 - 1]["responses"]) > 0:
            getall = str(input(bcs.WARNING + "[+] Get all other responses(" + str(len(
                selected["result_list"][choice2 - 1][
                    "responses"])) + ") ? [ Y / N / 0(To go back) ] :" + bcs.ENDC)).lower()

            try:
                if "y" in getall:
                    print("[+] > Others responses :")
                    print("\n[+] -")
                    for (respp_count, respp) in enumerate(selected["result_list"][choice2 - 1]["responses"]):
                        print(
                            "[+] \
                            ```````````````````````````````````````````````````````````````````````````````````````")
                        print(bcs.BOLD + "[+] " + str(respp_count + 1) + "-) " + str(
                            respp["votes"]) + "Votes" + bcs.ENDC)
                        print(
                            "[+] \
                            ```````````````````````````````````````````````````````````````````````````````````````")
                        print("[+] " + respp["content"].replace("\n", "\n[+] \t") + "[+] -\n")
                elif "0" in getall:
                    self.choose_from_answer(solutions, ch)
            except Exception as es:
                print(es)
                self.responses_entireQuestion(selected, solutions, choice2, ch)
        else:
            print(bcs.FAIL + "[+] Any other responses for this question." + bcs.ENDC)

        entire_content = str(input(
            bcs.WARNING + "[+] Get the entire question ?  [ Y / N / 0(To go back) ] :" + bcs.ENDC)).lower()
        try:
            if "y" in entire_content:
                print("[+] > Content :")
                print(
                    "[+] ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
                    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                print((selected["result_list"][choice2 - 1]["content"]).replace("\n", "\n[+] \t"))
                print(
                    "[+] |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\
                    ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            elif "0" in entire_content:
                self.choose_from_answer(solutions, ch)
        except Exception as es:
            print(es)
            self.responses_entireQuestion(selected, solutions, choice2, ch)

    def printResult(self, solutions):
        """
        A function that return the result of solutions around the web

        Arguments:
            solutions {[list]} -- [The list of solutions fetched]
        """
        choice = 0
        # We check if it's only one solution no need this step on listing just one solution
        if len(solutions) > 1:
            print("\n\n[+] -----------------")
            for (count_sol, sol) in enumerate(solutions):
                print(bcs.BOLD + "[+] " + str(count_sol + 1) + "-) " + sol["title"] + " (" + str(
                    sol["all_count"]) + ")" + bcs.ENDC)
            # print(bcs.BOLD + "[+] 88-) ["+str(self.search_level)+"] Change the search level(0-10)" + bcs.ENDC)
            print(bcs.FAIL + "[+] 0-) To stop" + bcs.ENDC)
            print("[+] ------------------------")
            choice = int(input(bcs.WARNING + "[+] Choose available options: " + bcs.ENDC))
        else:
            choice = 1

        if choice == 0:
            exit()
        # if choice == 88:
        #     self.search_level = int(input(bcs.WARNING + "[+] Choose the search level: " + bcs.ENDC))
        #     self.go(self.error)

        try:
            # if the choice is 0 then the checkpoint 2 will loop
            self.choose_from_answer(solutions, choice)
        except Exception as es:
            print(es)

    def buildResultList(self, elt, link, tree, JSONObj, i):
        """
        This method will generate a map of responses per links
        This method have the role on building the result_list

        Arguments:
            elt {[type]} -- [element from the array of titles]
            link {[str]} -- [The link]
            content {[str]} -- [The content of the question]
            tree
            tree2
            JSONObj
        """
        content = ""
        try:
            content = ''.join(tree.xpath(JSONObj['each']['content']))
        except Exception as es:
            pass

        if "://" not in link and "www." not in link:
            link = JSONObj['link'] + link
        source = requests.get(link)
        # The tree2 for sub-requests
        tree2 = html.fromstring(source.content)

        to_append = {"title": elt, "link": link, "content": content, "solve_response": ""}
        # Getting the solution
        try:
            to_append["solve_response"] = ''.join(tree2.xpath(JSONObj['solve_response'])[0].xpath('.//text()'))
        except Exception as es:
            pass

        # Getting the number of answers
        to_append["answers"] = 0
        try:
            to_append["answers"] = int(tree.xpath(JSONObj['each']['answers'])[i])
        except Exception as es:
            pass

        # Getting the number of votes
        to_append["votes"] = 0
        try:
            to_append["votes"] = int(tree.xpath(JSONObj['each']['votes'])[i])
        except Exception as es:
            pass

        # Getting the list of all response
        responses_content = []
        for responses_count, rep in enumerate(tree2.xpath(JSONObj['responses'])):
            # On recuperes uniquement des elements qui ne sont pas de la reponse
            if ''.join(rep.xpath('.//text()')) != to_append["solve_response"]:
                votes_per_response = 0
                try:
                    votes_per_response = int(tree2.xpath(JSONObj['responses_vote'])[responses_count])
                except Exception as es:
                    pass
                responses_content.append({"votes": votes_per_response, "content": ''.join(rep.xpath('.//text()'))})
            # if responses_count == MAX_RESPONSES_PER_LINK: break
        # Adding in the to_append
        to_append["responses"] = responses_content
        return to_append

    def checking_message_method(self):
        """
        This method will only print the waiting message
        """
        self.checking_message += "."
        return self.checking_message

    def wainting(self):
        """
        This method have the only role on printing point to wait
        """
        print(self.checking_message_method(), end="")

    def replaceSPECIALCARACTER(self, __string):
        """
        Remove spcial character form the error text search

        Arguments:
            __string
        """
        return __string.replace("'", "").replace('"', '').replace('@', '')

    def fetch_results_per_link(self, search_link, JSONObj):
        """
        Per link given, this method will fetchs responses, the whole questions,
            and the solution

        Arguments:
            search_link
            JSONObj

        Returns:
            [type] -- [description]
        """
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
                        link = "http://" + link.split("//")[1]

                try:
                    result_list.append(self.buildResultList(elt, link, tree, JSONObj, i))
                except Exception as es:
                    print(es)
                    self.go(self.error)
                # if i == MAX_RESULT: break

            return True, result_list, titles, len(titles) - 1
        else:
            return False, [], [], 0

    def go(self, error):
        """
        # ? go method
        # ! The Main method that take the eror and proceed
        A function that return the result of solutions around the web

        Keyword Arguments:
            error {str} -- [The error message] (default: {""})
        """
        try:
            # global MAX_RESULT
            # global MAX_RESPONSES_PER_LINK

            if not self.presentation_shows:
                self.presentation()
                self.presentation_shows = True

            # MAX_RESULT += self.search_level
            # MAX_RESPONSES_PER_LINK += self.search_level

            self.error = str(error).split("\n")[-1]
            print("[+] The Error is " + bcs.FAIL + ":::" + self.error + ":::" + bcs.ENDC)
            # with open(LIST_JSON_PATH, "r") as file_:
            JSONArray = list_json
            solutions = []
            self.checking_message = "\r[+] Checking available solution(s) online"
            print("[+] Where do you want to find solutions: ")
            for (solution_count, JSONObj) in enumerate(JSONArray):
                print(bcs.BOLD + "[+] " + str(solution_count + 1) + "-) " + str(JSONObj["title"]) + bcs.ENDC)

            thechoice = "1"
            try:
                thechoice = input(
                    bcs.WARNING + "[+] (Ex: 1 or Ex: 1,2,3 or press ENTER (Default is stackOverFlow))"
                                  "\n[+] Your Choice: " + bcs.ENDC)
                if thechoice == "": thechoice = "1"
            except Exception as es:
                pass

            selected_choice = thechoice.split(",")

            self.wainting()
            for o in range(0, len(selected_choice)):
                JSONObj = JSONArray[int(selected_choice[o]) - 1]

                self.wainting()
                # Removing special characters
                search_link = self.replaceSPECIALCARACTER(
                    JSONObj['search_link'].replace("[z]", self.error.replace(" ", JSONObj['space_replacement'])))

                resultlist_fetched = self.fetch_results_per_link(search_link, JSONObj)
                titles = resultlist_fetched[2]
                self.wainting()
                result_count = len(titles)
                all_count = resultlist_fetched[3]
                solutions.append({
                    "title": JSONObj['title'],
                    "result_count": result_count,
                    "all_count": all_count,
                    "result_list": resultlist_fetched[1]
                })
            self.printResult(solutions)
        except Exception as es:
            print(es)


def main():
    # we delete the first argument
    del argv[0]
    # We execute the zm method
    Ziim().zm(' '.join(argv))


if __name__ == "__main__":
    main()
