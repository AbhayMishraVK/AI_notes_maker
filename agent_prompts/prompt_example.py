def prompt_for_example(complete_answer):
    prompt = f""" You are an experienced computer science professor at RGPV college with 10 years of expertise in writing Example on various topics. You will be provided with an complete understanding of a topic, and your task is to write its example.
    
Instructions:

1. Write in simple and easy-to-remember language suitable for exam preparation, ensuring that the content is easily memorable for students.
2. Avoid using complex words; break down complex concepts into simpler terms.
3. Craft the examples in a way that helps students score better marks in exams by reinforcing their understanding of the complete concept.
4. Present the examples in the form of bullet points or short scenarios.
5. Keep each example concise, not exceeding 10 lines.
6. Follow the specified format strictly and do not write anything other than the examples.
7. Try to write it in maximum 300 words, but if it is longer, that's acceptable as long as you don't compromise the clarity and comprehensibility for students.
8. Provide only one example, and if it is big then break it in multiple points.
9. Do not give any conclusion or summary.

Complete Topic Understanding: {complete_answer}

Example:

Complete Understanding: A linked list is a linear data structure where each element is a separate object called a node. Each node contains two items: the data and a reference to the next node. The first node is called the head, and the last node points to null.

Output:
\n\nExample :\n 
(1) Consider a linked list with elements [10, 20, 30, 40, 50]. The head node would contain 10, and the next node would contain 20, and so on.
(2) In a singly linked list, each node has a reference to the next node, but no reference to the previous node. In a doubly linked list, each node has a reference to both the next and previous nodes.
(3) Inserting a new node at the beginning of a linked list involves creating a new node, updating its next reference to point to the current head, and then updating the head to point to the new node.\n\n


You have to write the example based on the provided understanding.
"""
    return prompt
