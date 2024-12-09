import os
import subprocess
import json
import pdfkit

# Base API URL for Confluence
api_base_url = 'https://access-ci.atlassian.net/wiki/rest/api'
email = 'your_email'  # Replace with your email #todo: add Github actions for secrets
api_key = 'your_api_key'  # Replace with your API key #todo: add Github actions for secrets

# Function to fetch child pages using wget
def fetch_child_pages(parent_page_id):
    url = f'{api_base_url}/content/{parent_page_id}/child/page'
    command = [
        'wget',
        '--user', email,
        '--password', api_key,
        '-q', '-O', '-', url
    ]

    # Execute wget and capture output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Failed to fetch child pages for {parent_page_id}: {result.stderr}")
        return []

    # Parse JSON response
    data = json.loads(result.stdout)
    return data.get('results', [])

# Function to fetch page content as HTML using wget
def fetch_page_content(page_id):
    url = f'{api_base_url}/content/{page_id}?expand=body.storage'
    command = [
        'wget',
        '--user', email,
        '--password', api_key,
        '-q', '-O', '-', url
    ]

    # Execute wget and capture output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Failed to fetch page content for {page_id}: {result.stderr}")
        return None

    # Parse JSON response
    data = json.loads(result.stdout)
    return data['body']['storage']['value']

# Function to save page content as PDF
def save_page_as_pdf(page):
    title = page['title'].replace('/', '_').replace('\\', '_')
    filename = f"{title}.pdf"
    output_path = os.path.join('pdfs', filename)

    html_content = fetch_page_content(page['id'])
    if not html_content:
        print(f'Failed to fetch content for page: {page["title"]}')
        return

    try:
        pdfkit.from_string(html_content, output_path)
        print(f'Saved: {output_path}')
    except Exception as e:
        print(f'Failed to save {page["title"]}: {str(e)}')

# Recursive function to fetch all pages and save them
def fetch_and_save_pages(parent_page_id):
    # Fetch child pages
    pages = fetch_child_pages(parent_page_id)
    for page in pages:
        # Save current page as PDF
        save_page_as_pdf(page)

        # Recursively fetch and save child pages
        fetch_and_save_pages(page['id'])

# Set the parent page ID and space key
parent_page_id = '467109469'  # ID of the top-level page
space_key = 'ACCESSdocumentation'

# Create a directory to store the PDFs
if not os.path.exists('pdfs'):
    os.makedirs('pdfs')

# Start fetching and saving pages
fetch_and_save_pages(parent_page_id)
