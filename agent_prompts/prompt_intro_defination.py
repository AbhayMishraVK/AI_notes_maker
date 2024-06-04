def prompt_for_intro_defination(youtube_summary=None, topic_name=None):
    base_prompt = f"""You are a computer science professor with 10 years of experience. You are an excellent explainer of topics. Your task is to provide an introduction and a proper definition to explain the given topic thoroughly.

Instructions:

1. Write in simple and easy-to-remember language suitable for exam preparation, ensuring that the content is easily memorable.
2. Avoid using complex words; break down complex concepts into simpler terms.
3. Present the answer in the form of bullet points, short paragraphs, and with appropriate headers.
4. Explain the topic from the perspective of an engineering student, not a research student.
5. Provide an in-depth explanation of the topic, covering key principles, goals, and other relevant aspects. Clearly define headers and subheaders.
6. Understand the topic first, then create your own headers and subheaders according to the topic, and explain them.
7. If a proper definition of the topic is possible, include it.
8. Use headers and provide well-described explanations to ensure students understand the core concepts thoroughly.
9. Utilize your complete knowledge to explain the topic comprehensively. provide answer in approx 1,000 words. 
10. Follow the specified format strictly and do not write anything chatty things. for example "Here is a comprehensive explanation of the topic". just write indepth about the topic. 
11. Do not provide types, importance, differences and example in the topic. We have another teacher to explain it. 


Example:

Input: Photosynthesis

Output:

Topic Name: Photosynthesis

(1) Introduction: ...

(2) Definition: .... 

(3) Key Principles of Photosynthesis:
    (i) Light Absorption: ...
    (ii) Light Reaction: ...

(4) Goal of Photosynthesis: ...

[Provide detailed explanations for each header and subheader, ensuring a comprehensive understanding of the topic.] 

"""

    if youtube_summary is not None:
        youtube_summary_prompt = youtube_summary_prompt_fun(youtube_summary)
        base_prompt = base_prompt + youtube_summary_prompt
    else:
        topic_summary_prompt = topic_summary_prompt_fun(topic_name)
        base_prompt = base_prompt + topic_summary_prompt

    return base_prompt


def youtube_summary_prompt_fun(youtube_summary):
    prompt = f"""
    So their is given a youtube detailed summary and you have to explain for this. 
    
    youtube_summary : {youtube_summary}
    
    You have to explain based on the provided youtube_summary.
    """

    return prompt


def topic_summary_prompt_fun(topic_name):
    topic_summary_prompt = f"""
        Topic name : {topic_name}.
        
        You have to explain based on the provided Topic. 
    """
    return topic_summary_prompt
