import requests


def get_repo_contents(repo_url):
    """
    Returns the list of files and directories, along with their metadata, in a public GitHub repository.

    Args:
        repo_url (str): The URL of the public GitHub repository in the format 'username/repo_name'.

    Returns:
        list: A list of dictionaries, where each dictionary represents the metadata of a file or directory.
    """

    def get_contents(path):
        """
        Recursively fetches the contents of a directory in the repository.

        Args:
            path (str): The path of the directory to fetch contents for.

        Returns:
            list: A list of dictionaries representing the metadata of files and directories in the given path.
        """
        api_url = f"https://api.github.com/repos/{repo_url}/contents/{path}?ref=master"
        response = requests.get(api_url)

        if response.status_code == 200:
            contents = response.json()
            result = []
            for item in contents:
                item_data = {
                    'path': item['path'],
                    'type': item['type'],
                    'html_url': item['html_url']
                }
                if item['type'] == 'file':
                    item_data['size'] = item['size']
                    item_data['download_url'] = item['download_url']
                result.append(item_data)
                if item['type'] == 'dir':
                    result.extend(get_contents(item['path']))
            return result
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []

    return get_contents("")
