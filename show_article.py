import json
import sys
import requests

if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except:
        sys.exit("provide arg 1, an url to a valid source (e.g. economist-article)")
    try:
        html = requests.get(url).text
    except:
        sys.exit(f"could not curl {url}")
    try:
        article_dict_str = html.split("<script type=\"application/ld+json\">")[1].split("</script>")[0]
    except:
        sys.exit("could not split html-source as expected")
    try:
        article_dict = json.loads(article_dict_str)
    except:
        sys.exit("could not load article-json as expected")

    article_headline = article_dict["headline"]
    article_body = article_dict["articleBody"]

    print(article_headline, "\n", article_body)
