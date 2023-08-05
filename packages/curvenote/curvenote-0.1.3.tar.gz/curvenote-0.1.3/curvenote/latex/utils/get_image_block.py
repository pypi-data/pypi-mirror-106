import logging
import os

import requests

from ...client import Session
from ...models import BlockFormat, BlockVersion
from .index import block_hash_to_url
from .localize_images import ImageFormats


def get_image_block(
    session: Session, assets_folder: str, block_path: str, local_path: str
):
    url = block_hash_to_url(session.api_url, block_path, BlockFormat.tex)
    logging.info("fetching image block from %s", url)
    image_block = session._get_model(url, BlockVersion)
    if not image_block:
        raise ValueError(f"Could not fetch image block {url}")

    # download from links.download (signed) to local path
    if not image_block.links.download:
        raise ValueError(f"Block kind {image_block.kind} has no download link")

    resp = requests.get(image_block.links.download)
    if resp.status_code >= 400:
        raise ValueError(resp.content)

    # now that we have the block we need to update the local path in the content
    # and save the file with the correct file extension
    content_type = resp.headers.get("content-type")
    if content_type not in ImageFormats:
        raise ValueError(f"Unsupported image content type {content_type}")
    ext = ImageFormats[content_type]
    local_path_with_extension = f"{local_path}.{ext}"

    logging.info("Writing %s", local_path_with_extension)
    with open(os.path.join(assets_folder, local_path_with_extension), "wb+") as file:
        file.write(resp.content)

    return image_block, local_path_with_extension
