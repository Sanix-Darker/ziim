data = [
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
    },
    {
        "title":"Quora [AJAX] not handle",
        "link":"https://www.quora.com",
        "search_link":"https://www.quora.com/search?q=[z]",
        "space_replacement": "+",
        "each":{
            "title": "//div[@class='QueryResults']//span[@class='ui_qtext_rendered_qtext']/text()",
            "link": "//div[@class='QueryResults']//a[@class='question_link']/@href",
            "content": "//div[@class='QueryResults']//div[contains(@class, 'truncated_q_text')]//text()",
            "answers": "//div[@class='nothing-yet']/text()",
            "votes": "//div[@class='nothing-yet']/text()"
        },
        "responses":"//div[contains(@class, 'postText')]",
        "responses_vote":"//div[@class='nothing-yet']/text()",
        "solve_response":"//div[@class='nothing-yet']"
    },
    {
        "title":"SitePoint [AJAX] not handle",
        "link":"https://www.sitepoint.com",
        "search_link":"https://www.sitepoint.com/community/search?q=[z]",
        "space_replacement": "%20",
        "each":{
            "title": "//span[contains(@class, 'topic-title')]//span[@class='ember-view']/text()",
            "link": "//a[contains(@class, 'search-link')]/@href",
            "content": "//div[contains(@class, 'blurb')]//text()",
            "answers": "//div[@class='nothing-yet']/text()",
            "votes": "//div[@class='nothing-yet']/text()"
        },
        "responses":"//div[@class='text']",
        "responses_vote":"//div[@class='nothing-yet']/text()",
        "solve_response":"//div[@itemprop='acceptedAnswer']"
    }
]