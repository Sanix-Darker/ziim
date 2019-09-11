import axios from 'axios'

LIST_JSON_PATH = "../list.json"
MAX_RESULT = 2
MAX_RESPONSES_PER_LINK = 3

class bcolors{

    constructor(){
        this.HEADER = '\033[95m';
        this.OKBLUE = '\033[94m';
        this.OKGREEN = '\033[92m';
        this.WARNING = '\033[93m';
        this.FAIL = '\033[91m';
        this.ENDC = '\033[0m';
        this.BOLD = '\033[1m';
        this.UNDERLINE = '\033[4m';
    }
}

// console.log bcolors.WARNING + "Warning: No active frommets remain. Continue?" 
//       + bcolors.ENDC

class Zeus{
    constructor(lang = "Python", specific_link=[], search_level = 0){
        /**
            Keyword Arguments:
                specific_link {list} -- [list of specific link, where to find] (functionault: {[]})
                search_level {int} -- [The level of searching results going from 0 to 5] (functionault: {0})
         */
        this.lang = lang
        this.specific_link = specific_link
        this.search_level = search_level
    };


    printlogResult(this, solutions){
        /**
        A function that return the result of solutions around the web

        Keyword Arguments:
            solutions {list} -- [The list of solutions fetched] (functionault: {""})
         */

    }

        choice = 0
        console.log("\n\n[+] -----------------")
        count_sol = 1
        solutions.forEach((sol) => {
            console.log(bcolors.BOLD + "[+] "+str(count_sol)+"-) "+sol["title"]+" ("+str(sol["all_count"])+" / "+str(sol["result_count"])+")" + bcolors.ENDC)
            count_sol += 1
        });

        console.log(bcolors.FAIL + "[+] 0-) To stop" + bcolors.ENDC)
        console.log("[+] ------------------------")
        const readline = require('readline');

        const rl = readline.createInterface({
          input: process.stdin,
          output: process.stdout
        });

        rl.question(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC, (answer) => {
          choice = answer
          rl.close();
        });
        if (choice == 0){
            return;
        }

