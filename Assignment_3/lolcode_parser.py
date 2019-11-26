from parsimonious.grammar import Grammar

#https://raw.githubusercontent.com/jynnantonix/lolcode/master/BNFGrammar.txt

grammar = Grammar(
    """
    bold_text    = bold_open text bold_close
    text         = ~"[A-Z 0-9]*"i
    bold_open    = "(("
    bold_close   = "))"
    """
    )

#print(grammar.parse('((bold stuff))'))


grammar = Grammar(
    r"""
    program      = "HAI" nlc code_block nlc "KTHXBAI"
    code_block   = (statement nlc )+ / (statement)
    statement    = comment / declaration / input_block / expression / print_block
    loop         = "IM IN YR" ws  label "WILE" ws expression nlc code_block nlc "IM OUTTA YR" ws label
    declaration  = ("I HAS A" ws label) / ("I HAS A" ws label "ITZ " label)
    comment      = ("BTW" ws string) / ("OBTW" ws string ws "TLDR")
    print_block  = ("VISIBLE" ws expression+ ws "MKAY?")
    if_block     = ("O RLY?" ws nlc ws "YA RLY" nlc code_block nlc " OIC") / 
                   ("O RLY? " nlc " YA RLY" nlc code_block nlc else_if_block nlc " OIC")
    else_if_block= ("MEBBE " expression nlc code_block nlc else_if_block) / 
                   ("NO WAI " nlc code_block) / ("MEBBE " expression nlc code_block)
    input_block  = "GIMMEH" ws label
    assignment   = label " R " expression
    expression   = label / atom / both / not_equals / either / greater / less / 
                   add / sub / mul / div / mod / not 

    equals       = "BOTH SAEM" ws expression ws "AN" ws expression
    not_equals   = "DIFFRINT " expression "AN " expression
    both         = "BOTH OF " expression "AN " expression
    either       = "EITHER OF " expression "AN " expression
    greater      = "BIGGR OF " expression "AN " expression
    less         = "SMALLR OF " expression "AN " expression
    add          = "SUM OF " expression "AN " expression
    sub          = "DIFF OF " expression "AN " expression
    mul          = "PRODUKT OF " expression "AN " expression
    div          = "QUOSHUNT OF " expression "AN " expression
    mod          = "MOD OF " expression "AN " expression
    not          = "NOT " expression

    label        = ~"[a-zA-Z0-9]*"
    atom         = (numbers "." numbers) / (quotes string quotes) / "WIN" / "FAIL" / "NOOB" / (numbers)
    quoted       = ~'"[^\"]*"' 
    quotes       = "\""
    numbers      = ~"[0-9]*"i
    string       = ~"[a-zA-Z0-9 ]*" / (~"[a-zA-Z0-9 ]*" ws )+
    ws        = ~"\s*"
    nlc          = ~"\n*" / ~","
    """
    )

f = open("greet_part.lols", "r")
contents = f.read()
print(contents)
print(len(contents))
contents = contents[:len(contents)-1]
print(contents)
print(len(contents))

print(grammar.parse(contents))
#Problem with normal string for atom

'''
Testing:
Comments: HAI,BTW HELLO,KTHXBAI 
Dot in between: HAI,90.74,KTHXBAI
Problem with atom and ("<string>")

'HAI
BTW This is the famous 'Hello World' program
"Hello World"
KTHXBAI
'''



'''
Assuming "<string>" for <atom> is just <string> not sure why it has quotes
Also maybe not sure about <string> is what I have fine?
'''
