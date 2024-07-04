# handle server disconnections
# handle endless redirects
import asyncio
import logging
import urllib.error
import urllib.parse
import re
import sys

from aiohttp import ClientSession, ClientError

logging.basicConfig(
	format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
	level=logging.DEBUG,
	datefmt="%H:%M:%S",
	stream=sys.stderr,
)
logger = logging.getLogger(__name__)
logging.getLogger('chardet.charsetprober').disabled

HREF_RE = re.compile(r'href="(.*?)"')
# **kwargs
async def fetch_html(url) -> str:
	async with ClientSession() as session:
			async with session.get(url) as resp:
				resp.raise_for_status()
				logger.info("Got response [%s] for URL: %s", resp.status, url)
				html = await resp.text()
				return html
	   

async def parse(url: str):
	found = set()
	try:
		html = await fetch_html(url)
		for link in HREF_RE.findall(html):
			try:
				abslink = urllib.parse.urljoin(url, link)
				found.add(abslink)
			except (urllib.error.URLError, ValueError):
				logger.exception("Error parsing URL: %s", link)
				pass
		logger.info("Found %d links for %s", len(found), url)
		return found
	except (
		  aiohttp.ClientError,
		  aiohttp.http_exceptions.HttpProcessingError,
	) as e:
		logger.error(
			"aiohttp exception for %s [%s]: %s",
			url,
			getattr(e, "status", None),
			getattr(e, "message", None),
		)
		return found
	except Exception as e:
			logger.error(
				"Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
			)
			return found


if __name__ == '__main__':
	asyncio.run(parse("https://regex101.com/"))

