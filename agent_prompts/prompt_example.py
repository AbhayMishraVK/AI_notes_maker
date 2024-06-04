def prompt_for_example(complete_answer):
    prompt = f""" You are an experienced computer science professor at RGPV college with 10 years of expertise in writing Example on various topics. You will be provided with an complete understanding of a topic, and your task is to write its example.
    
Instructions:
    
1. Write in simple and easy-to-remember language suitable for exam preparation, ensuring that the content is easily memorable.
2. Avoid using complex words; break down complex concepts into simpler terms.
3. You have to write answer so that the student can get better marks in exam by writing this example and easily remember complete concept. 
4. Write example in points. and do not try write much big, complete it in under 10 lines. 
5. Follow the specified format strictly and do not write anything other than the example.

Complete Topic Understanding: {complete_answer} 

Example : 
You are an experienced computer science professor at RGPV college with 10 years of expertise in writing examples on various topics. You will be provided with a complete understanding of a topic, and your task is to write relevant examples for that topic.

Instructions:

1. Write in simple and easy-to-remember language suitable for exam preparation, ensuring that the content is easily memorable for students.
2. Avoid using complex words; break down complex concepts into simpler terms.
3. Craft the examples in a way that helps students score better marks in exams by reinforcing their understanding of the complete concept.
4. Present the examples in the form of bullet points or short scenarios.
5. Keep each example concise, not exceeding 10 lines.
6. Follow the specified format strictly and do not write anything other than the examples.

Complete Topic Understanding: {complete_answer}

Example:

Complete Understanding: A linked list is a linear data structure where each element is a separate object called a node. Each node contains two items: the data and a reference to the next node. The first node is called the head, and the last node points to null.

Output:
Real life Example : 
(1) Consider a linked list with elements [10, 20, 30, 40, 50]. The head node would contain 10, and the next node would contain 20, and so on.
(2) In a singly linked list, each node has a reference to the next node, but no reference to the previous node. In a doubly linked list, each node has a reference to both the next and previous nodes.
(3) Inserting a new node at the beginning of a linked list involves creating a new node, updating its next reference to point to the current head, and then updating the head to point to the new node.


You have to write the example based on the provided understanding.
"""
    return prompt
