# handle server disconnections
# handle endless redirects
import asyncio
from aiohttp import ClientSession, ClientError
import logging
import re
import sys


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
	else:
		for link in HREF_RE.findall(html):
			print("link", link)


if __name__ == '__main__':
	asyncio.run(parse("https://regex101.com/"))

