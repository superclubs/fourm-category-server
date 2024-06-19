from bs4 import BeautifulSoup, Tag


# Main Section
def extract_content_summary(content):
    soup = BeautifulSoup(content, features="html.parser")

    block_tags = [
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

    extract_tags = ["style", "script"]
    media_tags = ["img", "video", "iframe", "jodit-file", "jodit-link-preview"]

    # Extract style, script Tags
    for extract_tag in soup.find_all(extract_tags):
        extract_tag.extract()

    # 태그 내부에 텍스트가 없거나, br태그만 있는지 체크하는 재귀 함수입니다.
    def is_empty_or_br_only(tag):
        return all(
            (isinstance(content, Tag) and (content.name == "br" or is_empty_or_br_only(content)))
            or (isinstance(content, str) and not content.strip())
            for content in tag.contents
        )

    block_tag_elements = soup.find_all(block_tags)
    for block_tag in block_tag_elements:
        has_media = any(isinstance(content, Tag) and content.name in media_tags for content in block_tag.descendants)

        if has_media:
            # 미디어 태그를 제거합니다.
            for media_tag in block_tag.find_all(media_tags):
                media_tag.extract()

            br_count = sum(1 for content in block_tag.descendants if isinstance(content, Tag) and content.name == "br")
            # 미디어 태그를 제거한 후, 블록 태그의 내용이 없는지 체크합니다. 텍스트가 없거나, br태그만 남아있는 경우 비어있는 것으로 취급하여 제거합니다.
            if is_empty_or_br_only(block_tag):
                # 삭제할 태그 내부에 있는 br태그의 개수만큼 br태그를 추가합니다.
                for _ in range(br_count):
                    br_tag = soup.new_tag("br")
                    block_tag.insert_after(br_tag)

                # 요소를 제거합니다.
                block_tag.extract()
                continue

        # 비어있거나 br태그만 있는 경우, br 태그를 추가하지 않습니다.
        if not is_empty_or_br_only(block_tag):
            br_tag = soup.new_tag("br")
            block_tag.insert_after(br_tag)

    # br 태그를 제외한 모든 html 태그를 제거합니다.
    for element in soup.find_all():
        if element.name != "br":
            element.unwrap()

    # 마지막에 br 태그가 있으면 제거합니다.
    while soup.contents and isinstance(soup.contents[-1], Tag) and soup.contents[-1].name == "br":
        soup.contents[-1].extract()

    content_summary = str(soup)
    return content_summary
