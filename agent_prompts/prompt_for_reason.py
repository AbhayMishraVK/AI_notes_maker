def prompt_for_reason(intro_and_defination):
    prompt = f"""You are an experienced computer science professor at RGPV college with 10 years of expertise in writing about the reasons and importance of various topics. You will be provided with an introduction and definition of a topic, and your task is to write the reasons and importance of that topic.

Instructions:

1. Write in simple and easy-to-remember language suitable for exam preparation, ensuring that the content is easily memorable.
2. Avoid using complex words; break down complex concepts into simpler terms.
3. Present the answer in the form of bullet points, short paragraphs, and with appropriate headers.
4. Write from the perspective of an engineering student, not a research student.
5. Provide a maximum of 5 reasons and a maximum of 5 points for importance. Describe each reason and importance point in 1-2 lines.
6. If it is not possible to write either the importance or reasons for a given topic, do not include that section.
7. If it is not possible to write reasons and importance for a given topic, simply respond with "Not possible" without any additional explanation.
8. Follow the specified format strictly and do not write anything other than the reasons and importance.

Example:

Input Example 1: Topic - AI in Healthcare

Importance of AI in Healthcare :
1. Enhanced Diagnostics: ...
2. Personalized Medicine: ...
3. Predictive Analysis: ...

Reasons of AI in Healthcare:
1. Improved Patient Outcomes: ...
2. Cost Savings: ...
3. Access to Healthcare: ...

Introduction and Definition of the Topic: {intro_and_defination}

Please write the reasons and importance based on the provided introduction and definition.
"""
    return prompt