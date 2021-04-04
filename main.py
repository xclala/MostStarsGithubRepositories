try:
    import requests
    from getpass import getpass
    password = getpass("xclala's Github password:")
    while True:
        lang = input("programing language:")
        url = f"https://api.github.com/search/repositories?q=language:{lang}&sort=stars"
        r = requests.get(url, auth=(
            'xclala', password))
        print("Status code:", r.status_code)
        response_dict = r.json()
        print("Total repositories:", response_dict['total_count'])
        repo_dicts = response_dict['items']
        print("Repositories returned:", len(repo_dicts))
        print("\nSelected information about each repository:")
        for repo_dict in repo_dicts:
            print('\nName:', repo_dict['name'])
            print('FullName:', repo_dict['full_name'])
            print('Owner:', repo_dict['owner']['login'])
            print('Repository:', repo_dict['html_url'])
            print('Description:', repo_dict['description'])
        print("\n\n\n")
except Exception as e:
    from os import system
    print("\a")
    print(e)
    system("pause")
