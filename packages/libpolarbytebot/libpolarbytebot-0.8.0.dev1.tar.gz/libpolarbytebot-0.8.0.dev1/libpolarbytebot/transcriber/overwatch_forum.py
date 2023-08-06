import re
import requests

# Imports
try:
    from .markdown import overwatch_html2markdown
    from .markdown import markdown_dictionary as m
    from .formats import overwatch_format
except ImportError:
    import libpolarbytebot.transcriber.markdown.overwatch_html2markdown as overwatch_html2markdown
    import libpolarbytebot.transcriber.markdown.markdown_dictionary as m
    import libpolarbytebot.transcriber.formats.overwatch_format as overwatch_format

__all__ = ['overwatch_findall_forum_urls', 'overwatch_findall_forum_urls_mentions', 'overwatch_forum_parse']

__forum_url_regex = 'https?://.{2,3}?\.forums\.battle\.net/[^ \]<")\s]*'

#https://us.forums.blizzard.com/en/overwatch/t/so-tracer-can-do-all-of-this-but-sombra-needs-a-nerf-for-being-too-powerful/30319
#https://us.forums.blizzard.com/en/overwatch/t/so-tracer-can-do-all-of-this-but-sombra-needs-a-nerf-for-being-too-powerful/30319/2

class ForumUrl:
    def __init__(self, url):
        self.url = str(url).strip()

    @property
    def is_comment(self):
        return re.match('https?://.{2,3}?\.forums\.blizzard\.com/en/overwatch/t/[a-zA-Z\-]+/\d+/\d+(/|)', self.url) is not None

    @property
    def is_thread(self):
        return re.match('https?://.{2,3}?\.forums\.blizzard\.com/en/overwatch/t/[a-zA-Z\-]+/\d+(/|)$', self.url) is not None

    #@property
    #def is_thread_latest(self):
    #    return re.match('http.*?://..-forum\.guildwars2\.com/discussion/\d*?/.*?#latest', self.url) is not None

    @property
    def comment_id(self):
        result = None
        if self.is_thread:
            result = '1'
        else:
            try:
                result = re.match('https?://.{2,3}?\.forums\.blizzard\.com/en/overwatch/t/[a-zA-Z\-]+/\d+/(?P<id>\d+)(/|)', self.url).group('id')
            except AttributeError:
                pass
        return result

    @property
    def json_url(self):
        return self.url.rsplit('#', maxsplit=1)[0] + '.json'

def overwatch_findall_forum_urls(content):
    forum_findings = re.findall(__forum_url_regex, content)
    forum_findings = set(forum_findings)
    return forum_findings


def overwatch_findall_forum_urls_mentions(content, mention_regex):
    forum_mention_findings = []
    temp_forum_mention_findings = re.findall(mention_regex + __forum_url_regex, content)

    for temp_mention in temp_forum_mention_findings:
        forum_mention_findings.extend(overwatch_findall_forum_urls(temp_mention))

    forum_mention_findings = set(forum_mention_findings)
    return forum_mention_findings

def overwatch_forum_parse(url, parse_refs=True):
    """
    Fetch and transform a forums post into a markdown formatted string, usable in the polarbytebot post text body. 
    No signatures included.
    :param url: the url of the discussion or comment to transcribe.
    :return: formatted text which can be used in the textbody.
    """
    def comment(cm, post):
        post.author = cm['username']
        post.timestamp = cm['created_at']
        if cm['moderator'] or cm['admin'] or cm['staff']:
            post._is_offical = True
        post.text = html_to_markdown(cm['cooked'], '')

    furl = ForumUrl(url)
    json_response = requests.get(furl.json_url).json()
    post = overwatch_format.OverwatchFormat(url=url)
    # find the matching post in the post stream
    ref_comment = list(filter(lambda item: str(item['post_number']) == furl.comment_id, json_response['post_stream']['posts']))[0]
    comment(ref_comment, post)

    # Search referenced posts
    all_links = overwatch_findall_forum_urls(post.text)
    if parse_refs and all_links != []:
        all_links = set(all_links)
        for link in all_links:
            post.referenced_posts.append(overwatch_forum_parse(link, parse_refs=False))

    return post.result


def html_to_markdown(content, host):
    parser = overwatch_html2markdown.Htmlparser()
    parser.convert_charrefs = True
    parser.host = 'https://' + host
    content = content.replace('\n', '\n>')
    parser.feed(content)
    return parser.result


if __name__ == '__main__':
    overwatch_forum_parse('https://us.forums.blizzard.com/en/overwatch/t/so-when-xqc-returns/8995/31')
    #overwatch_forum_parse('https://us.forums.blizzard.com/en/overwatch/t/so-when-xqc-returns/8995/26')
    #overwatch_forum_parse('https://us.forums.blizzard.com/en/overwatch/t/so-when-xqc-returns/8995/8')
    #overwatch_forum_parse('https://us.forums.blizzard.com/en/overwatch/t/so-tracer-can-do-all-of-this-but-sombra-needs-a-nerf-for-being-too-powerful/30319')
