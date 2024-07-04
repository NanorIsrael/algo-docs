# handle server disconnections
# handle endless redirects
import asyncio
import logging
import urllib.error
import urllib.parse
from typing import IO
import re
import sys

import aiofiles
import aiohttp


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
	async with aiohttp.ClientSession() as session:
			async with session.get(url) as resp:
				resp.raise_for_status()
				logger.info("Got response [%s] for URL: %s", resp.status, url)
				html = await resp.text()
				return html
	   

async def parse(url: str) -> set:
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

async def write_one(file: IO, url: str) -> None:
	"""Write the found HREFs from `url` to `file`."""
	resp = await parse(url)
	if not resp:
		return None
	async with aiofiles.open(file, 'a') as f:
		for p in resp:
			await f.write(f"{url}\t{p}")
		logger.info("Wrote results for source URL: %s", url)

async def bulk_crawl_write(file: IO, urls: set) -> None:
	"""Crawl & write concurrently to `file` for multiple `urls`."""
	task = []
	for url in urls:
		task.append(
			write_one(file, url)
		)
	await asyncio.gather(*task)


if __name__ == '__main__':
	import pathlib
	import sys

	assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
	parentdir = pathlib.Path(__file__).parent
	with open(parentdir.joinpath("urls.txt")) as infile:
		urls = set(map(str.strip, infile))

	outpath = parentdir.joinpath('foundurls.txt')
	with open(outpath, 'w') as outfile:
		outfile.write("source_url\tparsed_url\n")

	print(parentdir)
	asyncio.run(bulk_crawl_write(outpath, urls))

