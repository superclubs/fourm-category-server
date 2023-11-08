# Third Party
from bs4 import BeautifulSoup


# Main Section
def extract_content_summary(content):
    soup = BeautifulSoup(content, features='html.parser')

    # Extract <style> Tags
    for style_tag in soup.find_all('style'):
        style_tag.extract()

    # Find all <p> tags
    p_tags = soup.find_all('p')
    for p_tag in p_tags:
        p_tag = p_tag.find(text=True, recursive=False)

        # Check if the <p> tag has text and not empty
        if p_tag and not p_tag.isspace():
            p_content = p_tag.get_text()
            p_tag.replace_with(p_content + '<br>')

    # Combine the text
    text_parts = soup.find_all(text=True)
    text_parts_filtered = filter(lambda text_part: len(text_part.strip()) >= 1, text_parts)
    content_summary = ' '.join(text_parts_filtered)

    # Strip last <br> tag
    content_summary = content_summary.rstrip('<br>')
    return content_summary