        try:
            choice2 = 0
            while(choice2 == 0):
                selected = solutions[choice-1]
                console.log("\n\n[+] -----------------")
                console.log(bcolors.HEADER + "[+] On "+selected["title"]+"\n" + bcolors.ENDC)
                count_selected = 1
                for select in selected["result_list"]:
                    console.log(bcolors.BOLD + "[+] "+str(count_selected)+"-) "+select["title"]+" ("+str(select["answers"])+" answers, "+str(select["votes"])+" votes)" + bcolors.ENDC)
                    count_selected += 1
                console.log(bcolors.FAIL + "[+] 0-) To Back" + bcolors.ENDC)
                console.log("[+] ------------------------")
                choice2 = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))

                try:
                    if(choice2 == 0):
                        console.log("\n\n[+] -----------------")
                        count_sol = 1
                        for sol in solutions:
                            console.log(bcolors.BOLD + "[+] "+str(count_sol)+"-) "+sol["title"]+" ("+str(sol["all_count"])+" / "+str(sol["result_count"])+")" + bcolors.ENDC)
                            count_sol += 1
                        console.log(bcolors.FAIL + "[+] 0-) To stop" + bcolors.ENDC)
                        console.log("[+] ------------------------")
                        choice2 = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))
                        if choice2 == 0:
                            exit()

                    console.log("\n\n[+] -----------------")
                    console.log(bcolors.HEADER + "[+] On "+selected["title"] + bcolors.ENDC)
                    console.log("[+] > Title : '"+selected["result_list"][choice2-1]["title"]+"'")
                    console.log("[+] > Link : '"+selected["result_list"][choice2-1]["link"]+"'")

                    if len(selected["result_list"][choice2-1]["solve_response"]) > 4:
                        console.log(bcolors.OKGREEN + "[+] > Solution : ")
                        console.log("[+] ===================================================================================================")
                        console.log("[+] ---------------------------------------------------------------------------------------------------")
                        console.log(selected["result_list"][choice2-1]["solve_response"].replace("\n", "\n[+] "))
                        console.log("[+] ---------------------------------------------------------------------------------------------------")
                        console.log("[+] ===================================================================================================" + bcolors.ENDC)
                    else:
                        console.log(bcolors.FAIL + "{ Any Solution was approve for this question }" + bcolors.ENDC)

                    // We check first if the numper of all others responses
                    if len(selected["result_list"][choice2-1]["responses"]) > 0:
                        getall = str(input(bcolors.WARNING + "[+] Do you want to get all responses ? (Y/N) :" + bcolors.ENDC)).lower()
                        try:
                            if getall == "y":
                                console.log("[+] > Others responses :")
                                console.log("\n[+] -")
                                respp_count = 1
                                for respp in selected["result_list"][choice2-1]["responses"]:
                                    console.log("[+] ```````````````````````````````````````````````````````````````````````````````````````")
                                    console.log(bcolors.BOLD + "[+] "+str(respp_count)+"-) "+str(respp["votes"])+"Votes" + bcolors.ENDC)
                                    console.log("[+] ```````````````````````````````````````````````````````````````````````````````````````")
                                    console.log("[+] "+respp["content"].replace("\n", "\n[+] \t"))
                                    respp_count += 1
                                console.log("[+] -\n")
                        except Exception as es:
                            pass

                    entire_content = str(input(bcolors.WARNING + "[+] Do you want to see the entire question ? (Y/N) :" + bcolors.ENDC)).lower()
                    try:
                        if entire_content == "y":
                            console.log("[+] > Content :\n--------------------------\n '"+selected["result_list"][choice2-1]["content"]+"'\n--------------------------\n")
                    except Exception as es:
                        pass

                    console.log(bcolors.FAIL + "[+] 0-) To Back" + bcolors.ENDC)
                    console.log(bcolors.FAIL + "[+] 99-) To Exit" + bcolors.ENDC)
                    console.log("[+] ------------------------")
                    choice2 = int(input(bcolors.WARNING + "[+] Choose available options: " + bcolors.ENDC))
                    if choice2 == 99:
                        exit()
                except Exception as es:
                    console.log(es)

        except Exception as es:
            console.log(es)


}








    function go(this, error):
        global MAX_RESULT
        global MAX_RESPONSES_PER_LINK
        """
        A function that return the result of solutions around the web

        Keyword Arguments:
            error {str} -- [The error message] (functionault: {""})
        """
        console.log(bcolors.OKGREEN + "[+] ---------------------------------------------------------------------"+ bcolors.ENDC)
        console.log(bcolors.OKGREEN + "[+] |__  /___ _   _ ___  "+ bcolors.ENDC)
        console.log(bcolors.OKGREEN + "[+]   / // _ \ | | / __|"+ bcolors.ENDC)
        console.log(bcolors.OKGREEN + "[+]  / /|  __/ |_| \__ \\"+ bcolors.ENDC)
        console.log(bcolors.OKGREEN + "[+] /____\___|\__,_|___/ by S@n1x-d4rk3r (github.com/sanix-darker)"+ bcolors.ENDC)
        console.log(bcolors.OKGREEN + "[+] ---------------------------------------------------------------------"+ bcolors.ENDC)
        checking_message = "\r[+] Checking available solution(s) online, level("+str(this.search_level)+")."
        console.log(checking_message, end="")

        MAX_RESULT += this.search_level
        MAX_RESPONSES_PER_LINK += this.search_level

        error = this.lang+" "+str(error)
        with open(LIST_JSON_PATH, "r") as file_:
            JSONArray = json.loads(file_.read())
            solutions = []
            for JSONObj in JSONArray:

                checking_message += "."
                console.log(checking_message, end="")

                search_link = JSONObj['search_link'].replace("[z]", error.replace(" ", JSONObj['space_replacement']))
                r = requests.get(search_link)
                if r.status_code == 200:

                    checking_message += "."
                    console.log(checking_message, end="")
                    tree = html.fromstring(r.content)
                    titles = tree.xpath(JSONObj['each']['title'])
                    result_list = []
                    i = 0
                    for elt in titles:
                        checking_message += "."
                        console.log(checking_message, end="")
                        link = tree.xpath(JSONObj['each']['link'])[i]

                        content = ""
                        try: content = ''.join(tree.xpath(JSONObj['each']['content']))
                        except Exception as es: pass

                        if("://" not in link) :
                            link = JSONObj['link'] + link
                        source = requests.get(link)
                        // The tree2 for sub-requests
                        tree2 = html.fromstring(source.content)

                        to_append =  {
                            "title": elt,
                            "link": link,
                            "content":content
                        }

                        // Getting the solution
                        to_append["solve_response"] = ""
                        try: to_append["solve_response"] = ''.join(tree2.xpath(JSONObj['solve_response'])[0].xpath('.//text()'))
                        except Exception as es: pass

                        // Getting the number of answers
                        to_append["answers"] = 0
                        try: to_append["answers"] = int(tree.xpath(JSONObj['each']['answers'])[i])
                        except Exception as es: pass

                        // Getting the number of votes
                        to_append["votes"] = 0
                        try: to_append["votes"] = int(tree.xpath(JSONObj['each']['votes'])[i])
                        except Exception as es: pass

                        // Getting the list of all response
                        responses_content = []
                        responses_count = 0
                        for rep in tree2.xpath(JSONObj['responses']):
                            // On recuperes uniquement des elements qui ne sont pas de la reponse
                            if ''.join(rep.xpath('.//text()')) != to_append["solve_response"] :
                                votes_per_response = 0
                                try: votes_per_response = int(tree2.xpath(JSONObj['responses_vote'])[responses_count])
                                except Exception as es: pass
                                responses_content.append( { "votes": votes_per_response, "content":''.join(rep.xpath('.//text()'))})
                            responses_count += 1
                            if responses_count == MAX_RESPONSES_PER_LINK:
                                break
                        // Adding in the to_append
                        to_append["responses"] = responses_content

                        result_list.append(to_append)
                        i += 1
                        if i == MAX_RESULT:
                            break

                    checking_message += "."
                    console.log(checking_message, end="")

                    result_count = len(titles)
                    all_count = i
                    solutions.append( {
                        "title": JSONObj['title'],
                        "result_count": result_count,
                        "all_count": all_count,
                        "result_list": result_list
                    })
            this.printlogResult( solutions )