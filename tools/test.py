from tavily_tool import tavily_search
from flight_tool import search_flights

# res =  tavily_search("Best hotels in India")
# print(res)

res = search_flights("Plan a 7 days Nepal trip from India")
print(res)
