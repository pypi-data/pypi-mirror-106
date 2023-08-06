class Narasimman_nlp:
    def __init__(self,doc):
        self.__doc = doc
    
    def __check_special_character(self,token_string):
        special_characters = [',','"','"','.',':',';','[',']','{','}',"'","'"]
        result = []    
        temp_string = ""
        is_special_charcter = False

        for char in token_string:
            if char not in special_characters:
                temp_string = temp_string+char.strip()
            else:
                is_special_charcter = True
                result.append(temp_string.strip())
                result.append(char.strip())
                temp_string = ""

        if not is_special_charcter:
            result.append(temp_string.strip())
            
        return result

    def tokenize(self):
        _final = []
        for token in self.__doc.split():
            results = self.__check_special_character(token)
            for result in results:
                _final.append(result)
        
        return _final
    
    def sentence(self):
        return self.__doc.split(".")