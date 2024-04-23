from bs4 import BeautifulSoup, Tag


# Main Section
def extract_content_summary(content):
    soup = BeautifulSoup(content, features="html.parser")

    block_tag_list = [
        "div",
        "p",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "ul",
        "ol",
        "li",
        "blockquote",
        "pre",
        "table",
        "header",
        "footer",
        "section",
        "article",
        "nav",
        "aside",
        "address",
        "form",
        "fieldset",
        "hr",
    ]

    extract_tag_list = ["style", "script", "jodit-file", "jodit-link-preview"]

    # Extract style, script Tags
    for extract_tag in soup.find_all(extract_tag_list):
        extract_tag.extract()

    # Add br Tag after block tag
    block_tag_elements = soup.find_all(block_tag_list)
    for block_tag in block_tag_elements:
        br_tag = soup.new_tag("br")
        block_tag.insert_after(br_tag)

    # Unwrap all tags except br
    for element in soup.find_all():
        if element.name != "br":
            element.unwrap()

    # Remove br Tag at the end of the content
    while soup.contents and isinstance(soup.contents[-1], Tag) and soup.contents[-1].name == "br":
        soup.contents[-1].extract()

    content_summary = str(soup)
    return content_summary
