import re
str1 = "KLEF was established in 1980 at Vaddeswaram as K L College of Engineering (KLCE). " \
       "It became autonomous in 2006 and was recognized as deemed to be university in 2009," \
       " known as K L University.[3] Following the University Grants Commission's request from " \
       "123 deemed institutes, not to use "university" in the name[4] " \
     "it was renamed Koneru Lakshmaiah Education Foundation."\
    " In 2019 it was renamed KL Deemed to be University.[5] The University has recently expanded" \
                                                                                                                                                                                                                                                                                                                 " with a new campus in Bachupally, Hyderabad that has been operational since 2019."
matches1 = re.findall("In",str1)
print(matches1)
matches2 = re.search("name",str1)
print(matches2)
matches3 = re.split(str1,"he")
print(matches3)
matches4 = re.match(str1,"league")
print(matches4)

