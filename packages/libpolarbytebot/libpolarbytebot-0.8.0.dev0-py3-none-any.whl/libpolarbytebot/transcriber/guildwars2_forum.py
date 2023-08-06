"""Module to retrieve information from Guild Wars 2 forum posts."""
import datetime
import requests
import re

from urllib import parse
from bs4 import BeautifulSoup

from .markdown import guildwars2_html2markdown
from .formats import guildwars2_format

__all__ = [
    'guildwars2_forum_parse',
    'guildwars2_findall_forum_urls',
    'guildwars2_findall_forum_urls_mentions',
]


__forum_url_regex = 'https?://..-forum\\.guildwars2\\.com/topic/[^ \\])\\s]*'


class ForumUrl:
    def __init__(self, url):
        self.url = str(url).strip()

    @property
    def is_comment(self):
        return self.comment_id is not None

    @property
    def is_thread(self):
        return self.comment_id is None

    @property
    def comment_id(self):
        parsed = parse.urlparse(self.url)
        # Either it is a direct link to a comment, like
        # https://en-forum.guildwars2.com/topic/95447-game-update-notes-may-11-2021/?tab=comments#comment-1364791
        match = re.match('comment-(\\d+)$', parsed.fragment)
        if match:
            return match.group(1)

        # Or it is a link to a "comment search" in a thread, like
        # https://en-forum.guildwars2.com/topic/95447-game-update-notes-may-11-2021/?do=findComment&comment=1364791
        query = parse.parse_qs(parsed.query)
        if query.get('do', None) == ['findComment'] and 'comment' in query:
            return query['comment'][0]

        return None


class Article:
    def __init__(self):
        self.content = None
        self.author = None
        self.is_official = None
        self.url = None
        self.timestamp = None

    @property
    def comment_id(self):
        return ForumUrl(self.url).comment_id

    def to_post(self):
        """Converts this article to a GuildWars2Format post."""
        return guildwars2_format.GuildWars2Format(
            author=self.author,
            timestamp=self.timestamp,
            text=self.content,
            type='forum',
            url=self.url,
            is_offical=self.is_official,
        )


class GuildWars2ForumException(Exception):
    pass


def guildwars2_findall_forum_urls(content):
    forum_findings = re.findall(__forum_url_regex, content)
    forum_findings = set(forum_findings)
    return forum_findings


def guildwars2_findall_forum_urls_mentions(content, mention_regex):
    forum_mention_findings = []
    temp_forum_mention_findings = re.findall(
        mention_regex + __forum_url_regex, content
    )

    for temp_mention in temp_forum_mention_findings:
        forum_mention_findings.extend(
            guildwars2_findall_forum_urls(temp_mention)
        )

    forum_mention_findings = set(forum_mention_findings)
    return forum_mention_findings


def extract_articles(html, base_url):
    """Extract all of "articles" (forum posts) from the given HTML data.

    :param html: The HTML data.
    :type html: str
    :param base_url: The base url for relative links.
    :type base_url: str
    :return: A generator of found articles, all of type :class:`Article`.
    :rtype: generator
    """
    soup = BeautifulSoup(html, features='html.parser')
    articles = soup.find_all('article')
    for article_elem in articles:
        article = Article()

        content = article_elem.find(attrs={'data-role': 'commentContent'})
        content = guildwars2_html2markdown.convert(content, base_url)
        article.content = content

        aside = article_elem.find('aside')
        author = aside.find('h3').get_text().strip()
        article.author = author

        group = aside.find(attrs={'data-role': 'group'})
        if group and 'ArenaNet Staff' in group.get_text():
            article.is_official = True
        else:
            article.is_official = False

        timestamp = article_elem.find('time')
        article.timestamp = datetime.datetime.fromisoformat(
            timestamp['datetime'].rstrip('Z')
        )

        meta = article_elem.find('div', class_='ipsComment_meta')
        url = (meta
               .find('div', class_='ipsResponsive_hidePhone', recursive=False)
               .find('a'))
        if url:
            article.url = url['href']

        yield article


def guildwars2_forum_parse(url):
    """
    Fetch and transform a forums post into a markdown formatted string, usable
    in the polarbytebot post text body.

    No signatures included.

    :param url: the url of the discussion or comment to transcribe.
    :return: formatted text which can be used in the textbody.
    """
    furl = ForumUrl(url)
    html_response = requests.get(furl.url).content
    articles = extract_articles(html_response, url)

    right_article = None

    if furl.is_comment:
        # filter out the comment which maches the id in the anchor tag
        # (#comment-XXXXXXX)
        for article in articles:
            if article.comment_id == furl.comment_id:
                right_article = article
                break
    elif furl.is_thread:
        try:
            right_article = next(articles)
        except StopIteration:
            # No articles found :(
            raise GuildWars2ForumException(
                "Could not find article for {}".format(url)
            )

    return right_article.to_post().result


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='GW2 forum scraper demonstration.',
    )
    parser.add_argument('url', help='The URL to scrape.')
    args = parser.parse_args()

    print("You gave me the url", args.url)

    match = re.match(__forum_url_regex, args.url)
    if not match:
        print("This is not a forum URL.")
        return

    forum_url = ForumUrl(args.url)
    if forum_url.is_thread:
        print("This is a link to a whole thread")
    else:
        print(
            "This is a link to a single comment with ID",
            forum_url.comment_id,
        )

    print("Here is my post:")
    print()
    print()
    print(guildwars2_forum_parse(args.url))


if __name__ == '__main__':
    main()
