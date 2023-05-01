import requests
from bs4 import BeautifulSoup

def get_metadata(url):
    # Fetch webpage
    response = requests.get(url)

    # Parse webpage using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract metadata tags
    metadata_tags = soup.find_all('meta')

    # Create list of metadata dictionary
    metadata_list = []
    for tag in metadata_tags:
        metadata_dict = {}
        for attribute in tag.attrs:
            if attribute.startswith('property') or attribute.startswith('name'):
                # Extract metadata property or name
                key = attribute.split(':')[-1]
                metadata_dict[key] = tag.get(attribute)
        if metadata_dict:
            # Add metadata dictionary to list
            metadata_list.append(metadata_dict)

    # Return list of metadata
    return metadata_list
