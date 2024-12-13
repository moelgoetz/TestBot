import os
import requests
from requests.auth import HTTPBasicAuth
import pdfkit


# Confluence credentials and base URL
confluence_base_url = 'https://access-ci.atlassian.net/wiki'
api_base_url = f'{confluence_base_url}/rest/api'
username = os.getenv('conf_username')
api_token = os.getenv('conf_api_token')

# Headers for authentication
headers = {
    'Authorization': f'Basic {requests.auth._basic_auth_str(username, api_token)}',
    'Content-Type': 'application/json'
}

# Function to fetch all pages recursively
def fetch_pages(space_key):
    url = f'{api_base_url}/space/{space_key}/content/page'
    params = {
        'expand': 'ancestors',
        'limit': 100  #change if needed
    }


    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    pages = data.get('results', [])
    for page in pages:
        yield page
        # Recursively fetch child pages
        child_pages = fetch_child_pages(page['id'])
        for child_page in child_pages:
            yield child_page
    
    # Handle pagination
    url = data['_links'].get('next')

def fetch_child_pages(parent_page_id):
    url = f'{api_base_url}/content/{parent_page_id}/child/page'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    pages = data.get('results', [])
    for page in pages:
        yield page
        # Recursively fetch child pages
        child_pages = fetch_child_pages(page['id'])
        for child_page in child_pages:
            yield child_page

# Function to fetch page content as HTML
def fetch_page_content(page_id):
    url = f'{api_base_url}/content/{page_id}?expand=body.storage'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data['body']['storage']['value']

# Function to save page content as PDF
def save_page_as_pdf(page):
    title = page['title'].replace('/', '_').replace('\\', '_')
    filename = f"{title}.pdf"
    output_path = os.path.join('pdfs', filename)

    html_content = fetch_page_content(page['id'])

    try:
        pdfkit.from_string(html_content, output_path)
        print(f'Saved: {output_path}')
    except Exception as e:
        print(f'Failed to save {page["title"]}: {str(e)}')


# Set the space key
space_key = 'ACCESSdocumentation'

# Create a directory to store the page data
if not os.path.exists('pdfs'):
    os.makedirs('pdfs')

# Fetch and process pages
for page in fetch_pages(space_key):
    save_page_as_pdf(page)