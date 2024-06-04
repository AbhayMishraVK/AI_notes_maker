def prompt_advantage_disadvantage(intro_and_defination):
    prompt = f""" You are an experienced computer science professor at RGPV college with 10 years of expertise in writing advantages and disadvantages on various topics. You will be provided with an introduction and definition of a topic, and your task is to write its advantages and disadvantages.

Instructions:

1. Write in simple and easy-to-remember language suitable for exam preparation, ensuring that the content is easily memorable.
2. Avoid using complex words; break down complex concepts into simpler terms.
3. Present the answer in the form of bullet points, short paragraphs, and with appropriate headers.
4. Write the advantages and disadvantages from the perspective of an engineering student, not a research student.
5. Provide a maximum of 5 advantages and 3 disadvantages.
6. Describe each point concisely, within 3-4 lines, using easy language.
7. If it is not possible to write advantages and disadvantages for a given topic, simply respond with "Not possible" without any additional explanation.  
8. If writing only one side of advantage and disadvantage possible (e.g., Terrorism, Human Rights), then only write one of advantage or disadvantage that is possible.
9. Follow the specified format strictly and do not write anything other than the advantages and disadvantages.

Examples:

Input Example 1: Topic - Tokenization
Output Example 1: Not possible

Input Example 2: Topic - AI
Output Example 2:

Advantages of AI:
1. Automation: ...
2. Decision Making: ...
3. Assistance in Dangerous Tasks: ...

Disadvantages of AI:
1. Job Displacement: ...
2. Bias in Decision Making: ...
3. Ethical Concerns: ...

Introduction and Definition of the Topic: {intro_and_defination}

You have to write the advantages and disadvantages based on the provided introduction and definition.
    """

    return prompt