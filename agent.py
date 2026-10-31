
from langchain_ollama import ChatOllama
from tools import course_retrieval_tool, career_search_tool

# Connect to Ollama
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,
    num_ctx=2048
)

def ask_agent(question):

    q = question.lower()

    academic_keywords = [
        "explain", "what is", "define", "subject",
        "syllabus", "course", "academic", "chapter",
        "concept", "topic", "notes"
    ]

    career_keywords = [
        "career", "job", "internship", "opportunity",
        "skill", "employment", "profession"
    ]

    # Decide which tools are needed
    need_academic = any(word in q for word in academic_keywords)
    need_career = any(word in q for word in career_keywords)

    # Retrieve academic information
    academic_result = ""

    if need_academic:
        academic_result = course_retrieval_tool.invoke({
            "question": question
        })
        print("TOOL CALLED: course_retrieval_tool")

    # Retrieve career information
    career_result = ""

    if need_career:
        career_result = career_search_tool.invoke({
            "topic": question
        })
        print("TOOL CALLED: career_search_tool")

    # Prepare context for the LLM
    context = f"""
    Academic PDF information:
    {academic_result}

    Career opportunity information:
    {career_result}
    """

    prompt = f"""
    You are EduPathAI, an academic and career guidance assistant.

    Answer the user's question using the supplied information.

    Rules:
    1. Use academic PDF information for academic answers.
    2. Use career tool information for career answers.
    3. Never invent facts, salaries, companies or job openings.
    4. Career opportunities are sample demo records, not live vacancies.
    5. If the PDF does not contain relevant information, say so.
    6. Use simple English and clear headings.

    Context:
    {context}

    User question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":

    print("Welcome to EduPathAI!")

    while True:

        question = input(
            "\nAsk EduPathAI (type exit to stop): "
        )

        if question.lower().strip() == "exit":
            print("Thank you for using EduPathAI!")
            break

        try:
            answer = ask_agent(question)
            print("\nEduPathAI:", answer)

        except Exception as e:
            print("\nError:", e)
