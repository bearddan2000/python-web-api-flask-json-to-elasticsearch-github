import csv, json, logging, math, requests

from model.cls_repo import Repo

logging.basicConfig(level=logging.INFO)

def get_url(url):
    headers = {'Content-Type': 'application/json' }
    logging.info(url)
    return requests.get(url, headers=headers, verify=False)

def to_json(url):
    response = get_url(url)
    logging.info("to json "+url)
    return json.loads(response.text)

def get_count():
    url = "https://api.github.com/users/bearddan2000"
    json_object = to_json(url)
    logging.info("get count")
    return json_object['public_repos']

def get_repo_by_page(page: int):
    lst = []
    url = f"https://api.github.com/users/bearddan2000/repos?per_page=100&page={page}"
    json_object = to_json(url)
    for item in json_object:
        name = item['name']
        try:
            if len(name.split("-")) > 1:
                desc=item['description']
                topics=item['topics']
                repo = Repo(name,desc,topics)
                lst.append(repo)
                logging.info(repo)
        except:
            pass
    return lst

def repo_to_csv(rows: list):
    # field names 
    fields = ['Name', 'Desc', 'Topics'] 
    logging.info(fields)
    with open('/app/Repo.csv', 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(rows)

def main():
    print("hello world")
    repo = []
    total_by_hundred: int = get_count()/100
    total_rounded: int = math.ceil(total_by_hundred)
    for page in range(total_rounded):
        collection = get_repo_by_page(page+1)
        if collection is not None:
            repo.append(collection)
    repo_to_csv(repo)

main()

def test_get_count_get_url():
    url = "https://api.github.com/users/bearddan2000"
    assert get_url(url).status_code == 200

def test_get_count_to_json_public_repos():
    url = "https://api.github.com/users/bearddan2000"
    assert to_json(url).has_key('public_repos') == True

def test_get_count():
    assert get_count() > 0

def test_get_repo_get_url():
    url = "https://api.github.com/users/bearddan2000/repos?per_page=100&page=1"
    assert get_url(url).status_code == 200

def test_get_repo_to_json_name():
    url = "https://api.github.com/users/bearddan2000/repos?per_page=100&page=1"
    assert to_json(url).has_key('name') == True

def test_get_repo_to_json_description():
    url = "https://api.github.com/users/bearddan2000/repos?per_page=100&page=1"
    assert to_json(url).has_key('description') == True

def test_get_repo_to_json_topics():
    url = "https://api.github.com/users/bearddan2000/repos?per_page=100&page=1"
    assert to_json(url).has_key('topics') == True