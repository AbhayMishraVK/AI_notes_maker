def prompt_for_real_life_example(complete_answer):
    prompt = f""" You are an experienced computer science professor with 10 years of expertise in writing real-life examples on various topics. You will be provided with a complete understanding of a topic, and your task is to connect it with relevant real-life examples.

Instructions:

1. Write in simple and easy-to-remember language suitable for exam preparation, ensuring that the content is easily memorable.
2. Avoid using complex words; break down complex concepts into simpler terms.
3. The purpose of these examples is not for students to write them in exams, but rather to help them remember and better understand the concepts by connecting them to real-life scenarios.
4. Relate the concepts to everyday life examples that students can easily grasp.
5. Keep the examples concise, not exceeding 10 words, while capturing the core essence of how the concept relates to the real-life scenario.
6. Try to write it in maximum 200 words, but if it is longer, that's acceptable as long as you don't compromise the clarity and comprehensibility for students.
7. Do not give any conclusion or summary.

Complete Topic Understanding: {complete_answer}

Example:

Example input : 
Complete Topic Understanding: Reinforcement learning is a type of machine learning approach where an agent learns to take actions in an environment to maximize a reward signal. The agent receives rewards or penalties for its actions, and it learns to modify its behavior to maximize the cumulative reward over time.

Example Output:

\n\n**Real-life Example:**\n
(1) Imagine a robot chef learning to cook a new dish through reinforcement learning.
(2) The robot starts with no knowledge of the recipe or cooking process.
(3) It takes an action, such as adding an ingredient or adjusting the heat.
(4) If the action leads to a desired outcome (e.g., the dish tastes better), the robot receives a positive reward.
(5) If the action leads to an undesired outcome (e.g., the dish tastes worse), the robot receives a negative reward or penalty.
(6) Over time, the robot learns which actions lead to positive rewards and adjusts its behavior accordingly.
(7) It may try different combinations of ingredients, cooking times, and temperatures to maximize the reward (deliciousness of the dish).
(8) Through this trial-and-error process and reward/penalty feedback, the robot eventually learns the optimal cooking process for the dish.\n

Please write concise real-life examples based on the provided complete understanding of the topic, connecting the concepts to relatable scenarios from everyday life.
"""

    return prompt




