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

// On going

}