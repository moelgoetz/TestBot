#!/bin/bash

# Your Confluence API key and email
#todo: add Github actions for secrets

# Base URL for the Confluence API
BASE_URL=https://access-ci.atlassian.net/wiki/rest/api

# Function to recursively fetch and process pages
fetch_pages_recursive() {
    local parent_id=$1

    # Fetch child pages of the current parent page
    child_pages_url="${BASE_URL}/content/${parent_id}/child/page"
    response=$(wget --user="${EMAIL}" --password="${API_KEY}" -O - "${child_pages_url}")
    #response=$(wget -s -u "${EMAIL}:${API_KEY}" -X GET "${child_pages_url}")
    echo "$child_pages_url"
    echo "$response"
    # Process each child page
    echo "$response" | jq -c '.results[]' | while read page; do
        page_id=$(echo "$page" | jq -r '.id')
        title=$(echo "$page" | jq -r '.title')

        # Fetch the page content to check the status
        page_content_url="${BASE_URL}/content/${page_id}?expand=body.storage"
        # Use wget to fetch the page and capture headers
        headers=$(wget --user="${EMAIL}" --password="${API_KEY}" --server-response -O /dev/null "${page_content_url}" 2>&1)

        # Extract the HTTP status code from the headers
        page_response=$(echo "$headers" | grep "HTTP/" | awk '{print $2}' | head -n 1)

        echo "Title: $title"
        echo "Status Code: $page_response"
        echo "Page ID: $page_id"
        echo "-----------------------------"

        # Recursively fetch and process child pages of this page
        fetch_pages_recursive "$page_id"
    done
}

# Start the recursive fetching from the "Getting Help" page
PARENT_PAGE_ID="467109469"
fetch_pages_recursive "$PARENT_PAGE_ID"
