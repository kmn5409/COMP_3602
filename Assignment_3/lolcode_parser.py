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
    program     = begin nlc code_block nlc end 
    code_block  = statement / (statement nlc code_block)
    statement   = "HELLO"
    begin       = "HAI"
    nlc         = "\n" / ~","
    end         = "KTHXBAI"
    """
    )

print(grammar.parse('''HAI,HELLO,KTHXBAI'''))



'''
    statement   = loop / declaration / comment / print_block / if_block / input_block / func_decl / assignment / expression
    loop        = "IM IN YR" label "WILE" expression nlc codeblock nlc "IM OUTTA YR" label
'''
