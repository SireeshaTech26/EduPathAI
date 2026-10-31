
from tools import course_retrieval_tool, career_search_tool

print("\n========== TEST 1: COURSE RETRIEVAL ==========")

result1 = course_retrieval_tool.invoke({
    "question": "What is Machine Learning?"
})

print(result1)


print("\n========== TEST 2: CAREER SEARCH ==========")

result2 = career_search_tool.invoke({
    "topic": "Python Machine Learning"
})

print(result2)
