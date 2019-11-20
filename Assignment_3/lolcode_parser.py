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
    code_block   = statement / (statement nlc code_block)
    statement    = loop / declaration / comment / print_block / expression
    loop         = "IM IN YR" label "WILE" expression nlc code_block nlc "IM OUTTA YR" label
    declaration  = ("I HAS A" label) / ("I HAS A" label "ITZ" label)
    comment      = ("BTW" string) / ("OBTW" string "TLDR")
    print_block  = ("VISIBLE" expression "MKAY?") / (expression expression)
    if_block     = ("O RLY?" nlc "YA RLY" nlc code_block nlc "OIC") / 
                   ("O RLY?" nlc "YA RLY" nlc code_block nlc else_if_block nlc "OIC")
    else_if_block= ("MEBBE" expression nlc code_block nlc else_if_block) / 
                   ("NO WAI" nlc code_block) / ("MEBBE" expression nlc code_block)
    input_block  = "GIMME" label
    assignment   = label "R" expression
    expression   = equals / both / not_equals / either / greater / less / 
                   add / sub / mul / div / mod / not / atom

    equals       = "BOTH SAEM" expression "AN" expression
    not_equals   = "DIFFRINT" expression "AN" expression
    both         = "BOTH OF" expression "AN" expression
    either       = "EITHER OF" expression "AN" expression
    greater      = "BIGGR OF" expression "AN" expression
    less         = "SMALLR OF" expression "AN" expression
    add          = "SUM OF" expression "AN" expression
    sub          = "DIFF OF" expression "AN" expression
    mul          = "PRODUKT OF" expression "AN" expression
    div          = "QUOSHUNT OF" expression "AN" expression
    mod          = "MOD OF" expression "AN" expression
    not          = "NOT" expression

    label        = ~"[a-zA-Z0-9]*"i
    atom         = "WIN" / "FAIL" / "NOOB" / (numbers "." numbers) / (numbers) / (string / quoted)
    quoted       = ~'"[^\"]+"' 
    numbers      = ~"[0-9]*"i
    string       = ~"[a-zA-Z0-9]*"i 
    nlc          = "\n" / ~","
    """
    )

print(grammar.parse('''HAI,WIN,KTHXBAI'''))
#Problem with normal string for atom

'''
Testing:
Comments: HAI,BTW HELLO,KTHXBAI 
Dot in between: HAI,90.74,KTHXBAI
Problem with atom and ("<string>")
'''


'''
    statement   = loop / declaration / comment / print_block / if_block / input_block / func_decl / assignment / expression
    loop        = "IM IN YR" label "WILE" expression nlc codeblock nlc "IM OUTTA YR" label
    declaration = ("I HAS A" label) | ("I HAS A" label "ITZ" value)
'''



'''
To-Do

<program>       ::= HAI <nlc> <code_block> <nlc> KTHXBAI
<code_block>        ::= <statement> | <statement> <nlc> <code_block>
<statement>     ::= <loop> | <declaration> | <comment> | <print_block> |
                    <if_block> | <input_block> | <func_decl> |
                            <assignment> | <expression>
<loop>          ::= IM IN YR <label> WILE <expression> <nlc> <code_block>
                    <nlc> IM OUTTA YR <label>
<declaration>       ::= I HAS A <label> | I HAS A <label> ITZ <value>
<comment>       ::= BTW <string> | OBTW <string> TLDR
<print_block>       ::= VISIBLE <expression> <expression> … <expression> MKAY?
<if_block>      ::= O RLY? <nlc> YA RLY <nlc> <code_block> <nlc> OIC |
                    O RLY? <nlc> YA RLY <nlc> <code_block> <nlc>
                    <else_if_block> <nlc> OIC
<else_if_block>     ::= MEBBE <expression> <nlc> <code_block> <nlc>
                    <else_if_block> | NO WAI <nlc> <code_block> |
                    MEBBE <expression> <nlc> <code_block>
<input_block>       ::= GIMMEH <label>
<func_decl>     ::= HOW DUZ I <label> [[YR <label>] AN YR <label>…] <nlc>
                    <code_block> <nlc> IF U SAY SO
<assignment>        ::= <label> R <expression>
<expression>        ::= <equals> | <both> | <not_equals> | <greater> | <less> |
                    <add> | <sub> | <mul> | <div> | <mod> | <cast> |
                    <either> | <all> | <any> | <not> | <func> | <label> | 
                    <atom>
<equals>        ::= BOTH SAEM <expression> AN <expression>
<not_equals>        ::= DIFFRINT <expression> AN <expression>
<both>          ::= BOTH OF <expression> AN <expression>
<either>        ::= EITHER OF <expression> AN <expression>
<greater>       ::= BIGGR OF <expression> AN <expression>
<less>          ::= SMALLR OF <expression> AN <expression>
<add>           ::= SUM OF <expression> AN <expression>
<sub>           ::= DIFF OF <expression> AN <expression>
<mul>           ::= PRODUKT OF <expression> AN <expression>
<div>           ::= QUOSHUNT OF <expression> AN <expression>
<mod>           ::= MOD OF <expression> AN <expression>
<cast>          ::= MAEK <expression> A <type>
<all>           ::= ALL OF <expression> [AN <expression> … ] MKAY?
<any>           ::= ANY OF <expression> [AN <expression> … ] MKAY?
<not>           ::= NOT <expression>
<func>          ::= <label> <expression> [<expression> … ] MKAY?
<label>         ::= (A-Za-z0-9)*
<atom>          ::= WIN | FAIL | NOOB | (0-9)* | (0-9)*.(0-9)* | "<string>"
'''

'''
Assuming "<string>" for <atom> is just <string> not sure why it has quotes
Also maybe not sure about <string> is what I have fine?
'''
