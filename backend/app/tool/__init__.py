from .searchOnlineTool import fetch_web_page, search_duckduckgo
from .getStopsTool import get_all_stop_times
from .getWeatherTool import get_current_weather

FUNCTION_MAPPING = {
    "fetch_web_page": fetch_web_page,
    "search_duckduckgo": search_duckduckgo,
    "get_all_stop_times": get_all_stop_times,
    "get_current_weather": get_current_weather
}

