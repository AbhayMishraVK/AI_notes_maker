def prompt_to_convert_list(unstructured_string=None):
    base_prompt = f"""
        You are an experienced parser that converts an unstructured string into a Python list of strings.
        
        Instructions:
        1. Do not modify the input string based on your knowledge. Simply parse it into a list where each element is a string.
        2. Do not include any additional output beyond the resulting list.
        
        To parse:
        {unstructured_string}
        
        Example:
        Input: "Photosynthesis\nmicrochonida"
        Output: ['Photosynthesis', 'microchonida']
    """

    return base_prompt
