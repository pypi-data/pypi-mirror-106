import aiohttp

from yutto.api.types import CId
from yutto.utils.fetcher import Fetcher
from yutto.utils.danmaku import DanmakuData


async def get_xml_danmaku(session: aiohttp.ClientSession, cid: CId) -> DanmakuData:
    danmaku_api = "http://comment.bilibili.com/{cid}.xml"
    data = await Fetcher.fetch_text(session, danmaku_api.format(cid=cid), encoding="utf-8")
    # fmt: off
    return {
        "source_type": "xml",
        "save_type": None,
        "data": data
    }
    # fmt: on


async def get_protobuf_danmaku(session: aiohttp.ClientSession, cid: CId, segment_id: int = 1) -> DanmakuData:
    # Protobuf 弹幕，由于 XML 现在已经足够了，暂不使用它
    danmaku_api = "http://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={segment_id}"
    data = await Fetcher.fetch_bin(session, danmaku_api.format(cid=cid, segment_id=segment_id))
    # fmt: off
    return {
        "source_type": "protobuf",
        "save_type": None,
        "data": data
    }
    # fmt: on
