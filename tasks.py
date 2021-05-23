string = "test case"
def camel_case(string):
    camel_case_fix = string.title()
    return camel_case_fix.replace(" ", "")
print(camel_case(string))


#All types of inputs

#test.describe("Basic tests")
#test.assert_equals(camel_case("test case"), "TestCase")
#test.assert_equals(camel_case("camel case method"), "CamelCaseMethod")
#test.assert_equals(camel_case("say hello "), "SayHello")
#test.assert_equals(camel_case(" camel case word"), "CamelCaseWord")
#test.assert_equals(camel_case(""), "")