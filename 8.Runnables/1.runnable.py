import random

class NakliLLM:

    def __init__(self):
        print('LLM Created')
    
    def predict(self, prompt):
        response_list = [
            'Lahore is the capitol of Punjab',
            'PSL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]
        return {'response': random.choice(response_list)}


class NakliPromptTemplate:
    
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)