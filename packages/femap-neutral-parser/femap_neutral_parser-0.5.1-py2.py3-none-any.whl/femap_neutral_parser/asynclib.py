import asyncio
from femap_neutral_parser import blocks


async def get_block_raw_data(
    fpath: str, toc: dict, block_id: int, as_file_like: bool = False
):
    """yield file-like objects containing block data"""
    fh = open(fpath)
    line_offset = 0
    for line_start, line_end in toc[block_id]:
        lines = range(line_start, line_end)
        lines_content = []
        for line_nb, line in enumerate(fh, start=line_offset):
            if line_nb > line_end:
                line_offset = line_nb + 1
                break
            if line_nb in lines:
                lines_content.append(line)
        if as_file_like:
            txt = StringIO()
            txt.writelines(lines_content)
            txt.seek(0)
        else:
            txt = lines_content
        yield txt
    fh.close()


async def _async_parse_blocks(
    fpath: str, toc: dict, femap_version: str, block_id: int
) -> None:
    """"""
    block = getattr(blocks, f"B{block_id}")(version=femap_version)
    async for txt in get_block_raw_data(fpath, toc, block_id=block_id):
        block.parse(txt)
    return block
