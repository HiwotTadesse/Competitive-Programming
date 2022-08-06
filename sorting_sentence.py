def sortSentence(s: str) -> str:
        string_list = s.split(" ")
        string_dict = {}
        for astring in string_list:
            string_dict[astring[len(astring)-1]] = astring[:len(astring)-1]
        sorted_sentence = {key:string_dict[key] for key in sorted(string_dict.keys())}

        result = " ".join(sorted_sentence.values())
            
        return result

print(sortSentence("is2 sentence4 This1 a3"))