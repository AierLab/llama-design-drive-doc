from .searchOnlineTool import fetch_web_page, search_google
from .getStopsTool import get_all_stop_times

FUNCTION_MAPPING = {
    "fetch_web_page": fetch_web_page,
    "search_google": search_google,
    "get_all_stop_times": get_all_stop_times
}

