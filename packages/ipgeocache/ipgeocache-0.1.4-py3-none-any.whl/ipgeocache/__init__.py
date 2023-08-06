import os
import re
import json
import warnings
import logging

from pathlib import Path
from typing import Optional, Dict, Any, Tuple
from functools import lru_cache

import requests

CACHE_DIR_NAME: str = "ipgeocache"
BASE_URL: str = "https://ipinfo.io/{}"

Json = Dict[str, Any]


USER_DATA_DIR: str = os.environ.get(
    "XDG_DATA_HOME", os.path.join(os.environ["HOME"], ".local", "share")
)


@lru_cache(1)
def get_cache_dir(passed_cache: Optional[str] = None) -> Path:
    """
    Uses the cache directory given by the user,
    $IPGEOCACHE_DIR, else uses the default location
    """
    loc: Path
    if passed_cache is not None:
        loc = Path(passed_cache)
    elif "IPGEOCACHE_DIR" in os.environ:
        loc = Path(os.environ["IPGEOCACHE_DIR"])
    else:
        loc = Path(USER_DATA_DIR) / CACHE_DIR_NAME
    locabs: Path = Path(loc).expanduser().absolute()
    if not locabs.exists():
        warnings.warn(f"{locabs} cache dir doesn't exist, creating...")
        locabs.mkdir(parents=True)
    return locabs


def get_token(token: Optional[str] = None) -> str:
    """
    Get the token passed by the user, else lookup in environment
    """
    if token is not None:
        return token
    elif "IPINFO_TOKEN" in os.environ:
        return os.environ["IPINFO_TOKEN"]
    else:
        warnings.warn("No geolocation ipinfo token passed or in environment!")
        return ""


SAFE_FILENAMES_PAT = re.compile(r"[:.]")


def _slugify_ip(ip: str) -> str:
    return re.sub(SAFE_FILENAMES_PAT, "_", ip)


def get_from_cache(
    ip_address: str, cache_dir: Path, logger: Optional[logging.Logger]
) -> Tuple[Path, Optional[Json]]:
    """
    Return the expected cache path, and any data if it exists
    """
    cache_target: Path
    cache_target = cache_dir / ip_address
    # if that file doesn't exist, slugify the name and return that
    if not cache_target.exists():
        cache_target = cache_dir / _slugify_ip(ip_address)
    if cache_target.exists():
        if logger is not None:
            logger.debug("Cache Hit: {}, reading {}".format(ip_address, cache_target))
        ipinfo: Json = json.loads(cache_target.read_text())
        return cache_target, ipinfo
    return cache_target, None


def get_from_cache_or_request(
    ip_address: str,
    ipinfo_token: str,
    cache_dir: Path,
    logger: Optional[logging.Logger],
) -> Json:
    cache_target, ipinfo = get_from_cache(ip_address, cache_dir, logger)
    if ipinfo is not None:
        return ipinfo
    else:
        if logger is not None:
            logger.debug(f"Cache Miss: {ip_address}, requesting...")
        resp = requests.get(
            BASE_URL.format(ip_address),
            headers={"Authorization": "Bearer {}".format(ipinfo_token)},
        )
        resp.raise_for_status()
        resp_json: Json = resp.json()
        with cache_target.open("w") as jf:
            json.dump(resp_json, jf)
        return resp_json


def get(
    ip_address: str,
    token: Optional[str] = None,
    cache_dir: Optional[str] = None,
    logger: Optional[logging.Logger] = None,
) -> Json:
    """
    Get geolocation info for an IP address

    optional parameters:
    token: ipinfo token to use, if IPINFO_TOKEN not set as an environment variable
    cache_dir: directory to use for cache, overrides default (XDG_DATA_DIR/ipgeocache) if given
    logger: a logger to send cache hit/miss info out on
    """
    return get_from_cache_or_request(
        ip_address, get_token(token), get_cache_dir(cache_dir), logger=logger
    )
